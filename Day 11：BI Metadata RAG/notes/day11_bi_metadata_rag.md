# Day 11：BI Metadata RAG 学习笔记

## 今日学习内容
- 学习 Superset metadata 的核心对象：dataset、column、metric、chart、dashboard。
- 构造 datasets.json、charts.json、dashboards.json。
- 实现从图表问题追踪到 chart、dataset、columns。
- 理解图表字段、过滤条件和数据集之间的关系。
- 为后续 dashboard 总结和 SQL 生成准备上下文。

### Dataset metadata
Dataset metadata 描述数据集名称、字段、指标、权限、来源。SQL Agent 生成查询前必须知道这些信息。

### Column description
字段说明把技术字段和业务语言连接起来，例如 revenue 表示销售额。

### Metric
Metric 是业务指标定义，例如 GMV、转化率、客单价。指标往往不等于单个字段，可能包含公式。

### Chart metadata
Chart metadata 告诉你图表用了哪个 dataset、哪些字段、什么图表类型、过滤条件。

### Dashboard metadata
Dashboard metadata 包含多个 chart、全局 filter、业务主题。总结 dashboard 时要用它。

### 今日笔记要点
- Superset Agent 的上下文主要来自 metadata。
- 用户问图表问题时，要先找到 chart，再追到 dataset 和 columns。

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
