# Day 5：ReAct Loop 学习笔记

## 今日学习内容
- 理解 ReAct 的 Reason -> Act -> Observe 循环。
- 学习最大工具调用次数和停止条件。
- 把工具执行结果作为 observation 回填给模型。
- 实现最小 ReAct SQL Agent。
- 处理工具失败后的 1 次重试和最终 answer。

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
