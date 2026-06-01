# Day 2：Structured Output 学习笔记

## 今日学习内容

今天的核心目标：把大模型从“会聊天的助手”变成“能被程序稳定调用的组件”。自然语言适合给人读，但 Agent 要决定下一步做什么、调用哪个工具、是否继续追问、是否结束任务，就需要结构化输出。

本节重点学习 5 件事：

1. 为什么 Agent 需要结构化输出，而不是只返回自然语言。
2. JSON Schema 如何约束字段类型、枚举值和必填字段。
3. 如何为 SQL 场景实现一个 intent classifier。
4. 如何处理模型输出不是合法 JSON 的情况。
5. 如何设计解析失败后的有限重试策略。

## 1. 为什么 Agent 需要结构化输出

普通聊天场景里，模型返回一段自然语言就够了，比如：

```text
用户可能是想生成 SQL，我建议先查看表结构。
```

这句话人能看懂，但程序很难稳定处理。不同模型、不同温度、不同上下文下，模型可能会换一种说法：

```text
这个问题看起来属于 SQL 生成任务。
```

或者：

```text
我判断这是 generate_sql，可以调用 SQL 工具。
```

这些表达意思相近，但程序如果靠字符串匹配来判断下一步，就会很脆弱。Agent 系统需要的是确定字段，而不是含糊描述。

更适合 Agent 的输出是：

```json
{
  "intent": "generate_sql",
  "confidence": 0.95,
  "needs_tool": true
}
```

这样程序可以直接读取：

- `intent`：用户意图是什么。
- `confidence`：模型有多确定。
- `needs_tool`：是否需要调用工具。

结构化输出的价值不在于“看起来更像代码”，而在于它把模型回答变成了可校验、可路由、可重试、可记录的数据。

## 2. JSON Schema 是什么

JSON Schema 可以理解为“模型输出的合同”。它规定模型必须返回哪些字段、字段是什么类型、哪些值是允许的。

以今天的 SQL intent classifier 为例，我们希望模型输出：

```json
{
  "intent": "generate_sql",
  "confidence": 0.95,
  "needs_tool": true
}
```

对应的 schema 可以这样设计：

```json
{
  "type": "object",
  "properties": {
    "intent": {
      "type": "string",
      "enum": [
        "generate_sql",
        "fix_sql",
        "explain_sql",
        "summarize_dashboard",
        "recommend_chart",
        "unknown"
      ]
    },
    "confidence": {
      "type": "number",
      "minimum": 0,
      "maximum": 1
    },
    "needs_tool": {
      "type": "boolean"
    }
  },
  "required": ["intent", "confidence", "needs_tool"]
}
```

这里有几个关键点：

- `type`：限制数据类型，比如 object、string、number、boolean、array。
- `properties`：定义对象里有哪些字段。
- `enum`：限制字段只能取固定值，避免模型输出奇怪的新分类。
- `required`：规定哪些字段必须出现。
- `minimum` / `maximum`：限制数值范围，比如 confidence 必须在 0 到 1 之间。

Schema 的作用不是让模型“更聪明”，而是让输出更稳定。Agent 里稳定通常比花哨更重要。

## 3. SQL 场景里的 intent classifier

Intent classifier 的任务是判断用户到底想做什么。对 SQL Agent 来说，常见意图可以分成：

| intent | 含义 | 例子 | 是否通常需要工具 |
| --- | --- | --- | --- |
| `generate_sql` | 生成 SQL | “帮我写一个查询最近 7 天订单的 SQL” | 是 |
| `fix_sql` | 修复 SQL | “这个 SQL 报错了，帮我改一下” | 是 |
| `explain_sql` | 解释 SQL | “解释一下这段 SQL 在做什么” | 否 |
| `summarize_dashboard` | 总结看板 | “帮我总结这个 dashboard 的趋势” | 否或视情况 |
| `recommend_chart` | 推荐图表 | “这个指标适合用什么图展示” | 否或视情况 |
| `unknown` | 无法判断 | “你觉得这个怎么样” | 否 |

分类器输出不要写成长篇解释。它应该像一个路由器，只负责给后续流程一个明确决策：

```json
{
  "intent": "fix_sql",
  "confidence": 0.92,
  "needs_tool": true
}
```

如果 `intent = fix_sql`，后续 Agent 可能进入 SQL 修复流程；如果 `intent = explain_sql`，后续可以进入解释流程；如果 `intent = unknown`，Agent 应该追问用户，而不是强行调用工具。

## 4. 为什么需要 unknown 兜底

很多初学者会只设计几个“正常意图”，不设计 `unknown`。这会导致一个问题：模型被迫在几个选项中硬选。

比如用户输入：

```text
帮我看看这个数据有没有问题
```

它可能是要总结 dashboard，也可能是要生成 SQL，也可能只是想做数据质量检查。如果没有 `unknown`，模型可能随便选一个最接近的意图，后续流程就会走偏。

