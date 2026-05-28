# Day 17：Agent Executor 学习笔记

## 今日学习内容
- 实现 ReAct executor 的主循环。
- 实现 call_model、parse_action、run_tool、append_observation 的骨架。
- 支持 max_steps 防止无限循环。
- 支持 final answer 停止条件。
- 把 tool error 作为 observation 放回状态。

### ReAct executor
Executor 管理循环：call_model、parse_action、run_tool、append_observation。

### max_steps
max_steps 是防止无限循环的硬限制。达到上限要返回失败原因或部分结果。

### final answer
模型必须有明确格式告诉执行器任务结束，例如 action=final 或 final_answer 字段。

### tool error observation
工具失败也要追加到 messages，让模型看到错误并调整策略。

### 今日笔记要点
- Executor 不负责业务逻辑，它负责流程推进。
- 每一步都要可日志化。

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
