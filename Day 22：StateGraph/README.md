# Day 22：StateGraph

## 今日目标
按照原计划完成 Day 22 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

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
实现：

start -> classify_intent -> final_response
```

产出：

```text
assignments/week4/basic_state_graph.py
```

## 今日学习内容
- 学习 LangGraph StateGraph 的基本概念。
- 实现 start -> classify_intent -> final_response。
- 定义 state 中保存哪些字段。
- 理解 node 如何读取 state 并返回更新。
- 理解 edge 如何控制节点流转。

## 学习内容详解与笔记

### StateGraph
StateGraph 用状态驱动工作流。每个节点读取 state，返回 state 的增量更新。

### Node
Node 是一个函数，负责一个明确职责，例如 classify_intent 或 final_response。

### Edge
Edge 定义节点之间怎么流转。最简单是固定边：start -> classify -> final。

### State
State 保存 workflow 需要共享的信息，例如 user_input、intent、messages、answer。

### 今日笔记要点
- LangGraph 的核心不是“聊天”，而是状态图。
- 节点要小而清楚。

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

## 本章代码
- [code/README.md](code/README.md)

## 本章笔记
- [notes/day22_state_graph.md](notes/day22_state_graph.md)

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
