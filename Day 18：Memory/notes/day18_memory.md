# Day 18：Memory 学习笔记

## 今日学习内容
- 实现 SessionMemory 保存会话消息。
- 保存工具结果，让后续推理能看到 observation。
- 实现 get_recent_messages 控制上下文长度。
- 实现 summarize_if_too_long 的简化版本。
- 理解记忆不是无限拼接，而是面向任务保留关键信息。

### SessionMemory
SessionMemory 管理一个会话里的消息、工具结果和摘要。

### add_message
保存用户、助手和系统消息。需要保留顺序。

### add_tool_result
工具结果是 Agent 记忆的一部分，后续推理要能看到。

### get_recent_messages
上下文窗口有限，所以只取最近消息或关键消息。

### summarize_if_too_long
历史太长时做摘要，保留任务目标、关键约束、已完成步骤和未解决问题。

### 今日笔记要点
- Memory 不是把所有内容无限拼接。
- 摘要要服务任务，不是普通聊天总结。

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
