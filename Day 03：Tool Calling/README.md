# Day 3：Tool Calling

## 今日目标
按照原计划完成 Day 3 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

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
Tool schema
Tool input/output
Tool error
Tool result
模型选择工具
工具执行器
```

资料：

- [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling?api-mode=chat)

作业：

```text
实现 4 个 mock tools：

get_dataset_columns(dataset_id)
get_dataset_metrics(dataset_id)
validate_sql(sql)
recommend_chart_type(columns)
```

示例：

```python
get_dataset_columns("sales")
# 返回 ["ds", "region", "revenue", "quantity"]
```

产出：

```text
assignments/week1/tools.py
assignments/week1/tool_calling_demo.py
```

## 今日学习内容
- 理解 Tool Calling 中模型和代码的分工。
- 学习 tool schema 如何描述工具能力和参数。
- 实现 4 个 Superset/BI 风格 mock tools。
- 设计结构化 tool result 和 tool error。
- 写一个 demo 展示模型选择工具、代码执行工具、结果回填。

## 学习内容详解与笔记

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

## Hugging Face Agents Course
- 阅读范围：Unit 1 Agent Fundamentals。
- 重点：Agent、Tool、Message、Thought、Action、Observation、ReAct。
- 写进作业：今天的实现或复盘如何体现这些概念。

## 今日作业
请按上方“原始计划内容”中的作业、要求和产出路径完成今天任务。完成后，把提交说明写到本文件夹的 `assignment.md`，方便 Codex 批改。

## 本章代码
- [code/README.md](code/README.md)

## 本章笔记
- [notes/day03_tool_calling.md](notes/day03_tool_calling.md)

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
