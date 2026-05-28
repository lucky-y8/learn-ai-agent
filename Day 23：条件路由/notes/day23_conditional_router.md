# Day 23：条件路由 学习笔记

## 今日学习内容
- 学习条件路由 conditional edges。
- 根据 intent 路由到 sql_node、explain_node、chart_node、dashboard_node。
- 设计 unknown intent 的默认分支。
- 写测试用例验证不同 intent 路由正确。
- 理解条件路由如何让 Agent 决策显式化。

### 条件路由
条件路由根据 state 中的 intent 决定下一节点。

### Intent 到 Node
generate_sql 进入 sql_node；explain_sql 进入 explain_node；recommend_chart 进入 chart_node；summarize_dashboard 进入 dashboard_node。

### 默认分支
必须处理 unknown 或无法识别 intent，避免图断掉。

### 今日笔记要点
- 条件边是 Agent 决策逻辑的显式化。
- 路由函数要简单、可测试。

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
