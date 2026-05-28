# Day 6：周项目 1

## 今日目标
按照原计划完成 Day 6 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

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
Mini SQL Assistant v0
```

功能：

```text
自然语言输入
-> 判断 intent
-> 获取 mock dataset schema
-> 生成 SQL
-> 校验 SQL
-> 返回 SQL 和解释
```

要求：

```text
有 README
有日志
有错误处理
最多 5 次 tool 调用
不依赖任何 Agent 框架
```

产出：

```text
projects/week1_mini_sql_assistant/
```

## 今日学习内容
- 把第 1 周的 intent、tool、SQL generation、SQL validation 串起来。
- 实现 Mini SQL Assistant v0 的完整 happy path。
- 补齐 unknown intent、tool error、SQL invalid 等错误路径。
- 写 README、日志和示例输入输出。
- 确认项目不依赖任何 Agent 框架。

## 学习内容详解与笔记

### Mini SQL Assistant v0 的闭环
本项目把 intent classifier、mock schema tool、SQL generation、validate_sql 串成一个最小助手。重点不是模型多强，而是流程是否清楚。

### 不依赖 Agent 框架
本周项目要求不用 LangGraph、CrewAI、AutoGen。你要自己写清楚每一步函数调用和状态传递。

### 错误处理
至少处理 unknown intent、dataset 不存在、SQL 校验失败、工具异常。错误返回要能被用户看懂，也能被日志记录。

### 日志
记录每次用户输入、intent、工具调用、SQL 校验结果、最终回答。日志会帮助后面做 audit 和 eval。

### README
README 要说明运行方式、示例输入输出、模块结构、限制。一个 demo 能不能被别人跑起来，README 很关键。

### 今日笔记要点
- 周项目是把零散知识变成可运行作品。
- 最小可用比功能多更重要。
- 先跑通 happy path，再补错误路径。

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
