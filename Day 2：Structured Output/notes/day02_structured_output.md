# Day 2：Structured Output 学习笔记

## 今日学习内容
- 学习为什么 Agent 需要结构化输出，而不是只返回自然语言。
- 理解 JSON Schema、字段类型、枚举值和必填字段。
- 实现 SQL 场景的 intent classifier。
- 处理模型输出不是合法 JSON 的情况。
- 设计解析失败后的有限重试策略。

### JSON 输出
JSON 输出让模型回答变成程序可以读取的数据。Agent 里不能只靠自然语言判断下一步，必须把 intent、confidence、needs_tool 等字段变成稳定结构。

### JSON Schema
JSON Schema 用来约束字段名、类型、枚举值和必填项。比如 intent 只能是 generate_sql、fix_sql、explain_sql、summarize_dashboard、recommend_chart、unknown。

### Intent classification
Intent classification 是把用户问题归类。SQL Agent 需要先判断用户是要生成 SQL、修 SQL、解释 SQL、总结 dashboard，还是推荐图表。分类结果会影响后续工具路由和提示词。

### 输出校验
不要默认相信模型输出。需要 parse JSON、检查字段是否存在、类型是否正确、intent 是否在枚举里、confidence 是否在 0-1。校验失败要给模型一次修复机会。

### 解析失败重试
重试提示要短而明确：指出模型上一次输出哪里不合法，并要求只返回符合 schema 的 JSON。重试次数要有限制，避免 Agent 卡死。

### 今日笔记要点
- 结构化输出是 Agent 可编排的前提。
- 分类器不需要“聪明地回答”，只需要稳定地产生机器可读决策。
- unknown 是必要兜底，能防止模型强行分类。

## 学习来源
- Hugging Face Agents Course Unit 1：https://huggingface.co/learn/agents-course/en/unit1/introduction
- OpenAI Structured Outputs：https://developers.openai.com/api/docs/guides/structured-outputs
- 学习方法：先理解 Agent 为什么需要可解析输出，再照 structured outputs 文档实现 intent JSON 和校验。

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
