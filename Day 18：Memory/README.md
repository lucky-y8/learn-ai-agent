# Day 18：Memory

## 今日目标
按照原计划完成 Day 18 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

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
实现 SessionMemory：

add_message()
add_tool_result()
get_recent_messages()
summarize_if_too_long()
```

产出：

```text
mini_agent/memory.py
```

## 今日学习内容
- 实现 SessionMemory 保存会话消息。
- 保存工具结果，让后续推理能看到 observation。
- 实现 get_recent_messages 控制上下文长度。
- 实现 summarize_if_too_long 的简化版本。
- 理解记忆不是无限拼接，而是面向任务保留关键信息。

## 学习内容详解与笔记

### SessionMemory
SessionMemory 管理一个会话里的消息、工具结果和摘要。

### add_message
保存用户、助手和系统消息。需要保留顺序。

### add_tool_result
工具结果是 Agent 记忆的一部分，后续推理要能看到。

### get_recent_messages
上下文窗口有限，所以只取最近消息或关键消息。

### summarize_if_too_long
历史太长时做摘要，保留任务目标、关键约束、已完成步骤和未解决问题。

### 今日笔记要点
- Memory 不是把所有内容无限拼接。
- 摘要要服务任务，不是普通聊天总结。

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
- [notes/day18_memory.md](notes/day18_memory.md)

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
