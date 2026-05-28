# Day 12：RAG + Tool Router 学习笔记

## 今日学习内容
- 区分 RAG 找知识和 Tool 查实时信息。
- 设计用户问题到 RAG/Tool/RAG+Tool 的路由规则。
- 实现字段含义、表结构、SQL 生成、dashboard 总结的不同路径。
- 处理 unknown 或混合意图。
- 说明 router 在 Agent 中承担的决策职责。

### RAG 找知识
字段含义、指标口径、业务解释适合 RAG，因为这些是文档知识。

### Tool 查实时信息
表结构、当前图表配置、dashboard filters 适合 Tool，因为它们来自系统实时状态。

### Router
Router 根据 intent 和问题类型决定走 RAG、Tool 或两者组合。

### RAG + Tool
生成 SQL 常常需要两类信息：业务含义来自 RAG，真实字段和表结构来自 Tool。

### 今日笔记要点
- Router 是 Agent 的决策层。
- 不同问题要走不同信息来源，不能所有问题都塞给 RAG。

## 学习来源
- Hugging Face Agents Course Unit 3 Agentic RAG：https://huggingface.co/learn/agents-course/en/unit3/agentic-rag/introduction
- Datawhale Hello-Agents：https://github.com/datawhalechina/hello-agents
- Superset 文档入口：https://superset.apache.org/docs/intro/
- 学习方法：HF 学 Agentic RAG 思路，Datawhale 补中文解释，Superset 文档帮助理解 BI metadata 场景。

## Hugging Face 对应内容
- 阅读范围：Unit 3 Agentic RAG。
- 重点：检索不是最终答案，检索结果要作为上下文交给 Agent 判断和生成。
- 写进作业：把 Agentic RAG 映射到 Superset metadata 检索。

## 我的理解
- 

## 今日疑问
- 

## 今日小结
- 
