# Day 27：周项目 4

## 今日目标
按照原计划完成 Day 27 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

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
LangGraph SQL Agent
```

流程：

```text
User
-> classify_intent
-> build_context
-> get_schema
-> generate_sql
-> sql_guard
-> wait_confirm
-> final_response
```

产出：

```text
projects/week4_langgraph_sql_agent/
```

## 今日学习内容
- 实现 LangGraph SQL Agent 项目。
- 搭建 classify_intent、build_context、get_schema、generate_sql、sql_guard、wait_confirm、final_response 节点。
- 明确每个节点输入输出。
- 把 SQL guard 放在确认之前。
- 输出可演示的完整 workflow。

## 学习内容详解与笔记

### LangGraph SQL Agent
流程是 User -> classify_intent -> build_context -> get_schema -> generate_sql -> sql_guard -> wait_confirm -> final_response。

### build_context
上下文来自页面、dataset、dashboard、RAG 检索和用户输入。

### sql_guard
SQL guard 必须在 wait_confirm 之前执行。用户不应该确认一段危险 SQL。

### final_response
最终回答包含 SQL、解释、使用字段、风险提示和下一步操作。

### 今日笔记要点
- 图工作流要表达安全边界。
- 每个节点只做一件事。

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
