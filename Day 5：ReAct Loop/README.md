# Day 5：ReAct Loop

## 今日目标
按照原计划完成 Day 5 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

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
Reason -> Act -> Observe
最大循环次数
停止条件
工具调用结果如何回填给模型
```

作业：

```text
写一个最小 ReAct SQL Agent。

用户输入：
"帮我写一个查询每月销售额趋势的 SQL"

Agent 流程：
1. 调 get_dataset_columns
2. 根据字段生成 SQL
3. 调 validate_sql
4. 返回 SQL 和解释
```

限制：

```text
最多 5 次工具调用
工具失败后最多重试 1 次
必须输出最终 answer
```

产出：

```text
assignments/week1/react_sql_agent.py
```

## 今日学习内容
- 理解 ReAct 的 Reason -> Act -> Observe 循环。
- 学习最大工具调用次数和停止条件。
- 把工具执行结果作为 observation 回填给模型。
- 实现最小 ReAct SQL Agent。
- 处理工具失败后的 1 次重试和最终 answer。

## 学习内容详解与笔记

### Reason -> Act -> Observe
ReAct 的核心是让模型先推理下一步，再选择动作，再观察工具结果。SQL Agent 中可以是：想知道字段 -> 调 schema 工具 -> 看到字段 -> 生成 SQL -> 调校验工具。

### 最大循环次数
必须设置 max_steps 或 max_tool_calls。否则模型可能在工具调用和观察之间无限循环。今天限制最多 5 次工具调用。

### 停止条件
停止条件可以是模型输出 final answer、达到最大步数、遇到不可恢复错误、用户取消。执行器要明确识别 final answer。

### 工具结果回填
工具结果要作为 observation 放回消息历史，让模型基于真实结果继续推理。不要让模型“假装已经查过 schema”。

### 失败重试
工具失败后可以最多重试 1 次。重试时要把失败原因告诉模型，例如 dataset_id 不存在或 SQL 包含禁止语句。

### 今日笔记要点
- ReAct 适合需要多步决策的任务。
- SQL Agent 的每一步都要可追踪。
- 最终 answer 必须包含 SQL 和解释，而不是只给中间过程。

## 学习来源
- Hugging Face Agents Course Unit 1 ReAct / Thought-Action-Observation：https://huggingface.co/learn/agents-course/en/unit1/introduction
- Datawhale Hello-Agents：https://github.com/datawhalechina/hello-agents
- 学习方法：看懂 ReAct 循环后，用 mock SQL tools 手写一轮 Reason -> Act -> Observe。

## Hugging Face Agents Course
- 阅读范围：Unit 1 Agent Fundamentals。
- 重点：Agent、Tool、Message、Thought、Action、Observation、ReAct。
- 写进作业：今天的实现或复盘如何体现这些概念。

## 今日作业
请按上方“原始计划内容”中的作业、要求和产出路径完成今天任务。完成后，把提交说明写到本文件夹的 `assignment.md`，方便 Codex 批改。

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
