# Day 28：复盘

## 今日目标
按照原计划完成 Day 28 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

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
画一张 DAG 图：
Superset SQL Agent Workflow

写清楚：
1. 每个 node 的职责
2. 每条 edge 的条件
3. state 里保存什么
4. 哪些地方需要 human confirmation
```

产出：

```text
notes/week4_summary.md
```

## 第 5 周：SQL Safety + Agent 工程化

目标：从 demo 走向生产思维。

## 今日学习内容
- 画 Superset SQL Agent Workflow DAG。
- 写清每个 node 的职责。
- 写清每条 edge 的条件。
- 写清 state 里保存的字段。
- 标出哪些地方需要 human confirmation。

## 学习内容详解与笔记

### DAG 图
DAG 图用来表达节点和边，帮助别人理解 Agent 工作流。

### Node 职责
每个 node 要写清输入、处理、输出。

### Edge 条件
边不是线条而已，要写清什么时候走这条边。

### State 内容
state 是节点之间传递信息的合同，必须列出关键字段。

### Human confirmation
标出哪些节点前后需要用户确认，例如 SQL 插入、执行、创建图表。

### 今日笔记要点
- 复盘要能让别人照图复现流程。

## 学习来源
- LangGraph 官方文档：https://langchain-ai.github.io/langgraph/
- Hugging Face Agents Course Unit 2.3 LangGraph：https://huggingface.co/learn/agents-course/en/unit2/langgraph/introduction
- 学习方法：HF 先看图工作流的概念，LangGraph 官方文档看 StateGraph、node、edge、checkpoint 的实现。

## Hugging Face Agents Course
- 阅读范围：Unit 2.3 LangGraph。
- 重点：StateGraph、节点、边、条件路由、checkpoint、human-in-the-loop。
- 写进作业：对比你的图工作流和课程中的 graph building blocks。

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