`unknown` 的作用是承认“不确定”。一个可靠的 Agent 不应该每次都假装知道答案。遇到信息不足时，返回 `unknown`，再让 Agent 追问：

```text
你是想让我生成查询 SQL，还是想让我分析已有 dashboard？
```

这比盲目调用工具更安全。

## 5. 处理模型输出不是合法 JSON 的情况

即使 prompt 里写了“只返回 JSON”，模型也可能输出：

```text
当然可以，下面是结果：
{"intent": "generate_sql", "confidence": 0.95, "needs_tool": true}
```

这不是严格 JSON，因为前面有自然语言。也可能出现字段缺失：

```json
{
  "intent": "generate_sql",
  "confidence": 0.95
}
```

或者类型错误：

```json
{
  "intent": "generate_sql",
  "confidence": "high",
  "needs_tool": "yes"
}
```

所以 Agent 不能直接相信模型输出。至少要做 4 层检查：

1. 能否用 `json.loads()` 解析。
2. 解析结果是不是对象。
3. 必填字段是否都存在。
4. 字段类型和取值范围是否符合 schema。

今天代码里的 `validate_output()` 就是在做这件事：

```python
def validate_output(data: Dict) -> bool:
    if not isinstance(data, dict):
        return False

    required_fields = ["intent", "confidence", "needs_tool"]
    for field in required_fields:
        if field not in data:
            return False

    if not isinstance(data["intent"], str) or data["intent"] not in VALID_INTENTS:
        return False
    if not isinstance(data["confidence"], (float, int)) or not (0 <= data["confidence"] <= 1):
        return False
    if not isinstance(data["needs_tool"], bool):
        return False

    return True
```

这段校验逻辑的意义是：模型可以生成内容，但程序负责把关。

## 6. 有限重试策略

当模型输出不合法时，不应该直接崩溃，也不应该无限重试。更好的策略是：记录错误，给模型一次或两次修复机会。

重试提示要短、明确、只针对格式问题：

```text
上一次输出不是合法 JSON：缺少 required 字段 needs_tool。
请只返回一个符合 schema 的 JSON 对象，不要包含解释文字。
```

有限重试的流程可以这样理解：

```text
模型输出
  ↓
尝试解析 JSON
  ↓
校验字段和类型
  ↓
成功：进入后续 Agent 流程
  ↓
失败：把错误反馈给模型并重试
  ↓
超过最大次数：返回 unknown
```

为什么要限制重试次数？因为 Agent 是一个自动流程，如果没有上限，模型一直输出错，程序就可能卡在循环里。今天代码里使用：

```python
MAX_RETRIES = 2
```

这代表最多给两次修复机会。超过次数后，返回安全兜底：

```python
{"intent": "unknown", "confidence": 0.0, "needs_tool": False}
```

这是一种“失败也可控”的设计。

## 7. 今日代码对应关系

今天的练习代码在：

```text
Day 2：Structured Output/week1/intent_classifier.py
```

可以把它拆成 4 个部分理解：

- `VALID_INTENTS`：定义允许的意图枚举。
- `validate_output()`：检查模型输出是否符合结构。
- `parse_model_output()`：负责 JSON 解析、校验、重试和兜底。
- `classify_intent()`：根据用户输入生成结构化分类结果。

当前代码为了方便练习，用简单规则模拟模型分类：

```python
if "修" in user_input_lower or "错" in user_input_lower:
    intent = "fix_sql"
elif "生成" in user_input_lower or "写sql" in user_input_lower:
    intent = "generate_sql"
```

真实项目里，这一步通常会换成调用大模型，让模型根据用户问题输出 JSON。无论分类来自规则还是模型，后面的校验和兜底逻辑都很重要。

## 8. 可以继续改进的方向

当前版本已经能表达核心思想，但还有几个可以升级的点：

- 使用真正的 JSON Schema 校验库，比如 `jsonschema` 或 Pydantic。
- 给 `intent` 增加 `reason` 字段，用于调试，但不要让路由依赖长文本。
- 在重试时把具体错误传给模型，而不是简单模拟修复。
- 给每个 intent 写测试用例，防止后续修改破坏分类逻辑。
- 增加 `missing_info` 字段，让 Agent 知道下一步应该追问什么。

一个更完整的输出可能是：

```json
{
  "intent": "generate_sql",
  "confidence": 0.91,
  "needs_tool": true,
  "missing_info": ["table_schema"],
  "reason": "用户明确要求生成 SQL，但没有提供表结构"
}
```

不过字段不是越多越好。字段越多，校验和维护成本也越高。初学阶段先把 `intent`、`confidence`、`needs_tool` 做稳定就够了。

## 今日笔记要点

- Agent 需要结构化输出，因为后续流程要靠字段做判断，而不是靠自然语言猜意思。
- JSON Schema 是输出合同，负责约束字段名、类型、枚举值和必填项。
- Intent classifier 本质是路由器，不负责回答所有问题，只负责判断下一步走哪条流程。
- `unknown` 是必要兜底，可以避免模型在不确定时强行分类。
- 模型输出必须校验，不能因为“看起来像 JSON”就直接使用。
- 重试要有限，失败后要回到安全状态，而不是让 Agent 卡死。

