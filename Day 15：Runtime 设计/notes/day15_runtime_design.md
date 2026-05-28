# Day 15：Runtime 设计 学习笔记

## 今日学习内容
- 设计 mini_agent 的基础 runtime 数据结构。
- 实现 Message，明确 role/content/tool_call 等字段。
- 实现 AgentState，保存任务执行状态。
- 实现 ToolCall、ToolResult，统一工具调用协议。
- 实现 AgentConfig，保存模型、步数和工具配置。

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

## Hugging Face 对应内容
- 阅读范围：Unit 1 复习 + Unit 2 框架概览。
- 重点：框架解决的是状态、工具、执行循环、记忆和编排问题。
- 写进作业：说明你手搓的模块对应哪个 Agent 概念。

## 我的理解
- 

## 今日疑问
- 

## 今日小结
- 
