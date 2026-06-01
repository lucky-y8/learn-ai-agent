"""
Day 2 Structured Output - SQL intent classifier

目标：
1. 使用 Day 1 同款 OpenAI 兼容客户端调用模型。
2. 要求模型只输出符合 schema 的 JSON。
3. 校验 intent、confidence、needs_tool 三个字段。
4. 解析失败时有限重试，最终安全兜底为 unknown。
"""

import argparse
import json
import os
from pathlib import Path
from typing import Any, Dict, Tuple


# 当前脚本所在目录：Day 2：Structured Output/week1
SCRIPT_DIR = Path(__file__).resolve().parent

# 项目根目录：D:\ai_agent\learn-ai-agent
# 这里用 parents[1] 是因为 SCRIPT_DIR 的上两级才是项目根目录。
PROJECT_ROOT = SCRIPT_DIR.parents[1]


def load_env_file(path: Path, override: bool = False) -> None:
    """轻量加载 .env；如果安装了 python-dotenv，也兼容 Day 1 的写法。"""
    try:
        # 如果项目已经安装 python-dotenv，就直接使用成熟库读取 .env。
        from dotenv import load_dotenv

        load_dotenv(dotenv_path=path, override=override)
        return
    except ModuleNotFoundError:
        # 没有安装 python-dotenv 时，继续使用下面的简易 .env 解析逻辑。
        pass

    # .env 文件不存在时直接跳过，避免本地演示时因为缺文件报错。
    if not path.exists():
        return

    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()

        # 跳过空行、注释行，以及没有 key=value 结构的行。
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")

        # override=False 时，不覆盖系统里已经存在的环境变量。
        if override or key not in os.environ:
            os.environ[key] = value


# 先加载项目根目录的 .env，再兼容加载当前目录的 .env。
load_env_file(PROJECT_ROOT / ".env")
load_env_file(SCRIPT_DIR / ".env", override=False)


# intent 的枚举值必须固定，避免模型输出 "sql_fix"、"make_chart" 这类程序不认识的值。
VALID_INTENTS = [
    "generate_sql",
    "fix_sql",
    "explain_sql",
    "summarize_dashboard",
    "recommend_chart",
    "unknown",
]

# 最多重试 2 次，防止模型持续输出错误格式导致程序卡死。
MAX_RETRIES = 2

# 这是今天笔记里的核心：用 schema 明确告诉模型输出必须有哪些字段、字段类型是什么。
INTENT_SCHEMA = {
    "type": "object",
    "properties": {
        "intent": {
            "type": "string",
            "enum": VALID_INTENTS,
        },
        "confidence": {
            "type": "number",
            "minimum": 0,
            "maximum": 1,
        },
        "needs_tool": {
            "type": "boolean",
        },
    },
    "required": ["intent", "confidence", "needs_tool"],
}


def create_llm_client() -> Tuple[Any, str]:
    """沿用 Day 1 的多厂商 OpenAI 兼容接口配置。"""
    try:
        # 延迟导入 openai：这样运行 --mock 时即使没装 openai 包也不会报错。
        from openai import OpenAI
    except ModuleNotFoundError as exc:
        raise RuntimeError("缺少 openai 依赖，请先执行 pip install -r requirements.txt") from exc

    # 优先使用 LLM_PROVIDER；如果没配置，就根据已有 API Key 自动选择厂商。
    provider = os.getenv("LLM_PROVIDER")
    if provider:
        provider = provider.lower()
    elif os.getenv("DEEPSEEK_API_KEY"):
        provider = "deepseek"
    elif os.getenv("OPENAI_API_KEY"):
        provider = "openai"
    else:
        provider = "deepseek"

    # 各家厂商都使用 OpenAI 兼容接口，所以可以复用同一个 OpenAI 客户端。
    config_map = {
        "openai": {
            "base_url": os.getenv("OPENAI_BASE_URL"),
            "api_key": os.getenv("OPENAI_API_KEY"),
            "model": os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        },
        "deepseek": {
            "base_url": os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"),
            "api_key": os.getenv("DEEPSEEK_API_KEY"),
            "model": os.getenv("DEEPSEEK_MODEL", "deepseek-chat"),
        },
        "doubao": {
            "base_url": os.getenv(
                "DOUBAO_BASE_URL", "https://ark.cn-beijing.volces.com/api/v3"
            ),
            "api_key": os.getenv("DOUBAO_API_KEY"),
            "model": os.getenv("DOUBAO_MODEL", "doubao-lite-4k"),
        },
        "ali": {
            "base_url": os.getenv(
                "ALI_BASE_URL", "https://dashscope.aliyuncs.com/compatible-mode/v1"
            ),
            "api_key": os.getenv("ALI_API_KEY"),
            "model": os.getenv("ALI_MODEL", "qwen-turbo"),
        },
    }

    if provider not in config_map:
        raise ValueError(f"暂不支持该服务商: {provider}, 可选: {list(config_map)}")

    cfg = config_map[provider]

    # 没有 API Key 时直接报错，避免请求发出去后才看到更难懂的鉴权错误。
    if not cfg["api_key"]:
        raise ValueError(f"缺少 API Key，请在 .env 中配置 {provider.upper()}_API_KEY")

    client_kwargs: Dict[str, Any] = {"api_key": cfg["api_key"]}

    # OpenAI 官方可以不传 base_url；DeepSeek、豆包、阿里百炼通常需要传兼容地址。
    if cfg["base_url"]:
        client_kwargs["base_url"] = cfg["base_url"]

    return OpenAI(**client_kwargs), cfg["model"]


