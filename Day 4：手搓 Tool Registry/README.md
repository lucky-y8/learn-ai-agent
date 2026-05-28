# Day 4：手搓 Tool Registry

## 今日目标
按照原计划完成 Day 4 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

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
工具注册
工具查找
工具参数校验
工具执行错误处理
```

作业：

```text
实现 ToolRegistry：

register_tool()
list_tools()
get_tool_schema()
run_tool()
```

要求：

```text
工具不存在时返回结构化错误
参数错误时返回结构化错误
工具执行要有日志
```

产出：

```text
assignments/week1/tool_registry.py
```

## 今日学习内容
- 学习 ToolRegistry 为什么是 Agent 工具层核心。
- 实现工具注册、工具查找、schema 获取和统一执行入口。
- 给工具执行增加参数校验和结构化错误。
- 给工具执行增加日志和耗时记录。
- 为后续 ReAct Agent 准备可复用工具层。

## 学习内容详解与笔记

### 工具注册
ToolRegistry 是工具中心。它保存工具名、描述、参数 schema、执行函数。Agent 不应该到处硬编码工具函数。

### 工具查找
工具查找要能根据名称拿到 schema 或执行函数。如果工具不存在，要返回结构化错误，而不是直接崩溃。

### 参数校验
执行工具前先校验参数。常见错误包括缺少必填字段、类型不对、多余字段、空字符串。

### 执行错误处理
工具执行可能失败，例如 dataset 不存在、SQL 非法、超时。错误要包含 tool_name、error_type、message，方便日志和模型观察。

### 执行日志
日志至少记录 tool_name、input、status、duration_ms、error。生产环境还要加 user_id、session_id、risk_level。

### 今日笔记要点
- ToolRegistry 是后续 Agent 框架的核心模块。
- 工具不存在和参数错误是两类不同错误。
- 执行器永远不要吞掉错误，要把错误变成可观察结果。

## 学习来源
- Hugging Face Agents Course Unit 1：https://huggingface.co/learn/agents-course/en/unit1/introduction
- OpenAI Function Calling：https://developers.openai.com/api/docs/guides/function-calling
- Datawhale Hello-Agents：https://github.com/datawhalechina/hello-agents
- 学习方法：参考工具调用概念，自己实现 ToolRegistry，不急着用框架。

## Hugging Face Agents Course
- 阅读范围：Unit 1 Agent Fundamentals。
- 重点：Agent、Tool、Message、Thought、Action、Observation、ReAct。
- 写进作业：今天的实现或复盘如何体现这些概念。

## 今日作业
请按上方“原始计划内容”中的作业、要求和产出路径完成今天任务。完成后，把提交说明写到本文件夹的 `assignment.md`，方便 Codex 批改。

## 本章代码
- [code/README.md](code/README.md)

## 本章笔记
- [notes/day04_tool_registry.md](notes/day04_tool_registry.md)

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
