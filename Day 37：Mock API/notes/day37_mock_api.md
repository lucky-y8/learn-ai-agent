# Day 37：Mock API 学习笔记

## 今日学习内容
- 实现 mock API 项目结构。
- 实现 POST /ai/chat。
- 实现 POST /ai/confirm。
- 实现 GET /ai/session/:id。
- 让接口返回 assistant message、tool calls、generated SQL、confirmation required。

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

## Hugging Face 对应内容
- 阅读范围：Unit 4 Final Project。
- 重点：最终作品要可运行、可展示、可解释、可评估。
- 写进作业：说明你的 Superset Agent MVP 如何满足最终项目标准。

## 我的理解
- 

## 今日疑问
- 

## 今日小结
- 