def build_messages(user_input: str, last_error: str = ""):
    # 把 schema 放进 system prompt，让模型清楚知道输出合同。
    schema_text = json.dumps(INTENT_SCHEMA, ensure_ascii=False, indent=2)

    # 这个 system prompt 的重点是限制角色：模型只做分类，不回答 SQL 问题本身。
    system_prompt = f"""
你是 SQL Agent 的 intent classifier。
你的任务不是回答用户问题，而是判断用户意图，并返回机器可读 JSON。

必须只返回一个 JSON 对象，不要返回 Markdown，不要返回解释文字。
JSON 必须符合这个 schema：
{schema_text}

intent 取值说明：
- generate_sql：用户想让你生成 SQL。
- fix_sql：用户想让你修复 SQL、排查 SQL 报错或检查 SQL 哪里错了。
- explain_sql：用户想让你解释 SQL 的含义。
- summarize_dashboard：用户想让你总结 BI dashboard、指标趋势或看板内容。
- recommend_chart：用户想让你推荐图表类型或可视化方式。
- unknown：用户意图不清楚，或不属于以上类型。

判断规则：
- 如果用户提到“报错”“哪里错了”“修一下”“改 SQL”，优先判断为 fix_sql。
- 如果用户提到“生成”“写一个查询”“帮我写 SQL”，优先判断为 generate_sql。
- 如果信息不足，不要强行分类，返回 unknown。
- confidence 是 0 到 1 之间的数字。
- needs_tool 表示后续是否通常需要调用 SQL 或元数据工具。
- 如果用户输入同时包含多个互相冲突的意图，并且没有明确主语或最终目标，就返回 unknown，不要强行分类。
""".strip()

    if last_error:
        # 如果上一次输出不合法，把具体错误反馈给模型，让它下一次只修格式。
        system_prompt += f"\n\n上一次输出不合法：{last_error}\n请修复格式，只返回合法 JSON。"

    # Chat Completions API 使用 messages 数组：system 设规则，user 放真实输入。
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input},
    ]


def validate_output(data: Any) -> Tuple[bool, str]:
    """校验模型输出是否符合今日笔记中的结构化输出要求。"""
    # 第 1 层校验：输出必须是 JSON object，而不是数组、字符串或数字。
    if not isinstance(data, dict):
        return False, "输出不是 JSON object"

    # 第 2 层校验：required 中的字段必须全部存在。
    for field in INTENT_SCHEMA["required"]:
        if field not in data:
            return False, f"缺少必填字段: {field}"

    # 第 3 层校验：intent 必须属于预设枚举值。
    if data["intent"] not in VALID_INTENTS:
        return False, f"intent 不在枚举范围内: {data['intent']}"

    # 第 4 层校验：confidence 必须是数字，不能是 "high" 这类自然语言。
    if not isinstance(data["confidence"], (int, float)):
        return False, "confidence 必须是 number"

    # confidence 的取值范围固定在 0 到 1。
    if not 0 <= data["confidence"] <= 1:
        return False, "confidence 必须在 0 到 1 之间"

    # needs_tool 必须是真正的布尔值 true/false，不能是 "yes" 或 1。
    if not isinstance(data["needs_tool"], bool):
        return False, "needs_tool 必须是 boolean"

    return True, ""


