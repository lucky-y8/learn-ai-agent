# Day 10：Simple RAG Pipeline

## 今日目标
按照原计划完成 Day 10 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

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
retrieve
rerank
generate
citation
answer grounding
```

作业：

```text
实现简单 RAG：

用户问题
-> 检索 top 3 chunks
-> 模型基于 chunks 回答
-> 返回引用 source
```

产出：

```text
assignments/week2/simple_rag.py
```

## 今日学习内容
- 实现 retrieve -> rerank -> generate -> citation 的 RAG 流程。
- 检索 top 3 chunks 并打印 debug 信息。
- 让模型只基于 chunks 回答。
- 返回引用 source，避免无来源回答。
- 总结 grounding 在 BI 场景中的意义。

## 学习内容详解与笔记

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

## Hugging Face Agents Course
- 阅读范围：Unit 3 Agentic RAG。
- 重点：检索不是最终答案，检索结果要作为上下文交给 Agent 判断和生成。
- 写进作业：把 Agentic RAG 映射到 Superset metadata 检索。

## 今日作业
请按上方“原始计划内容”中的作业、要求和产出路径完成今天任务。完成后，把提交说明写到本文件夹的 `assignment.md`，方便 Codex 批改。

## 本章代码
- [code/README.md](code/README.md)

## 本章笔记
- [notes/day10_simple_rag_pipeline.md](notes/day10_simple_rag_pipeline.md)

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
