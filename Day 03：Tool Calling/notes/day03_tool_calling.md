# Day 3：Tool Calling 学习笔记

## 今日学习内容

今天的核心目标：理解 Agent 如何通过工具连接外部系统。模型本身不会查数据库、不会读 Superset 元数据、不会真正执行 SQL；它只能根据上下文选择“应该调用哪个工具”以及“传什么参数”。真正执行工具的是代码。

本节重点学习 6 件事：

1. Tool Calling 中模型和代码的分工。
2. Tool schema 如何描述工具能力和参数。
3. 如何实现 4 个 Superset / BI 风格 mock tools。
4. 如何设计结构化 tool result 和 tool error。
5. 如何展示“模型选择工具，代码执行工具，结果回填”的流程。
6. 为什么工具失败也是一次 observation，而不是简单报错退出。

## 1. 模型和代码的分工

Tool Calling 里最容易误解的一点是：模型不会真的执行工具。

模型负责：

- 理解用户意图。
- 根据 tool schema 选择工具。
- 生成工具参数。

代码负责：

- 校验工具名是否存在。
- 校验参数是否正确。
- 调用真实函数或外部 API。
- 捕获异常。
- 返回结构化结果。

例如用户说：

```text
帮我看一下 sales 数据集有哪些字段
```

模型应该输出类似：

```json
{
  "name": "get_dataset_columns",
  "arguments": {
    "dataset_id": "sales"
  }
}
```

但真正去查 `sales` 字段列表的是 Python 代码里的 `get_dataset_columns("sales")`。

## 2. Tool schema 是什么

Tool schema 是给模型看的工具说明书。它告诉模型：

- 工具叫什么名字。
- 工具能做什么。
- 工具需要哪些参数。
- 参数是什么类型。
- 哪些参数是必填的。

以 `get_dataset_columns` 为例：

```json
{
  "name": "get_dataset_columns",
  "description": "查询 Superset 数据集的字段列表",
  "parameters": {
    "type": "object",
    "properties": {
      "dataset_id": {
        "type": "string",
        "description": "数据集 ID"
      }
    },
    "required": ["dataset_id"]
  }
}
```

schema 写得清楚，模型就更容易传对参数。schema 写得模糊，模型可能会传错字段名，比如把 `dataset_id` 写成 `dataset_name`。

## 3. 本日 4 个 mock tools

今天实现的工具都放在：

```text
Day 3：Tool Calling/week1/tools.py
```

### get_dataset_columns(dataset_id)

用途：查询数据集有哪些字段。

示例：

```python
get_dataset_columns("sales")
```

返回：

```json
{
  "ok": true,
  "data": {
    "dataset_id": "sales",
    "columns": ["ds", "region", "revenue", "quantity"]
  },
  "error": null
}
```

### get_dataset_metrics(dataset_id)

用途：查询数据集有哪些指标。

例如 `sales` 数据集可以有：

```json
["sum_revenue", "avg_order_value", "total_quantity"]
```

这些指标可以帮助后续 Agent 生成 SQL 或推荐图表。

### validate_sql(sql)

用途：校验 SQL 是否安全、是否符合只读查询要求。

今天的 mock 版本只做简单规则：

- SQL 不能为空。
- 必须以 `SELECT` 开头。
- 不允许 `INSERT`、`UPDATE`、`DELETE`、`DROP`、`ALTER`、`TRUNCATE`。
- 查询需要包含 `FROM`。

这不是生产级 SQL 校验，但它能表达一个关键思想：安全相关工具必须返回明确 reason，不能只返回 true / false。

### recommend_chart_type(columns)

用途：根据字段列表推荐图表类型。

简单规则：

- 有时间字段和指标字段：推荐折线图。
- 有类别字段和指标字段：推荐柱状图。
- 不确定时：推荐表格。

这体现了 BI Agent 的基本思路：先理解字段结构，再决定可视化方式。

## 4. Tool result 和 Tool error

工具返回结果要结构化。不要让每个工具随便返回不同格式，否则执行器和后续 Agent 会很难处理。

今天统一使用：

```json
{
  "ok": true,
  "data": {},
  "error": null
}
```

失败时使用：

```json
{
  "ok": false,
  "data": null,
  "error": {
    "code": "dataset_not_found",
    "message": "未知 dataset_id: xxx"
  }
}
```

这样做的好处是：

- 程序可以稳定判断 `ok`。
- 成功结果都放在 `data`。
- 失败原因都放在 `error`。
- 模型或执行器可以根据 `error.code` 决定是否重试。

## 5. 工具执行器

