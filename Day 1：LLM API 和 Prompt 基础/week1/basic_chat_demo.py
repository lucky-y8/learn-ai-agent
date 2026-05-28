"""
Day1 LLM API & Prompt 基础 - 最小 Chat Demo
适配 OpenAI 兼容接口，支持 OpenAI / DeepSeek / 豆包 / 阿里百炼切换
作业要求：支持 system prompt、user prompt、输出模型回复、多厂商切换
"""
import os
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

# 优先加载项目根目录 .env；如果章节目录下也有 .env，则作为兼容补充。
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parents[1]
load_dotenv(dotenv_path=PROJECT_ROOT / ".env")
load_dotenv(dotenv_path=SCRIPT_DIR / ".env", override=False)

def create_llm_client():
    """根据环境变量创建 LLM 客户端，支持多厂商切换"""
    provider = os.getenv("LLM_PROVIDER")
    if provider:
        provider = provider.lower()
    elif os.getenv("DEEPSEEK_API_KEY"):
        provider = "deepseek"
    elif os.getenv("OPENAI_API_KEY"):
        provider = "openai"
    else:
        provider = "deepseek"

    # 各厂商 OpenAI 兼容接口配置
    config_map = {
        "openai": {
            "base_url": os.getenv("OPENAI_BASE_URL"),
            "api_key": os.getenv("OPENAI_API_KEY"),
            "model": os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        },
        "deepseek": {
            "base_url": os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"),
            "api_key": os.getenv("DEEPSEEK_API_KEY"),
            "model": os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
        },
        "doubao": {
            "base_url": os.getenv("DOUBAO_BASE_URL", "https://ark.cn-beijing.volces.com/api/v3"),
            "api_key": os.getenv("DOUBAO_API_KEY"),
            "model": os.getenv("DOUBAO_MODEL", "doubao-lite-4k")
        },
        "ali": {
            "base_url": os.getenv("ALI_BASE_URL", "https://dashscope.aliyuncs.com/compatible-mode/v1"),
            "api_key": os.getenv("ALI_API_KEY"),
            "model": os.getenv("ALI_MODEL", "qwen-turbo")
        }
    }

    if provider not in config_map:
        raise ValueError(f"暂不支持该服务商: {provider}, 可选: {list(config_map.keys())}")

    cfg = config_map[provider]
    if not cfg["api_key"]:
        raise ValueError(f"缺少 API Key，请在 .env 中配置 {provider.upper()}_API_KEY")

    client_kwargs = {"api_key": cfg["api_key"]}
    if cfg["base_url"]:
        client_kwargs["base_url"] = cfg["base_url"]

    client = OpenAI(**client_kwargs)
    return client, cfg["model"]

def chat(system_prompt: str, user_prompt: str, temperature: float = 0.2) -> str:
    """
    对话主函数
    :param system_prompt: 角色/规则约束
    :param user_prompt: 用户提问
    :param temperature: 随机性系数，SQL/工具场景建议低数值
    :return: 模型回复文本
    """
    client, model = create_llm_client()
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    try:
        resp = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        return f"调用模型失败: {str(e)}"

if __name__ == "__main__":
    # 测试用例：结合 Superset / SQL Agent 场景
    system_text = "你是专业的SQL助手，基于Apache Superset编写标准SQL，只输出可执行SQL，不额外解释。"
    user_text = "查询近30天每日订单总数，按日期升序排列"

    print("===== System Prompt =====")
    print(system_text)
    print("\n===== User Prompt =====")
    print(user_text)
    print("\n===== 模型回复 =====")
    result = chat(system_text, user_text)
    print(result)
