# Day 37：Mock API

## 今日目标
按照原计划完成 Day 37 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

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
实现 mock API：

POST /ai/chat
POST /ai/confirm
GET /ai/session/:id
```

接口返回：

```text
assistant message
tool calls
generated SQL
confirmation required
```

产出：

```text
projects/week6_superset_agent_mvp/mock_api/
```

## 今日学习内容
- 实现 mock API 项目结构。
- 实现 POST /ai/chat。
- 实现 POST /ai/confirm。
- 实现 GET /ai/session/:id。
- 让接口返回 assistant message、tool calls、generated SQL、confirmation required。

## 学习内容详解与笔记

### Mock API
Mock API 让前端和 Agent 流程先跑起来，不依赖真实 Superset 后端。

### POST /ai/chat
接收用户输入，返回 assistant message、tool calls、generated SQL、是否需要确认。

### POST /ai/confirm
接收用户确认或取消，确认后才执行 mock 插入。

### GET /ai/session/:id
返回会话状态、历史消息、工具调用和当前 pending action。

### 今日笔记要点
- API 返回要结构化，方便 UI 渲染。
- confirmation_required 是安全流程的关键字段。

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
