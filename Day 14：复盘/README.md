# Day 14：复盘

## 今日目标
按照原计划完成 Day 14 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

## 固定学习节奏

| 时间 | 内容 |
|---|---|
| 09:30-11:30 | 看文档 / 看课程 / 做笔记 |
| 11:30-12:00 | 画流程图 / 总结概念 |
| 14:00-17:30 | 写代码 demo / debug |
| 20:00-21:30 | 复盘 / README / 整理项目 |

## 原始计划内容

作业：

```text
写一篇：
RAG、Tool Calling、Agent 的区别和关系。

要求结合 Superset 场景举例：
- 字段解释用什么？
- 表结构查询用什么？
- SQL 生成用什么？
- Dashboard 总结用什么？
```

产出：

```text
notes/week2_summary.md
```

## 第 3 周：手搓 Agent 框架

目标：不依赖 LangGraph / CrewAI / AutoGen，理解 Agent 底层。

资料：

- [Datawhale Hello-Agents](https://github.com/datawhalechina/hello-agents)

## 今日学习内容
- 复盘 RAG、Tool Calling、Agent 的区别。
- 用 Superset 场景解释字段含义、表结构、SQL 生成、Dashboard 总结分别用什么。
- 画出 RAG、Tool、Agent 的关系。
- 总结第 2 周对 Superset metadata assistant 的价值。
- 记录仍不清楚的问题，作为后续项目改进点。

## 学习内容详解与笔记

### RAG
RAG 负责找知识，适合字段含义、指标口径、业务文档。

### Tool Calling
Tool Calling 负责查系统状态或执行受控动作，适合 schema、chart metadata、SQL validation。

### Agent
Agent 负责目标、状态和决策，决定什么时候 RAG、什么时候 Tool、什么时候让用户确认。

### Superset 映射
字段解释用 RAG；表结构查询用 Tool；SQL 生成用 RAG + Tool + LLM；Dashboard 总结用 metadata tool + RAG。

### 今日笔记要点
- 复盘要讲关系，不只是分别定义。
- 最好画一张三者关系图。

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
- [notes/day14_week2_review.md](notes/day14_week2_review.md)

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
