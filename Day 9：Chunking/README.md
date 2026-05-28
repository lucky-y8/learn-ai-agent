# Day 9：Chunking

## 今日目标
按照原计划完成 Day 9 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

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
chunk size
chunk overlap
metadata
source tracking
```

作业：

```text
把一份业务说明文档切成 chunks。

每个 chunk 包含：
{
  "text": "...",
  "source": "business_doc.md",
  "section": "sales"
}
```

产出：

```text
assignments/week2/chunking_demo.py
```

## 今日学习内容
- 理解 chunk size、chunk overlap 对检索质量的影响。
- 把业务说明文档切成可检索 chunks。
- 给每个 chunk 增加 source、section 等 metadata。
- 保留 source tracking，方便 RAG 回答引用。
- 检查 chunk 是否能独立表达一个知识点。

## 学习内容详解与笔记

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

## Hugging Face Agents Course
- 阅读范围：Unit 3 Agentic RAG。
- 重点：检索不是最终答案，检索结果要作为上下文交给 Agent 判断和生成。
- 写进作业：把 Agentic RAG 映射到 Superset metadata 检索。

## 今日作业
请按上方“原始计划内容”中的作业、要求和产出路径完成今天任务。完成后，把提交说明写到本文件夹的 `assignment.md`，方便 Codex 批改。

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
