# Day 33：权限 ／ 审计 学习笔记

## 今日学习内容
- 设计 audit log schema。
- 理解 user_id、session_id、tool_name、input_hash 的作用。
- 记录 risk_level、timestamp、status、error。
- 记录 model_provider 和 token_usage。
- 思考敏感信息脱敏和可追踪性之间的平衡。

### Audit log
Audit log 记录 Agent 做过什么、谁触发的、用了什么工具、结果如何。

### input_hash
不要直接记录敏感输入全文，可以记录 hash，必要字段脱敏。

### risk_level
risk_level 帮助筛选高风险行为，例如 SQL 写入、图表创建、跨 dataset 访问。

### token_usage
token_usage 用于成本分析和异常检测。

### status / error
每次工具调用都要知道成功或失败，失败原因是什么。

### 今日笔记要点
- 审计是生产 Agent 的底线。
- 日志要能回答“谁在什么时候让 Agent 做了什么”。

## 学习来源
- OpenAI Function Calling / tools 设计：https://developers.openai.com/api/docs/guides/function-calling
- Hugging Face Bonus Unit 2 Observability and Evaluation：https://huggingface.co/learn/agents-course/en/bonus-unit2/introduction
- Superset 文档入口：https://superset.apache.org/docs/intro/
- 学习方法：结合 Superset 的权限和 SQL 使用场景，设计 SQL guard、context builder、tool layer、audit log。

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
