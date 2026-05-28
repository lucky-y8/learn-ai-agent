# Day 27：周项目 4 学习笔记

## 今日学习内容
- 实现 LangGraph SQL Agent 项目。
- 搭建 classify_intent、build_context、get_schema、generate_sql、sql_guard、wait_confirm、final_response 节点。
- 明确每个节点输入输出。
- 把 SQL guard 放在确认之前。
- 输出可演示的完整 workflow。

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

## Hugging Face 对应内容
- 阅读范围：Unit 2.3 LangGraph。
- 重点：StateGraph、节点、边、条件路由、checkpoint、human-in-the-loop。
- 写进作业：对比你的图工作流和课程中的 graph building blocks。

## 我的理解
- 

## 今日疑问
- 

## 今日小结
- 