## 学习来源

- Hugging Face Agents Course Unit 1：https://huggingface.co/learn/agents-course/en/unit1/introduction
- OpenAI Structured Outputs：https://developers.openai.com/api/docs/guides/structured-outputs
- 学习方法：先理解 Agent 为什么需要可解析输出，再实现 intent JSON、字段校验和失败兜底。

## Hugging Face 对应内容

- 阅读范围：Unit 1 Agent Fundamentals。
- 重点概念：Agent、Tool、Message、Thought、Action、Observation、ReAct。
- 对应关系：结构化输出是 Agent 从“想法”走向“行动”的桥梁。只有输出能被程序解析，Agent 才能稳定选择工具、执行动作、观察结果并继续下一步。

## 我的理解

- 结构化输出不是为了让回答更复杂，而是为了让程序更可靠。
- 自然语言适合解释给人听，JSON 适合交给系统执行。
- Agent 的每一步都应该尽量可校验：输入是什么、输出是什么、为什么进入下一步。

## 今日疑问

### 1. 如果模型多次输出不合法，是 prompt 写得不清楚，还是 schema 设计太复杂？

两种可能都有，需要分开判断。

如果模型经常在 JSON 外面加解释文字，比如“当然可以，下面是结果”，通常是 prompt 约束不够明确。可以在提示词里强调：

```text
只返回 JSON，不要返回 Markdown，不要返回解释文字。
```

如果模型字段经常漏掉、类型经常错，可能是 schema 太复杂，或者字段含义不够清楚。初学阶段不要一次设计太多字段，先保证最关键的 3 个字段稳定：

```json
{
  "intent": "generate_sql",
  "confidence": 0.95,
  "needs_tool": true
}
```

判断方法：

- 输出格式外面混入自然语言：优先优化 prompt。
- 字段太多、含义重叠、模型经常填错：优先简化 schema。
- 某些字段总是模棱两可：给字段补充定义和例子。

工程上不要只靠“让模型听话”。更可靠的做法是：prompt 约束 + schema 校验 + 失败重试 + 安全兜底。

### 2. `confidence` 应该完全相信模型自己给出的分数吗？还是应该结合规则或历史表现再计算？

不应该完全相信模型自己给出的 `confidence`。

模型给出的 confidence 更像是“自我感觉”，可以作为参考，但不能当成严格概率。模型有时会很自信地犯错，也可能在简单问题上给出偏低分数。

更稳妥的做法是把 confidence 当成一个信号，再结合其他规则判断：

- 用户问题是否明确包含关键词，比如“生成 SQL”“解释 SQL”“修复报错”。
- intent 是否容易混淆，比如 `summarize_dashboard` 和 `recommend_chart`。
- 关键上下文是否缺失，比如没有表结构却要求生成 SQL。
- 历史评测里该类任务的准确率如何。

一个简单策略是：

```text
模型 confidence >= 0.8 且字段完整：进入对应流程。
模型 confidence 在 0.5 到 0.8 之间：可以继续，但要更谨慎，必要时追问。
模型 confidence < 0.5：返回 unknown 或追问用户。
```

在真实系统中，confidence 最好不要只由模型决定，而是由“模型判断 + 规则校验 + 上下文完整度”共同决定。

### 3. 什么情况下应该返回 `unknown`，什么情况下应该继续追问更多信息？

`unknown` 表示当前意图无法可靠判断，适合用来兜底。继续追问则是 `unknown` 之后常见的下一步动作。

应该返回 `unknown` 的情况：

- 用户问题太短，比如“帮我看看”。
- 用户目标不明确，比如“这个数据怎么样”。
- 用户输入和已有 intent 都对不上。
- 多个 intent 都可能成立，但没有足够上下文区分。
- 模型输出不合法，并且重试后仍然失败。

应该继续追问的情况：

- 用户确实想做 SQL 相关任务，但缺少必要信息。
- 可以通过一个问题把意图问清楚。
- 继续追问比强行执行工具更安全。

例如用户说：

```text
帮我分析一下这个订单数据。
```

此时可以返回：

```json
{
  "intent": "unknown",
  "confidence": 0.4,
  "needs_tool": false
}
```

然后追问：

```text
你是想让我生成 SQL 查询订单数据，还是想总结已有 dashboard 的指标变化？
```

简单说：`unknown` 是分类结果，追问是下一步动作。一个可靠 Agent 应该允许自己“不确定”，再用追问把任务重新拉回清晰状态。

## 今日小结

今天学到的是 Agent 工程里非常基础但关键的一层：让模型输出变得可控。只要输出能被解析、能被校验、失败能重试、最终能兜底，Agent 才有可能从 demo 走向稳定系统。
