# Day 2：Structured Output

## 今日目标
按照原计划完成 Day 2 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

## 固定学习节奏

| 时间 | 内容 |
|---|---|
| 09:30-11:30 | 看文档 / 看课程 / 做笔记 |
| 11:30-12:00 | 画流程图 / 总结概念 |
| 14:00-17:30 | 写代码 demo / debug |
| 20:00-21:30 | 复盘 / README / 整理项目 |

## 原始计划内容

学习内容：

```text
JSON 输出
JSON Schema
Intent classification
输出校验
解析失败重试
```

资料：

- [OpenAI Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs?api-mode=chat)

作业：

```text
实现 intent classifier。

输入：
"帮我看一下这个 SQL 哪里错了"

输出：
{
  "intent": "fix_sql",
  "confidence": 0.92,
  "needs_tool": true
}
```

要求支持：

```text
generate_sql
fix_sql
explain_sql
summarize_dashboard
recommend_chart
unknown
```

产出：

```text
assignments/week1/intent_classifier.py
```

## 今日学习内容
- 学习为什么 Agent 需要结构化输出，而不是只返回自然语言。
- 理解 JSON Schema、字段类型、枚举值和必填字段。
- 实现 SQL 场景的 intent classifier。
- 处理模型输出不是合法 JSON 的情况。
- 设计解析失败后的有限重试策略。

## 学习内容详解与笔记

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

## Hugging Face Agents Course
- 阅读范围：Unit 1 Agent Fundamentals。
- 重点：Agent、Tool、Message、Thought、Action、Observation、ReAct。
- 写进作业：今天的实现或复盘如何体现这些概念。

## 今日作业
请按上方“原始计划内容”中的作业、要求和产出路径完成今天任务。完成后，把提交说明写到本文件夹的 `assignment.md`，方便 Codex 批改。

## 本章代码
- [code/README.md](code/README.md)

## 本章笔记
- [notes/day02_structured_output.md](notes/day02_structured_output.md)

## 完成标准
- 完成原计划中列出的代码、文档或项目产出。
- 能用自己的话解释今天的核心概念。
- 在 `assignment.md` 中填写完成内容、运行方式、自测结果和疑问。
- 代码类作业至少提供一个可运行示例或自测说明。
- 文档类作业要结合 BI / Superset / SQL Agent 主线。

## 给 Codex 批改时重点看
- 是否满足当天作业的全部要求。
- 产出路径是否和计划一致。
- 代码是否能运行，错误处理是否清楚。
- 解释是否准确，是否贴合 Superset 场景。
