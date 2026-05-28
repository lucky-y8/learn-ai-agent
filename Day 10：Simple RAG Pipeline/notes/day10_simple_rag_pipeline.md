# Day 10：Simple RAG Pipeline 学习笔记

## 今日学习内容
- 实现 retrieve -> rerank -> generate -> citation 的 RAG 流程。
- 检索 top 3 chunks 并打印 debug 信息。
- 让模型只基于 chunks 回答。
- 返回引用 source，避免无来源回答。
- 总结 grounding 在 BI 场景中的意义。

### Retrieve
retrieve 是从知识库中找相关 chunks。检索质量决定后续回答质量。

### Rerank
rerank 是对初步检索结果重新排序。简单 demo 可以先跳过，但要知道生产里常用它提高准确率。

### Generate
generate 是让模型基于 chunks 回答。提示词要明确：只能基于给定上下文，不知道就说不知道。

### Citation
citation 是引用 source。没有引用的 RAG 回答很难被信任。

### Answer grounding
grounding 是让答案扎根于检索内容，而不是模型自由发挥。

### 今日笔记要点
- RAG = 检索 + 生成 + 引用 + 约束。
- top 3 chunks 要打印出来方便 debug。

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
