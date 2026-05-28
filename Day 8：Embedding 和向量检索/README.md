# Day 8：Embedding 和向量检索

## 今日目标
按照原计划完成 Day 8 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

## 固定学习节奏

| 时间 | 内容 |
|---|---|
| 09:30-11:30 | 看文档 / 看课程 / 做笔记 |
| 11:30-12:00 | 画流程图 / 总结概念 |
| 14:00-17:30 | 写代码 demo / debug |
| 20:00-21:30 | 复盘 / README / 整理项目 |

## 原始计划内容

学习内容：

```text
Embedding
Vector search
Semantic similarity
Top-k retrieval
```

作业：

```text
准备 20 条字段说明：

sales.revenue: 销售额
sales.ds: 日期
sales.region: 地区
sales.quantity: 销售数量
```

实现：

```text
用户问："哪个字段表示收入？"
系统返回最相关字段和相似度。
```

产出：

```text
assignments/week2/metadata_embedding_search.py
```

## 今日学习内容
- 理解 embedding 如何把文本变成向量。
- 理解 vector search 和 semantic similarity 的作用。
- 准备 20 条 BI 字段说明。
- 实现 top-k 字段语义检索。
- 返回相关字段和相似度，便于解释结果。

## 学习内容详解与笔记

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

## Hugging Face Agents Course
- 阅读范围：Unit 3 Agentic RAG。
- 重点：检索不是最终答案，检索结果要作为上下文交给 Agent 判断和生成。
- 写进作业：把 Agentic RAG 映射到 Superset metadata 检索。

## 今日作业
请按上方“原始计划内容”中的作业、要求和产出路径完成今天任务。完成后，把提交说明写到本文件夹的 `assignment.md`，方便 Codex 批改。

## 本章代码
- [code/README.md](code/README.md)

## 本章笔记
- [notes/day08_embedding_vector_search.md](notes/day08_embedding_vector_search.md)

## 完成标准
- 完成原计划中列出的代码、文档或项目产出。
- 能用自己的话解释今天的核心概念。
- 在 `assignment.md` 中填写完成内容、运行方式、自测结果和疑问。
- 代码类作业至少提供一个可运行示例或自测说明。
- 文档类作业要结合 BI / Superset / SQL Agent 主线。

## 给 Codex 批改时重点看
- 是否满足当天作业的全部要求。
- 产出路径是否和计划一致。
- 代码是否能运行，错误处理是否清楚。
- 解释是否准确，是否贴合 Superset 场景。
