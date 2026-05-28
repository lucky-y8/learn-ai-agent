# Day 14：复盘 学习笔记

## 今日学习内容
- 复盘 RAG、Tool Calling、Agent 的区别。
- 用 Superset 场景解释字段含义、表结构、SQL 生成、Dashboard 总结分别用什么。
- 画出 RAG、Tool、Agent 的关系。
- 总结第 2 周对 Superset metadata assistant 的价值。
- 记录仍不清楚的问题，作为后续项目改进点。

### RAG
RAG 负责找知识，适合字段含义、指标口径、业务文档。

### Tool Calling
Tool Calling 负责查系统状态或执行受控动作，适合 schema、chart metadata、SQL validation。

### Agent
Agent 负责目标、状态和决策，决定什么时候 RAG、什么时候 Tool、什么时候让用户确认。

### Superset 映射
字段解释用 RAG；表结构查询用 Tool；SQL 生成用 RAG + Tool + LLM；Dashboard 总结用 metadata tool + RAG。

### 今日笔记要点
- 复盘要讲关系，不只是分别定义。
- 最好画一张三者关系图。

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
