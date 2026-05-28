# Day 21：复盘 学习笔记

## 今日学习内容
- 复盘不用框架时 Agent 至少需要哪些模块。
- 解释 Model Client、Tool Registry、Executor、Memory、Planner 的职责。
- 补充 Policy Guard 和 Logger 在生产中的必要性。
- 把这些模块映射到 Handmade SQL Agent。
- 形成一篇可作为后续架构说明的总结。

### Model Client
封装 provider 差异，统一 call_model 接口。

### Tool Registry
统一管理工具 schema 和执行。

### Executor
推进 ReAct 或 plan-execute 循环。

### Memory
保存消息、工具结果、摘要和关键状态。

### Planner
把复杂任务拆成步骤。

### Policy Guard
检查权限、SQL 安全、风险动作和用户确认。

### Logger
记录输入、输出、工具调用、错误和耗时。

### 今日笔记要点
- 复盘要回答“最少需要哪些模块以及为什么”。

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
