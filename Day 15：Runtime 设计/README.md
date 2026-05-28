# Day 15：Runtime 设计

## 今日目标
按照原计划完成 Day 15 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

## 固定学习节奏

| 时间 | 内容 |
|---|---|
| 09:30-11:30 | 看文档 / 看课程 / 做笔记 |
| 11:30-12:00 | 画流程图 / 总结概念 |
| 14:00-17:30 | 写代码 demo / debug |
| 20:00-21:30 | 复盘 / README / 整理项目 |

## 原始计划内容

作业：

```text
设计并实现：

Message
AgentState
ToolCall
ToolResult
AgentConfig
```

产出：

```text
mini_agent/message.py
mini_agent/state.py
```

## 今日学习内容
- 设计 mini_agent 的基础 runtime 数据结构。
- 实现 Message，明确 role/content/tool_call 等字段。
- 实现 AgentState，保存任务执行状态。
- 实现 ToolCall、ToolResult，统一工具调用协议。
- 实现 AgentConfig，保存模型、步数和工具配置。

## 学习内容详解与笔记

### Message
Message 表示对话中的一条消息，通常包含 role、content、name、tool_call_id 等。

### AgentState
AgentState 保存当前任务状态，例如 messages、intent、tool_calls、observations、final_answer。

### ToolCall
ToolCall 表示模型想调用的工具，包括 tool name 和 arguments。

### ToolResult
ToolResult 表示工具执行结果，包括 success、data、error、duration_ms。

### AgentConfig
AgentConfig 保存 max_steps、model、temperature、enabled_tools 等配置。

### 今日笔记要点
- Runtime 数据结构决定后面 Agent 是否好扩展。
- 先用 dataclass 或 Pydantic 定义清楚边界。

## 学习来源
- Datawhale Hello-Agents：https://github.com/datawhalechina/hello-agents
- Hugging Face Agents Course Unit 1：https://huggingface.co/learn/agents-course/en/unit1/introduction
- Hugging Face Agents Course：https://huggingface.co/learn/agents-course/en
- 学习方法：Datawhale 作为中文主线，HF 作为概念校准，目标是手搓 Message/State/Tool/Executor/Memory/Planner。

## Hugging Face Agents Course
- 阅读范围：Unit 1 复习 + Unit 2 框架概览。
- 重点：框架解决的是状态、工具、执行循环、记忆和编排问题。
- 写进作业：说明你手搓的模块对应哪个 Agent 概念。

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
