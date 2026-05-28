# Day 29：SQL Guard 学习笔记

## 今日学习内容
- 学习 SQL Guard 的 allowlist 思路。
- 只允许 SELECT 和 WITH。
- 禁止 DROP、DELETE、UPDATE、INSERT、ALTER、TRUNCATE、CREATE、MERGE、CALL。
- 实现 normalize 和关键字检查。
- 返回结构化安全检查结果和 reason。

### SQL Guard
SQL Guard 是安全闸门，用来拒绝危险 SQL。

### 只允许 SELECT / WITH
BI 查询通常只需要只读语句。WITH 是 CTE，常用于复杂查询。

### 禁止语句
DROP、DELETE、UPDATE、INSERT、ALTER、TRUNCATE、CREATE、MERGE、CALL 都可能改变数据、结构或触发副作用。

### 解析策略
简单实现可以先做 normalize + 关键字检查；更稳的是使用 SQL parser。

### 今日笔记要点
- 黑名单不够，最好用 allowlist。
- Guard 要返回明确 reason。

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
