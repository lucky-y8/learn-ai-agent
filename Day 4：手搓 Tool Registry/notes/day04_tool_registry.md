# Day 4：手搓 Tool Registry 学习笔记

## 今日学习内容
- 学习 ToolRegistry 为什么是 Agent 工具层核心。
- 实现工具注册、工具查找、schema 获取和统一执行入口。
- 给工具执行增加参数校验和结构化错误。
- 给工具执行增加日志和耗时记录。
- 为后续 ReAct Agent 准备可复用工具层。

### 工具注册
ToolRegistry 是工具中心。它保存工具名、描述、参数 schema、执行函数。Agent 不应该到处硬编码工具函数。

### 工具查找
工具查找要能根据名称拿到 schema 或执行函数。如果工具不存在，要返回结构化错误，而不是直接崩溃。

### 参数校验
执行工具前先校验参数。常见错误包括缺少必填字段、类型不对、多余字段、空字符串。

### 执行错误处理
工具执行可能失败，例如 dataset 不存在、SQL 非法、超时。错误要包含 tool_name、error_type、message，方便日志和模型观察。

### 执行日志
日志至少记录 tool_name、input、status、duration_ms、error。生产环境还要加 user_id、session_id、risk_level。

### 今日笔记要点
- ToolRegistry 是后续 Agent 框架的核心模块。
- 工具不存在和参数错误是两类不同错误。
- 执行器永远不要吞掉错误，要把错误变成可观察结果。

## 学习来源
- Hugging Face Agents Course Unit 1：https://huggingface.co/learn/agents-course/en/unit1/introduction
- OpenAI Function Calling：https://developers.openai.com/api/docs/guides/function-calling
- Datawhale Hello-Agents：https://github.com/datawhalechina/hello-agents
- 学习方法：参考工具调用概念，自己实现 ToolRegistry，不急着用框架。

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
