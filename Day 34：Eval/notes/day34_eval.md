# Day 34：Eval 学习笔记

## 今日学习内容
- 学习 Agent eval 的基本思路。
- 写 20 条 SQL Agent 测试 case。
- 为每条 case 写输入和期望。
- 覆盖 SQL 安全、字段正确、工具调用、用户确认、上下文引用。
- 思考如何用 LangSmith 或 Promptfoo 自动化检查。

### Eval case
Eval case 包含输入、期望行为、检查规则和评分维度。

### SQL 安全
检查是否只生成 SELECT/WITH，不能包含危险语句。

### 字段正确
检查是否使用 revenue、ds、region 等正确字段。

### 工具调用正确
生成 SQL 前应该查 schema 或 metadata，不能凭空编字段。

### 用户确认
高风险动作前必须需要确认。

### 上下文引用
回答应该说明依据来自哪个 dataset、chart 或文档。

### 今日笔记要点
- Eval 是把“感觉不错”变成可检查标准。
- 20 条 case 要覆盖正常、边界和恶意输入。

## 学习来源
- Hugging Face Bonus Unit 2 Observability and Evaluation：https://huggingface.co/learn/agents-course/en/bonus-unit2/introduction
- LangSmith Evaluation Concepts：https://docs.langchain.com/langsmith/evaluation-concepts
- Promptfoo Eval Guides：https://www.promptfoo.dev/docs/guides/
- 学习方法：把 eval case 写成可检查的输入、期望、评分维度，关注 SQL 安全、字段正确性、工具调用和用户确认。

## Hugging Face 对应内容
- 阅读范围：Bonus Unit 2 Observability and Evaluation。
- 重点：trace、tool usage、latency、token usage、用户反馈、评估集。
- 写进作业：说明 Safety / Audit / Eval 如何让 Agent 可控。

## 我的理解
- 

## 今日疑问
- 

## 今日小结
- 
