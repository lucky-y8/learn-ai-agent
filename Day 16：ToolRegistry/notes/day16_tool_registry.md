# Day 16：ToolRegistry 学习笔记

## 今日学习内容
- 把 ToolRegistry 抽象成 mini_agent 的核心模块。
- 实现 register_tool、get_tool、list_tools、run_tool、get_tool_schemas。
- 处理工具不存在和参数错误。
- 记录工具执行耗时。
- 为 executor 提供统一工具执行接口。

### register_tool
注册工具时保存名称、描述、schema、函数和风险等级。

### get_tool / list_tools
查询工具用于执行器和模型提示词构造。list_tools 应该返回可读摘要。

### run_tool
run_tool 是统一执行入口，负责参数校验、计时、异常捕获、结果封装。

### get_tool_schemas
模型只需要 schema 和描述，不应该看到内部函数实现。

### 今日笔记要点
- ToolRegistry 是手搓 Agent 的工具层。
- 耗时记录对后续 observability 很重要。

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
