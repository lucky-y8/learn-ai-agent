# Day 20：周项目 3

## 今日目标
按照原计划完成 Day 20 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

## 固定学习节奏

| 时间 | 内容 |
|---|---|
| 09:30-11:30 | 看文档 / 看课程 / 做笔记 |
| 11:30-12:00 | 画流程图 / 总结概念 |
| 14:00-17:30 | 写代码 demo / debug |
| 20:00-21:30 | 复盘 / README / 整理项目 |

## 原始计划内容

项目：

```text
Handmade SQL Agent
```

要求：

```text
不用 LangGraph
不用 CrewAI
不用 AutoGen
不用 Microsoft Agent Framework

自己实现：
ToolRegistry
Memory
Executor
Planner
SQL tools
```

产出：

```text
projects/week3_handmade_sql_agent/
```

## 今日学习内容
- 整合 ToolRegistry、Memory、Executor、Planner、SQL tools。
- 实现 Handmade SQL Agent 项目。
- 保持不使用 LangGraph、CrewAI、AutoGen、Microsoft Agent Framework。
- 写清项目结构和运行方式。
- 用示例展示手搓 Agent 的完整执行流程。

## 学习内容详解与笔记

### Handmade SQL Agent
这是一个完整手搓 Agent：ToolRegistry、Memory、Executor、Planner、SQL tools 都要能协作。

### 不用框架的意义
不用框架是为了理解底层模块边界。之后用 LangGraph 才知道它帮你省了什么。

### SQL tools
至少包含 schema 查询、SQL 生成辅助、SQL guard、validate_sql。

### 项目结构
建议把 mini_agent 框架代码和 SQL assistant 业务代码分开。

### 今日笔记要点
- 重点是模块边界清楚，不是代码量大。
- README 要画出执行流程。

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

## 本章代码
- [code/README.md](code/README.md)

## 本章笔记
- [notes/day20_handmade_sql_agent.md](notes/day20_handmade_sql_agent.md)

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
