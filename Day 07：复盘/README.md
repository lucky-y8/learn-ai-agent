# Day 7：复盘

## 今日目标
按照原计划完成 Day 7 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

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
写一篇复盘：
1. Agent 和普通 Chatbot 的区别是什么？
2. Tool Calling 的本质是什么？
3. 为什么 LLM 不应该直接执行 SQL？
4. ReAct Loop 有什么风险？
```

产出：

```text
notes/week1_summary.md
```

## 第 2 周：RAG + BI Metadata

目标：理解 Agent 如何拿外部知识，尤其是 BI 字段、数据集、图表上下文。

## 今日学习内容
- 复盘 Agent 和普通 Chatbot 的本质区别。
- 复盘 Tool Calling 的本质和执行边界。
- 分析为什么 LLM 不应该直接执行 SQL。
- 总结 ReAct Loop 的风险和保护措施。
- 把本周知识映射到 Superset SQL Agent。

## 学习内容详解与笔记

### Agent vs Chatbot
普通 Chatbot 主要生成文本；Agent 会基于目标维护状态、调用工具、观察结果并决定下一步。区别不在名字，而在是否能行动、是否有反馈闭环。

### Tool Calling 的本质
Tool Calling 不是模型真的执行函数，而是模型提出结构化调用请求，由代码执行，再把结果返回给模型。

### 为什么不能直接执行 SQL
模型可能生成 DROP、DELETE、越权查询或性能很差的 SQL。必须经过 SQL guard、权限检查、用户确认和审计。

### ReAct 风险
风险包括无限循环、工具误用、错误观察导致错误结论、提示注入、成本失控。需要 max_steps、日志、校验和人为确认。

### 今日笔记要点
- 复盘不是写感想，而是把架构判断讲清楚。
- 每个问题都要尽量结合 Superset SQL Agent 例子。

## 学习来源
- Hugging Face Agents Course Unit 1：https://huggingface.co/learn/agents-course/en/unit1/introduction
- Datawhale Hello-Agents：https://github.com/datawhalechina/hello-agents
- 学习方法：复盘 Agent、Tool Calling、ReAct，把概念落到 Mini SQL Assistant。

## Hugging Face Agents Course
- 阅读范围：Unit 1 Agent Fundamentals。
- 重点：Agent、Tool、Message、Thought、Action、Observation、ReAct。
- 写进作业：今天的实现或复盘如何体现这些概念。

## 今日作业
请按上方“原始计划内容”中的作业、要求和产出路径完成今天任务。完成后，把提交说明写到本文件夹的 `assignment.md`，方便 Codex 批改。

## 本章代码
- [code/README.md](code/README.md)

## 本章笔记
- [notes/day07_week1_review.md](notes/day07_week1_review.md)

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
