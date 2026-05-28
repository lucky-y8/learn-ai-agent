# Day 16：ToolRegistry

## 今日目标
按照原计划完成 Day 16 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

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

register_tool()
get_tool()
list_tools()
run_tool()
get_tool_schemas()
```

要求：

```text
工具不存在时返回明确错误
工具参数错误时返回结构化错误
工具执行需要记录耗时
```

产出：

```text
mini_agent/tool_registry.py
```

## 今日学习内容
- 把 ToolRegistry 抽象成 mini_agent 的核心模块。
- 实现 register_tool、get_tool、list_tools、run_tool、get_tool_schemas。
- 处理工具不存在和参数错误。
- 记录工具执行耗时。
- 为 executor 提供统一工具执行接口。

## 学习内容详解与笔记

### register_tool
注册工具时保存名称、描述、schema、函数和风险等级。

### get_tool / list_tools
查询工具用于执行器和模型提示词构造。list_tools 应该返回可读摘要。

### run_tool
run_tool 是统一执行入口，负责参数校验、计时、异常捕获、结果封装。

### get_tool_schemas
模型只需要 schema 和描述，不应该看到内部函数实现。

### 今日笔记要点
- ToolRegistry 是手搓 Agent 的工具层。
- 耗时记录对后续 observability 很重要。

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
