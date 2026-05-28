# Day 20：周项目 3 学习笔记

## 今日学习内容
- 整合 ToolRegistry、Memory、Executor、Planner、SQL tools。
- 实现 Handmade SQL Agent 项目。
- 保持不使用 LangGraph、CrewAI、AutoGen、Microsoft Agent Framework。
- 写清项目结构和运行方式。
- 用示例展示手搓 Agent 的完整执行流程。

### Handmade SQL Agent
这是一个完整手搓 Agent：ToolRegistry、Memory、Executor、Planner、SQL tools 都要能协作。

### 不用框架的意义
不用框架是为了理解底层模块边界。之后用 LangGraph 才知道它帮你省了什么。

### SQL tools
至少包含 schema 查询、SQL 生成辅助、SQL guard、validate_sql。

### 项目结构
建议把 mini_agent 框架代码和 SQL assistant 业务代码分开。

### 今日笔记要点
- 重点是模块边界清楚，不是代码量大。
- README 要画出执行流程。

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
