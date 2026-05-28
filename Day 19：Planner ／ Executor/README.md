# Day 19：Planner ／ Executor

## 今日目标
按照原计划完成 Day 19 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

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
实现 Planner：

用户任务 -> steps[]

实现 StepExecutor：

steps[] -> 逐步执行
失败 -> 返回 failed step 和 reason
```

产出：

```text
mini_agent/planner.py
```

## 今日学习内容
- 实现 Planner，把用户任务拆成 steps。
- 实现 StepExecutor，逐步执行 steps。
- 设计 step 的状态：pending、running、done、failed。
- 失败时返回 failed step 和 reason。
- 理解 Planner 和 Executor 的职责边界。

## 学习内容详解与笔记

### Planner
Planner 把用户任务拆成 steps。比如“生成月销售趋势 SQL”可以拆成识别数据集、获取字段、生成 SQL、校验 SQL、返回解释。

### StepExecutor
StepExecutor 逐步执行 steps，并记录每一步状态。

### 失败处理
失败时要返回 failed_step 和 reason，而不是只说“失败了”。这样用户和开发者能定位问题。

### 计划粒度
步骤太粗无法恢复，太细会增加复杂度。今天用 3-6 步即可。

### 今日笔记要点
- Planner 负责“做什么”，Executor 负责“怎么推进”。
- 计划要能被机器执行，而不是写成空泛自然语言。

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
- [notes/day19_planner_executor.md](notes/day19_planner_executor.md)

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
