# Day 35：复盘 学习笔记

## 今日学习内容
- 复盘 Safety、Audit、Eval 为什么是生产 Agent 必备能力。
- 结合 Superset 权限说明安全边界。
- 结合 SQL 安全说明只读和确认机制。
- 结合数据泄露说明上下文控制。
- 结合日志审计说明可追踪性。

### Safety
Safety 负责防止危险 SQL、越权访问、数据泄露和副作用动作。

### Audit
Audit 负责事后追踪和合规，能还原 Agent 行为。

### Eval
Eval 负责持续检查质量，避免改代码后能力退化。

### Superset 场景
Superset 涉及真实业务数据、权限边界、仪表盘共享和 SQL 执行，所以生产 Agent 必须比普通聊天更谨慎。

### 今日笔记要点
- 复盘要结合权限、SQL 安全、数据泄露、用户确认、日志审计。

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
