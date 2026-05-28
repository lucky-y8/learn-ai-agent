# Day 30：SQL Validate Tool 学习笔记

## 今日学习内容
- 把 sql_guard 封装成 validate_sql 工具。
- 返回 valid、reason、normalized_sql。
- 区分安全错误、语法错误、空 SQL。
- 保证输出结构稳定，方便 Agent 和前端读取。
- 写示例测试安全和不安全 SQL。

### validate_sql
validate_sql 是工具化的 SQL 校验入口。它调用 sql_guard，并返回结构化结果。

### normalized_sql
normalized_sql 是清理格式后的 SQL，便于展示、比较和日志记录。

### valid / reason
valid 表示是否通过；reason 解释失败原因。不要只返回 true/false。

### 错误处理
语法错误、安全错误、空 SQL 要区分。

### 今日笔记要点
- validate_sql 是 Agent 调用的工具，不只是内部函数。
- 输出结构要稳定，方便前端和评估读取。

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
