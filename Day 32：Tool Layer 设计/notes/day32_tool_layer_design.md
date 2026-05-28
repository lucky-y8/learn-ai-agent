# Day 32：Tool Layer 设计 学习笔记

## 今日学习内容
- 设计 10 个 Superset tools。
- 为每个工具写 input schema 和 output schema。
- 为每个工具标注 permission 和 risk level。
- 为每个工具设计 timeout。
- 为每个工具列出 audit log fields。

### Tool Layer
Tool Layer 是 Superset Agent 与系统能力之间的边界。

### Input / output schema
每个工具都要写清输入输出，避免模型猜参数。

### Permission
工具执行前要检查用户是否有权限访问 dataset、chart、dashboard 或执行动作。

### Risk level
读 metadata 风险低；preview_sql 中等；insert_sql_to_sqllab 或 create_chart_draft 风险更高，需要确认和审计。

### Timeout
每个工具要有超时时间，避免 Agent 卡住。

### Audit log fields
记录 user_id、session_id、tool_name、input_hash、status、error、duration_ms。

### 今日笔记要点
- 工具设计不是函数列表，而是权限和风险边界设计。

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
