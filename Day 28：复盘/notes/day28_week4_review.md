# Day 28：复盘 学习笔记

## 今日学习内容
- 画 Superset SQL Agent Workflow DAG。
- 写清每个 node 的职责。
- 写清每条 edge 的条件。
- 写清 state 里保存的字段。
- 标出哪些地方需要 human confirmation。

### DAG 图
DAG 图用来表达节点和边，帮助别人理解 Agent 工作流。

### Node 职责
每个 node 要写清输入、处理、输出。

### Edge 条件
边不是线条而已，要写清什么时候走这条边。

### State 内容
state 是节点之间传递信息的合同，必须列出关键字段。

### Human confirmation
标出哪些节点前后需要用户确认，例如 SQL 插入、执行、创建图表。

### 今日笔记要点
- 复盘要能让别人照图复现流程。

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
