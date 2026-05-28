# Day 31：Context Builder 学习笔记

## 今日学习内容
- 学习 Context Builder 在 Agent 中的作用。
- 实现 build_sqllab_context。
- 实现 build_dashboard_context。
- 实现 build_explore_context。
- 实现 build_dataset_context，并统一返回结构化 JSON。

### Context Builder
Context Builder 把不同页面状态整理成模型可用的结构化上下文。

### SQL Lab context
包含当前 SQL、数据库、schema、dataset、用户光标或选中文本。

### Dashboard context
包含 dashboard id、charts、filters、时间范围、用户正在查看的图表。

### Explore context
包含当前图表配置、dataset、metrics、dimensions、filters。

### Dataset context
包含字段、类型、描述、指标、权限。

### 今日笔记要点
- 上下文越结构化，模型越稳定。
- 不要把整个页面无脑塞给模型。

## 学习来源
- OpenAI Function Calling / tools 设计：https://developers.openai.com/api/docs/guides/function-calling
- Hugging Face Bonus Unit 2 Observability and Evaluation：https://huggingface.co/learn/agents-course/en/bonus-unit2/introduction
- Superset 文档入口：https://superset.apache.org/docs/intro/
- 学习方法：结合 Superset 的权限和 SQL 使用场景，设计 SQL guard、context builder、tool layer、audit log。

## Hugging Face 对应内容
- 阅读范围：Bonus Unit 2 Observability and Evaluation。
- 重点：trace、tool usage、latency、token usage、用户反馈、评估集。
- 写进作业：说明 Safety / Audit / Eval 如何让 Agent 可控。

## 我的理解
- 

## 今日疑问
- 

## 今日小结
- 
