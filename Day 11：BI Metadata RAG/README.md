# Day 11：BI Metadata RAG

## 今日目标
按照原计划完成 Day 11 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

## 固定学习节奏

| 时间 | 内容 |
|---|---|
| 09:30-11:30 | 看文档 / 看课程 / 做笔记 |
| 11:30-12:00 | 画流程图 / 总结概念 |
| 14:00-17:30 | 写代码 demo / debug |
| 20:00-21:30 | 复盘 / README / 整理项目 |

## 原始计划内容

学习内容：

```text
Dataset metadata
Column description
Metric
Chart metadata
Dashboard metadata
```

作业：

```text
构造 mock Superset metadata：

datasets.json
charts.json
dashboards.json

实现：
用户问 "销售趋势图用了哪些字段？"
系统能找到对应 chart、dataset、columns。
```

产出：

```text
assignments/week2/bi_metadata_rag.py
```

## 今日学习内容
- 学习 Superset metadata 的核心对象：dataset、column、metric、chart、dashboard。
- 构造 datasets.json、charts.json、dashboards.json。
- 实现从图表问题追踪到 chart、dataset、columns。
- 理解图表字段、过滤条件和数据集之间的关系。
- 为后续 dashboard 总结和 SQL 生成准备上下文。

## 学习内容详解与笔记

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

## Hugging Face Agents Course
- 阅读范围：Unit 3 Agentic RAG。
- 重点：检索不是最终答案，检索结果要作为上下文交给 Agent 判断和生成。
- 写进作业：把 Agentic RAG 映射到 Superset metadata 检索。

## 今日作业
请按上方“原始计划内容”中的作业、要求和产出路径完成今天任务。完成后，把提交说明写到本文件夹的 `assignment.md`，方便 Codex 批改。

## 完成标准
- 完成原计划中列出的代码、文档或项目产出。
- 能用自己的话解释今天的核心概念。
- 在 `assignment.md` 中填写完成内容、运行方式、自测结果和疑问。
- 代码类作业至少提供一个可运行示例或自测说明。
- 文档类作业要结合 BI / Superset / SQL Agent 主线。

## 给 Codex 批改时重点看
- 是否满足当天作业的全部要求。
- 产出路径是否和计划一致。
- 代码是否能运行，错误处理是否清楚。
- 解释是否准确，是否贴合 Superset 场景。
