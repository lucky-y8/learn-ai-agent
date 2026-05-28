# Day 3：Tool Calling 学习笔记

## 今日学习内容
- 理解 Tool Calling 中模型和代码的分工。
- 学习 tool schema 如何描述工具能力和参数。
- 实现 4 个 Superset/BI 风格 mock tools。
- 设计结构化 tool result 和 tool error。
- 写一个 demo 展示模型选择工具、代码执行工具、结果回填。

### Tool schema
Tool schema 是告诉模型“有哪些工具、每个工具需要什么参数、能做什么”。schema 写得越清楚，模型越不容易传错参数。

### Tool input/output
工具输入要尽量结构化，例如 dataset_id、sql、columns。工具输出也要结构化，例如 columns 数组、valid 布尔值、reason 字符串。

### Tool error
工具失败不是异常结束，而是一次 observation。Agent 应该把错误返回给模型或执行器，让它决定重试、换工具或最终失败。

### 模型选择工具
模型并不真正执行工具，它只是根据用户问题和 tool schema 选择工具并生成参数。真正执行发生在你的代码里。

### 工具执行器
执行器负责接收 tool call、校验参数、调用本地函数、捕获错误、返回 tool result。后面 ToolRegistry 会把这层抽象出来。

### 今日笔记要点
- 工具是模型连接外部世界的接口。
- mock tools 先不要复杂，重点是输入输出契约清楚。
- validate_sql 是安全相关工具，要返回明确 reason。

## 学习来源
- Hugging Face Agents Course Unit 1 Tools/Actions/Observations：https://huggingface.co/learn/agents-course/en/unit1/introduction
- OpenAI Function Calling：https://developers.openai.com/api/docs/guides/function-calling
- 学习方法：HF 学概念，OpenAI 文档学 tool schema 和 tool call 的实际接口格式。

## Hugging Face 对应内容
- 阅读范围：Unit 1 Agent Fundamentals。
- 重点：Agent、Tool、Message、Thought、Action、Observation、ReAct。
- 写进作业：今天的实现或复盘如何体现这些概念。

## 我的理解
- 

## 今日疑问
- 

## 今日小结
- 
