# Day 26：Checkpoint ／ Resume 学习笔记

## 今日学习内容
- 学习 checkpoint 的意义：保存工作流 state。
- 实现中断后保存 state。
- 实现 resume，从保存状态继续执行。
- 保存 pending confirmation、generated_sql、tool_results 等关键字段。
- 理解生产 Agent 为什么必须支持恢复。

### Checkpoint
Checkpoint 保存当前 state，让流程可以中断后恢复。

### Resume
Resume 从保存的 state 继续执行，而不是从头再来。

### 保存什么
至少保存 user_input、intent、context、generated_sql、tool_results、current_node、pending_confirmation。

### 失败恢复
工具失败或用户关闭页面后，可以通过 checkpoint 找回任务进度。

### 今日笔记要点
- 生产 Agent 必须考虑中断。
- state 设计得好，resume 才简单。

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