def parse_json_object(model_response: str) -> Dict[str, Any]:
    """严格解析 JSON；不做自然语言截取，避免默许模型输出脏格式。"""
    # 如果模型输出了 Markdown、解释文字或半截 JSON，这里会抛出 JSONDecodeError。
    return json.loads(model_response)


def call_model(user_input: str, last_error: str = "") -> str:
    # 每次调用都创建客户端，便于读取最新环境变量；小作业里这样最直观。
    client, model = create_llm_client()

    # temperature=0 让分类结果尽量稳定，减少同一个输入多次分类不一致。
    response = client.chat.completions.create(
        model=model,
        messages=build_messages(user_input, last_error),
        temperature=0,
    )
    content = response.choices[0].message.content
    return content.strip() if content else ""


def fallback_classify(user_input: str) -> Dict[str, Any]:
    """无网络或课堂演示时使用的本地兜底，不替代真实模型调用。"""
    # mock 模式用简单关键词模拟模型输出，方便检查 JSON 结构和运行流程。
    text = user_input.lower()

    # 修复类问题：报错、哪里错了、修一下，通常需要后续 SQL 工具参与。
    if "修" in text or "错" in text or "报错" in text or "error" in text:
        return {"intent": "fix_sql", "confidence": 0.92, "needs_tool": True}

    # 生成类问题：用户明确要求写 SQL 或查询。
    if "生成" in text or "写sql" in text or "写 sql" in text or "查询" in text:
        return {"intent": "generate_sql", "confidence": 0.9, "needs_tool": True}

    # 解释类问题：通常不一定需要调用工具，直接解释已有 SQL 即可。
    if "解释" in text or "说明" in text:
        return {"intent": "explain_sql", "confidence": 0.88, "needs_tool": False}

    # 看板总结类问题：更偏 BI / dashboard 分析。
    if "dashboard" in text or "看板" in text or "总结" in text:
        return {"intent": "summarize_dashboard", "confidence": 0.82, "needs_tool": False}

    # 可视化建议类问题：给用户推荐图表类型。
    if "图表" in text or "可视化" in text or "推荐" in text:
        return {"intent": "recommend_chart", "confidence": 0.82, "needs_tool": False}

    # 信息不足时不要强行分类，返回 unknown。
    return {"intent": "unknown", "confidence": 0.4, "needs_tool": False}


def classify_intent(user_input: str, use_mock: bool = False) -> Dict[str, Any]:
    # --mock 模式不调用模型，便于没网络或没 API Key 时完成课堂自测。
    if use_mock:
        return fallback_classify(user_input)

    last_error = ""

    # 总尝试次数 = 第一次调用 + MAX_RETRIES 次重试。
    for attempt in range(MAX_RETRIES + 1):
        try:
            # 1. 调模型，让模型按 schema 返回 JSON 字符串。
            raw_output = call_model(user_input, last_error)

            # 2. 严格解析 JSON，格式不合法会进入 except。
            data = parse_json_object(raw_output)

            # 3. 校验字段是否存在、类型是否正确、枚举值是否合法。
            is_valid, error = validate_output(data)
            if is_valid:
                return data

            # JSON 能解析但字段不符合要求时，把错误保存下来用于下一轮重试提示。
            last_error = error
        except Exception as exc:
            # JSON 解析失败、模型调用失败、依赖缺失等错误都会走到这里。
            last_error = str(exc)

        if attempt < MAX_RETRIES:
            print(f"输出不合法，准备重试 {attempt + 1}/{MAX_RETRIES}: {last_error}")

    # 所有重试都失败时，返回安全兜底，避免 Agent 继续执行错误工具调用。
    return {"intent": "unknown", "confidence": 0.0, "needs_tool": False}


def main() -> None:
    # 命令行入口，支持直接传入一句用户问题进行测试。
    parser = argparse.ArgumentParser(description="SQL intent classifier")
    parser.add_argument(
        "query",
        nargs="?",
        default="帮我看一下这个 SQL 哪里错了",
        help="需要分类的用户输入",
    )
    parser.add_argument(
        "--mock",
        action="store_true",
        help="不调用模型，使用本地规则验证输出结构",
    )
    args = parser.parse_args()

    # 最终只打印结构化 JSON，方便后续程序继续读取。
    result = classify_intent(args.query, use_mock=args.mock)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