工具执行器负责把模型输出的 tool call 变成真实函数调用。

在今天的 demo 里，tool call 长这样：

```json
{
  "name": "validate_sql",
  "arguments": {
    "sql": "select ds, revenue from sales"
  }
}
```

执行器做的事：

1. 检查 `name` 是否在工具注册表里。
2. 取出对应 Python 函数。
3. 把 `arguments` 传给函数。
4. 捕获参数错误或运行时错误。
5. 返回结构化 tool result。

这一步很重要，因为模型输出不等于可信执行。执行器是模型和真实系统之间的安全边界。

## 6. demo 对应关系

今天的 demo 文件是：

```text
Day 3：Tool Calling/week1/tool_calling_demo.py
```

核心结构：

- `TOOL_SCHEMAS`：工具说明，给模型看。
- `TOOL_REGISTRY`：工具注册表，给代码执行器用。
- `select_tool_call()`：模拟模型选择工具。
- `execute_tool_call()`：执行工具并捕获错误。
- `run_demo()`：串起完整流程。

运行示例：

```bash
python "Day 3：Tool Calling/week1/tool_calling_demo.py" "帮我看一下 sales 数据集有哪些字段"
```

输出会包含：

```json
{
  "user_input": "...",
  "tool_call": {
    "name": "get_dataset_columns",
    "arguments": {
      "dataset_id": "sales"
    }
  },
  "tool_result": {
    "ok": true,
    "data": {
      "dataset_id": "sales",
      "columns": ["ds", "region", "revenue", "quantity"]
    },
    "error": null
  }
}
```

## 7. 今日笔记要点

- 工具是模型连接外部世界的接口。
- 模型选择工具，但不执行工具。
- 代码执行工具，并负责安全、校验、异常处理。
- Tool schema 越清楚，模型越不容易传错参数。
- Tool result 和 tool error 要统一格式。
- 工具失败也是 observation，Agent 可以基于失败结果继续决策。

## 学习来源

- Hugging Face Agents Course Unit 1 Tools / Actions / Observations：https://huggingface.co/learn/agents-course/en/unit1/introduction
- OpenAI Function Calling：https://developers.openai.com/api/docs/guides/function-calling
- 学习方法：先理解 Agent / Tool / Observation 的概念，再用本地 mock tools 模拟真实工具调用链路。

## Hugging Face 对应内容

- 阅读范围：Unit 1 Agent Fundamentals。
- 重点概念：Agent、Tool、Message、Thought、Action、Observation、ReAct。
- 对应关系：Tool Calling 对应 ReAct 里的 Action 和 Observation。模型选择 Action，代码执行工具并返回 Observation。

## 我的理解

- Tool Calling 不是让模型“拥有工具”，而是让模型“请求代码调用工具”。
- 工具调用的关键不是函数多复杂，而是输入输出契约是否稳定。
- 对 Agent 来说，错误结果也有价值，因为它能帮助下一步重试、追问或停止。

## 今日疑问

### 1. 为什么不直接让模型自己回答字段、指标和图表推荐？

因为模型的知识可能过期，也不知道当前 Superset 里的真实数据集结构。字段、指标、权限、SQL 校验这些信息应该来自工具或系统，而不是模型猜。

模型适合做语义理解和决策，工具适合提供真实数据和确定结果。

### 2. tool schema 是不是越详细越好？

不是。schema 要足够清楚，但不要复杂到模型难以稳定填写。

好的 schema 应该做到：

- 工具职责单一。
- 参数名清楚。
- 参数类型明确。
- description 能说明什么时候使用。

如果一个工具参数太多，或者一个工具同时做很多事，模型更容易传错参数。生产环境里通常会把复杂能力拆成多个小工具。

### 3. 工具执行失败时，应该直接抛异常还是返回 error？

Agent 流程里更推荐返回结构化 error。

直接抛异常适合程序 bug；但很多工具失败是业务上的正常情况，比如 dataset 不存在、SQL 不安全、参数缺失。这些应该作为 observation 返回给 Agent。

例如：

```json
{
  "ok": false,
  "error": {
    "code": "dataset_not_found",
    "message": "未知 dataset_id: finance"
  }
}
```

这样 Agent 可以继续追问用户：“没有找到 finance 数据集，你要查看 sales 还是 orders？”

## 今日小结

今天完成了 Tool Calling 的最小闭环：定义工具、描述工具、选择工具、执行工具、返回结果。这个闭环是后续 ToolRegistry、Agent Executor、ReAct Loop 的基础。工具越稳定，Agent 的行动就越可靠。
