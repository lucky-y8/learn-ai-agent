# Day 42：总复盘 学习笔记

## 今日学习内容
- 完成总复盘和答辩问题。
- 解释为什么用 DAG + ReAct。
- 解释为什么不能让模型直接执行 SQL。
- 说明 Superset 上下文、权限、SQL 安全和评估方案。
- 说明如果换模型 provider，架构哪些地方需要改。

### DAG + ReAct
DAG 让流程可控，ReAct 让局部步骤能根据观察调整。两者结合适合生产 Agent。

### 不直接执行 SQL
模型输出必须经过 SQL guard、权限检查和用户确认，避免破坏数据或泄露信息。

### Superset 上下文
上下文来自 dashboard、chart、dataset、filters、SQL Lab、用户权限和业务 metadata。

### 权限保证
每次工具调用都要带 user/session，并检查资源权限。

### SQL 安全
只允许 SELECT/WITH，禁止危险语句，执行前校验，必要时 parser 解析。

### Agent 评估
用 eval cases 检查安全、字段、工具调用、确认流程、引用和回答质量。

### Provider 可替换
换百炼、DeepSeek、豆包时，主要改 ModelClient 配置；Tool Layer、State、Safety、Eval 不应该大改。

## 学习来源
- Hugging Face Agents Course Unit 4 Final Project：https://huggingface.co/learn/agents-course/en/unit4/introduction
- Superset 文档入口：https://superset.apache.org/docs/intro/
- OpenAI Function Calling：https://developers.openai.com/api/docs/guides/function-calling
- LangGraph 官方文档：https://langchain-ai.github.io/langgraph/
- 学习方法：把前 5 周能力整合成 Superset AI Agent MVP，重点是能演示、能解释、能评估、能控制风险。

## Hugging Face 对应内容
- 阅读范围：Unit 4 Final Project。
- 重点：最终作品要可运行、可展示、可解释、可评估。
- 写进作业：说明你的 Superset Agent MVP 如何满足最终项目标准。

## 我的理解
- 

## 今日疑问
- 

## 今日小结
- 
