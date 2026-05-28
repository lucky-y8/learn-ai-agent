# Day 21：复盘

## 今日目标
按照原计划完成 Day 21 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

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
如果不用任何框架，Agent 框架最少需要哪些模块？

必须覆盖：
Model Client
Tool Registry
Executor
Memory
Planner
Policy Guard
Logger
```

产出：

```text
notes/week3_summary.md
```

## 第 4 周：LangGraph / DAG

目标：掌握生产级 Agent 工作流。LangGraph 是主线框架。

资料：

- [LangGraph Docs](https://langchain-ai.github.io/langgraph/)

## 今日学习内容
- 复盘不用框架时 Agent 至少需要哪些模块。
- 解释 Model Client、Tool Registry、Executor、Memory、Planner 的职责。
- 补充 Policy Guard 和 Logger 在生产中的必要性。
- 把这些模块映射到 Handmade SQL Agent。
- 形成一篇可作为后续架构说明的总结。

## 学习内容详解与笔记

### Model Client
封装 provider 差异，统一 call_model 接口。

### Tool Registry
统一管理工具 schema 和执行。

### Executor
推进 ReAct 或 plan-execute 循环。

### Memory
保存消息、工具结果、摘要和关键状态。

### Planner
把复杂任务拆成步骤。

### Policy Guard
检查权限、SQL 安全、风险动作和用户确认。

### Logger
记录输入、输出、工具调用、错误和耗时。

### 今日笔记要点
- 复盘要回答“最少需要哪些模块以及为什么”。

## 学习来源
- Datawhale Hello-Agents：https://github.com/datawhalechina/hello-agents
- Hugging Face Agents Course Unit 1：https://huggingface.co/learn/agents-course/en/unit1/introduction
- Hugging Face Agents Course：https://huggingface.co/learn/agents-course/en
- 学习方法：Datawhale 作为中文主线，HF 作为概念校准，目标是手搓 Message/State/Tool/Executor/Memory/Planner。

## Hugging Face Agents Course
- 阅读范围：Unit 1 复习 + Unit 2 框架概览。
- 重点：框架解决的是状态、工具、执行循环、记忆和编排问题。
- 写进作业：说明你手搓的模块对应哪个 Agent 概念。

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
