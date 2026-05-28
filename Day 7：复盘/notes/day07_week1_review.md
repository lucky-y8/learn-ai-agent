# Day 7：复盘 学习笔记

## 今日学习内容
- 复盘 Agent 和普通 Chatbot 的本质区别。
- 复盘 Tool Calling 的本质和执行边界。
- 分析为什么 LLM 不应该直接执行 SQL。
- 总结 ReAct Loop 的风险和保护措施。
- 把本周知识映射到 Superset SQL Agent。

### Agent vs Chatbot
普通 Chatbot 主要生成文本；Agent 会基于目标维护状态、调用工具、观察结果并决定下一步。区别不在名字，而在是否能行动、是否有反馈闭环。

### Tool Calling 的本质
Tool Calling 不是模型真的执行函数，而是模型提出结构化调用请求，由代码执行，再把结果返回给模型。

### 为什么不能直接执行 SQL
模型可能生成 DROP、DELETE、越权查询或性能很差的 SQL。必须经过 SQL guard、权限检查、用户确认和审计。

### ReAct 风险
风险包括无限循环、工具误用、错误观察导致错误结论、提示注入、成本失控。需要 max_steps、日志、校验和人为确认。

### 今日笔记要点
- 复盘不是写感想，而是把架构判断讲清楚。
- 每个问题都要尽量结合 Superset SQL Agent 例子。

## 学习来源
- Hugging Face Agents Course Unit 1：https://huggingface.co/learn/agents-course/en/unit1/introduction
- Datawhale Hello-Agents：https://github.com/datawhalechina/hello-agents
- 学习方法：复盘 Agent、Tool Calling、ReAct，把概念落到 Mini SQL Assistant。

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
