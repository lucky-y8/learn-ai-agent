# Day 17：Agent Executor

## 今日目标
按照原计划完成 Day 17 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

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
实现 ReAct executor：

while not done:
  call_model()
  parse_action()
  run_tool()
  append_observation()
```

要求：

```text
支持 max_steps
支持 final answer
支持 tool error observation
```

产出：

```text
mini_agent/executor.py
```

## 今日学习内容
- 实现 ReAct executor 的主循环。
- 实现 call_model、parse_action、run_tool、append_observation 的骨架。
- 支持 max_steps 防止无限循环。
- 支持 final answer 停止条件。
- 把 tool error 作为 observation 放回状态。

## 学习内容详解与笔记

### ReAct executor
Executor 管理循环：call_model、parse_action、run_tool、append_observation。

### max_steps
max_steps 是防止无限循环的硬限制。达到上限要返回失败原因或部分结果。

### final answer
模型必须有明确格式告诉执行器任务结束，例如 action=final 或 final_answer 字段。

### tool error observation
工具失败也要追加到 messages，让模型看到错误并调整策略。

### 今日笔记要点
- Executor 不负责业务逻辑，它负责流程推进。
- 每一步都要可日志化。

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
- [notes/day17_agent_executor.md](notes/day17_agent_executor.md)

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
