# Day 24：Tool Node 学习笔记

## 今日学习内容
- 学习 LangGraph 中工具节点的接入方式。
- 把 get_dataset_columns、get_dataset_metrics、validate_sql、recommend_chart_type 接进图。
- 把工具结果写回 state。
- 处理工具错误并保留 observation。
- 记录 tool timeline 方便调试。

### Tool Node
Tool Node 把工具调用放进图工作流中。它接收 state 中的 tool request，执行工具，再把结果写回 state。

### 工具接入
get_dataset_columns、get_dataset_metrics、validate_sql、recommend_chart_type 都应该有稳定输入输出。

### 错误回填
工具错误不要让图崩溃，要写入 state 中的 errors 或 observations。

### 今日笔记要点
- LangGraph 让工具调用变成图中的一个节点。
- 工具节点仍然需要参数校验和日志。

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
