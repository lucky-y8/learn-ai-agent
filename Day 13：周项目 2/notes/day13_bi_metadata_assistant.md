# Day 13：周项目 2 学习笔记

## 今日学习内容
- 把 BI metadata 检索、schema tool、SQL 草稿生成串成项目。
- 让用户用业务语言提问。
- 检索相关字段并解释选择原因。
- 获取数据集 schema 并推荐 SQL 字段。
- 输出 SQL 草稿而不是直接执行 SQL。

### BI Metadata Assistant
这个项目目标是把业务问题变成字段推荐和 SQL 草稿。

### 业务问题理解
用户通常说“收入趋势”“销售表现”，系统要映射到字段、指标和数据集。

### 字段检索
先用 RAG 找相关字段说明，再用工具确认 schema。

### SQL 草稿
草稿不等于最终执行 SQL，仍要经过校验和用户确认。

### 今日笔记要点
- Metadata Assistant 是 Superset Agent 的上下文层雏形。
- 返回结果要解释为什么选择这些字段。

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
