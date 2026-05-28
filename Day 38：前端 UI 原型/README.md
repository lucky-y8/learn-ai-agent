# Day 38：前端 UI 原型

## 今日目标
按照原计划完成 Day 38 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

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
- assistant drawer
- message list
- input box
- SQL code block
- tool call timeline
- confirm button
```

产出：

```text
projects/week6_superset_agent_mvp/assistant_ui_demo/
```

## 今日学习内容
- 实现前端 assistant drawer。
- 实现 message list 和 input box。
- 展示 SQL code block。
- 展示 tool call timeline。
- 实现 confirm button 和确认状态。

## 学习内容详解与笔记

### Assistant drawer
drawer 是嵌入 Superset 页面侧边的助手入口，不打断用户主流程。

### Message list
消息列表展示用户问题、助手回答和错误提示。

### Input box
输入框要支持提交、loading、禁用状态。

### SQL code block
SQL 要用代码块展示，便于复制和审查。

### Tool call timeline
timeline 展示 Agent 查了哪些工具，让过程可解释。

### Confirm button
确认按钮只在需要确认时出现，取消和确认都要有明确反馈。

## 学习来源
- Hugging Face Agents Course Unit 4 Final Project：https://huggingface.co/learn/agents-course/en/unit4/introduction
- Superset 文档入口：https://superset.apache.org/docs/intro/
- OpenAI Function Calling：https://developers.openai.com/api/docs/guides/function-calling
- LangGraph 官方文档：https://langchain-ai.github.io/langgraph/
- 学习方法：把前 5 周能力整合成 Superset AI Agent MVP，重点是能演示、能解释、能评估、能控制风险。

## Hugging Face Agents Course
- 阅读范围：Unit 4 Final Project。
- 重点：最终作品要可运行、可展示、可解释、可评估。
- 写进作业：说明你的 Superset Agent MVP 如何满足最终项目标准。

## 今日作业
请按上方“原始计划内容”中的作业、要求和产出路径完成今天任务。完成后，把提交说明写到本文件夹的 `assignment.md`，方便 Codex 批改。

## 本章代码
- [code/README.md](code/README.md)

## 本章笔记
- [notes/day38_assistant_ui_prototype.md](notes/day38_assistant_ui_prototype.md)

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
