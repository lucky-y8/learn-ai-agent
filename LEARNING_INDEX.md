# AI Agent 42 天学习目录

每天一个文件夹，命名格式与现有文件夹保持一致：`Day NN：标题`。

每个文件夹包含：
- `README.md`：当天学习规划、原始任务、产出和验收标准。
- `assignment.md`：当天作业提交与 Codex 批改入口。

## 主要学习来源
- Agent 基础：https://huggingface.co/learn/agents-course/en
- OpenAI-compatible API / Chat / Prompt：https://developers.openai.com/api/docs/quickstart
- 结构化输出：https://developers.openai.com/api/docs/guides/structured-outputs
- Tool Calling：https://developers.openai.com/api/docs/guides/function-calling
- 中文手搓 Agent：https://github.com/datawhalechina/hello-agents
- LangGraph：https://langchain-ai.github.io/langgraph/
- Superset 场景：https://superset.apache.org/docs/intro/
- 评估：https://docs.langchain.com/langsmith/evaluation-concepts 和 https://www.promptfoo.dev/docs/guides/

## Hugging Face Agents Course
- 课程首页：https://huggingface.co/learn/agents-course/en
- Day 1-7：Unit 1 Agent Fundamentals
- Day 8-14：Unit 3 Agentic RAG
- Day 15-21：Unit 1/2，对照手搓 Agent 和框架封装
- Day 22-28：Unit 2.3 LangGraph
- Day 29-35：Bonus Unit 2 Observability and Evaluation
- Day 36-42：Unit 4 Final Project

- [Day 01：LLM API 和 Prompt 基础](Day 01：LLM API 和 Prompt 基础/README.md) | [作业](Day 01：LLM API 和 Prompt 基础/assignment.md)
- [Day 02：Structured Output](Day 02：Structured Output/README.md) | [作业](Day 02：Structured Output/assignment.md)
- [Day 03：Tool Calling](Day 03：Tool Calling/README.md) | [作业](Day 03：Tool Calling/assignment.md)
- [Day 04：手搓 Tool Registry](Day 04：手搓 Tool Registry/README.md) | [作业](Day 04：手搓 Tool Registry/assignment.md)
- [Day 05：ReAct Loop](Day 05：ReAct Loop/README.md) | [作业](Day 05：ReAct Loop/assignment.md)
- [Day 06：周项目 1](Day 06：周项目 1/README.md) | [作业](Day 06：周项目 1/assignment.md)
- [Day 07：复盘](Day 07：复盘/README.md) | [作业](Day 07：复盘/assignment.md)
- [Day 08：Embedding 和向量检索](Day 08：Embedding 和向量检索/README.md) | [作业](Day 08：Embedding 和向量检索/assignment.md)
- [Day 09：Chunking](Day 09：Chunking/README.md) | [作业](Day 09：Chunking/assignment.md)
- [Day 10：Simple RAG Pipeline](Day 10：Simple RAG Pipeline/README.md) | [作业](Day 10：Simple RAG Pipeline/assignment.md)
- [Day 11：BI Metadata RAG](Day 11：BI Metadata RAG/README.md) | [作业](Day 11：BI Metadata RAG/assignment.md)
- [Day 12：RAG + Tool Router](Day 12：RAG + Tool Router/README.md) | [作业](Day 12：RAG + Tool Router/assignment.md)
- [Day 13：周项目 2](Day 13：周项目 2/README.md) | [作业](Day 13：周项目 2/assignment.md)
- [Day 14：复盘](Day 14：复盘/README.md) | [作业](Day 14：复盘/assignment.md)
- [Day 15：Runtime 设计](Day 15：Runtime 设计/README.md) | [作业](Day 15：Runtime 设计/assignment.md)
- [Day 16：ToolRegistry](Day 16：ToolRegistry/README.md) | [作业](Day 16：ToolRegistry/assignment.md)
- [Day 17：Agent Executor](Day 17：Agent Executor/README.md) | [作业](Day 17：Agent Executor/assignment.md)
- [Day 18：Memory](Day 18：Memory/README.md) | [作业](Day 18：Memory/assignment.md)
- [Day 19：Planner ／ Executor](Day 19：Planner ／ Executor/README.md) | [作业](Day 19：Planner ／ Executor/assignment.md)
- [Day 20：周项目 3](Day 20：周项目 3/README.md) | [作业](Day 20：周项目 3/assignment.md)
- [Day 21：复盘](Day 21：复盘/README.md) | [作业](Day 21：复盘/assignment.md)
- [Day 22：StateGraph](Day 22：StateGraph/README.md) | [作业](Day 22：StateGraph/assignment.md)
- [Day 23：条件路由](Day 23：条件路由/README.md) | [作业](Day 23：条件路由/assignment.md)
- [Day 24：Tool Node](Day 24：Tool Node/README.md) | [作业](Day 24：Tool Node/assignment.md)
- [Day 25：Human-in-the-loop](Day 25：Human-in-the-loop/README.md) | [作业](Day 25：Human-in-the-loop/assignment.md)
- [Day 26：Checkpoint ／ Resume](Day 26：Checkpoint ／ Resume/README.md) | [作业](Day 26：Checkpoint ／ Resume/assignment.md)
- [Day 27：周项目 4](Day 27：周项目 4/README.md) | [作业](Day 27：周项目 4/assignment.md)
- [Day 28：复盘](Day 28：复盘/README.md) | [作业](Day 28：复盘/assignment.md)
- [Day 29：SQL Guard](Day 29：SQL Guard/README.md) | [作业](Day 29：SQL Guard/assignment.md)
- [Day 30：SQL Validate Tool](Day 30：SQL Validate Tool/README.md) | [作业](Day 30：SQL Validate Tool/assignment.md)
- [Day 31：Context Builder](Day 31：Context Builder/README.md) | [作业](Day 31：Context Builder/assignment.md)
- [Day 32：Tool Layer 设计](Day 32：Tool Layer 设计/README.md) | [作业](Day 32：Tool Layer 设计/assignment.md)
- [Day 33：权限 ／ 审计](Day 33：权限 ／ 审计/README.md) | [作业](Day 33：权限 ／ 审计/assignment.md)
- [Day 34：Eval](Day 34：Eval/README.md) | [作业](Day 34：Eval/assignment.md)
- [Day 35：复盘](Day 35：复盘/README.md) | [作业](Day 35：复盘/assignment.md)
- [Day 36：MVP 范围](Day 36：MVP 范围/README.md) | [作业](Day 36：MVP 范围/assignment.md)
- [Day 37：Mock API](Day 37：Mock API/README.md) | [作业](Day 37：Mock API/assignment.md)
- [Day 38：前端 UI 原型](Day 38：前端 UI 原型/README.md) | [作业](Day 38：前端 UI 原型/assignment.md)
- [Day 39：端到端流程](Day 39：端到端流程/README.md) | [作业](Day 39：端到端流程/assignment.md)
- [Day 40：用户确认](Day 40：用户确认/README.md) | [作业](Day 40：用户确认/assignment.md)
- [Day 41：文档和演示](Day 41：文档和演示/README.md) | [作业](Day 41：文档和演示/assignment.md)
- [Day 42：总复盘](Day 42：总复盘/README.md) | [作业](Day 42：总复盘/assignment.md)

