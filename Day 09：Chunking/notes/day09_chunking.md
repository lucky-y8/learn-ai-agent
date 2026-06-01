# Day 9：Chunking 学习笔记

## 今日学习内容
- 理解 chunk size、chunk overlap 对检索质量的影响。
- 把业务说明文档切成可检索 chunks。
- 给每个 chunk 增加 source、section 等 metadata。
- 保留 source tracking，方便 RAG 回答引用。
- 检查 chunk 是否能独立表达一个知识点。

### Chunk size
chunk size 是每个片段的长度。太短会丢上下文，太长会降低检索精度并浪费 token。

### Chunk overlap
overlap 是相邻 chunk 的重复部分，用来避免句子或段落被切断。业务说明文档通常需要少量 overlap。

### Metadata
每个 chunk 要带 source、section、title 等 metadata。没有 metadata，后续无法引用来源。

### Source tracking
RAG 回答要能告诉用户来自哪个文档、哪个章节。BI 场景中这能提高可信度。

### 今日笔记要点
- chunk 不只是文本切片，还要保留来源。
- 好的 chunk 应该能独立表达一个小知识点。

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
