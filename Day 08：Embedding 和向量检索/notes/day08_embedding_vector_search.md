# Day 8：Embedding 和向量检索 学习笔记

## 今日学习内容
- 理解 embedding 如何把文本变成向量。
- 理解 vector search 和 semantic similarity 的作用。
- 准备 20 条 BI 字段说明。
- 实现 top-k 字段语义检索。
- 返回相关字段和相似度，便于解释结果。

### Embedding
Embedding 是把文本变成向量，用来表示语义。字段说明、指标定义、图表描述都可以变成 embedding。

### Vector search
Vector search 根据向量相似度找最相关内容。用户问“收入字段是什么”，系统可以找 sales.revenue，而不是只做关键词匹配。

### Semantic similarity
语义相似度能处理“收入”“营收”“销售额”这类近义表达。BI 场景里很有用，因为业务用户和字段名常常不一致。

### Top-k retrieval
Top-k 表示返回最相关的 k 条。k 太小可能漏信息，k 太大占上下文。今天可以从 top 3 或 top 5 开始。

### 今日笔记要点
- metadata embedding search 是 BI RAG 的第一步。
- 每条字段说明要包含 dataset、column、description。
- 返回相似度是为了让结果可解释。

## 学习来源
- Hugging Face Agents Course Unit 3 Agentic RAG：https://huggingface.co/learn/agents-course/en/unit3/agentic-rag/introduction
- Datawhale Hello-Agents：https://github.com/datawhalechina/hello-agents
- Superset 文档入口：https://superset.apache.org/docs/intro/
- 学习方法：HF 学 Agentic RAG 思路，Datawhale 补中文解释，Superset 文档帮助理解 BI metadata 场景。

## Hugging Face 对应内容
- 阅读范围：Unit 3 Agentic RAG。
- 重点：检索不是最终答案，检索结果要作为上下文交给 Agent 判断和生成。
- 写进作业：把 Agentic RAG 映射到 Superset metadata 检索。

## 我的理解
- 

## 今日疑问
- 

## 今日小结
- 
