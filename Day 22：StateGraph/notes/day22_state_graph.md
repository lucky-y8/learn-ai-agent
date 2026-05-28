# Day 22：StateGraph 学习笔记

## 今日学习内容
- 学习 LangGraph StateGraph 的基本概念。
- 实现 start -> classify_intent -> final_response。
- 定义 state 中保存哪些字段。
- 理解 node 如何读取 state 并返回更新。
- 理解 edge 如何控制节点流转。

### StateGraph
StateGraph 用状态驱动工作流。每个节点读取 state，返回 state 的增量更新。

### Node
Node 是一个函数，负责一个明确职责，例如 classify_intent 或 final_response。

### Edge
Edge 定义节点之间怎么流转。最简单是固定边：start -> classify -> final。

### State
State 保存 workflow 需要共享的信息，例如 user_input、intent、messages、answer。

### 今日笔记要点
- LangGraph 的核心不是“聊天”，而是状态图。
- 节点要小而清楚。

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
