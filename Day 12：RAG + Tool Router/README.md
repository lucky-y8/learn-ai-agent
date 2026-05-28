# Day 12：RAG + Tool Router

## 今日目标
按照原计划完成 Day 12 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

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
RAG 找知识
Tool 查实时信息
Agent 决定用哪个
```

作业：

```text
实现一个 router：

如果用户问字段含义 -> RAG
如果用户问表结构 -> Tool
如果用户问生成 SQL -> RAG + Tool
如果用户问 dashboard 总结 -> dashboard metadata tool
```

产出：

```text
assignments/week2/rag_tool_router.py
```

## 今日学习内容
- 区分 RAG 找知识和 Tool 查实时信息。
- 设计用户问题到 RAG/Tool/RAG+Tool 的路由规则。
- 实现字段含义、表结构、SQL 生成、dashboard 总结的不同路径。
- 处理 unknown 或混合意图。
- 说明 router 在 Agent 中承担的决策职责。

## 学习内容详解与笔记

### RAG 找知识
字段含义、指标口径、业务解释适合 RAG，因为这些是文档知识。

### Tool 查实时信息
表结构、当前图表配置、dashboard filters 适合 Tool，因为它们来自系统实时状态。

### Router
Router 根据 intent 和问题类型决定走 RAG、Tool 或两者组合。

### RAG + Tool
生成 SQL 常常需要两类信息：业务含义来自 RAG，真实字段和表结构来自 Tool。

### 今日笔记要点
- Router 是 Agent 的决策层。
- 不同问题要走不同信息来源，不能所有问题都塞给 RAG。

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
- [notes/day12_rag_tool_router.md](notes/day12_rag_tool_router.md)

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
