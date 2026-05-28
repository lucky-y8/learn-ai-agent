# Day 13：周项目 2

## 今日目标
按照原计划完成 Day 13 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

## 固定学习节奏

| 时间 | 内容 |
|---|---|
| 09:30-11:30 | 看文档 / 看课程 / 做笔记 |
| 11:30-12:00 | 画流程图 / 总结概念 |
| 14:00-17:30 | 写代码 demo / debug |
| 20:00-21:30 | 复盘 / README / 整理项目 |

## 原始计划内容

项目：

```text
BI Metadata Assistant
```

功能：

```text
用户问业务问题
-> 检索相关字段
-> 获取数据集 schema
-> 推荐 SQL 字段
-> 给出 SQL 草稿
```

产出：

```text
projects/week2_bi_metadata_assistant/
```

## 今日学习内容
- 把 BI metadata 检索、schema tool、SQL 草稿生成串成项目。
- 让用户用业务语言提问。
- 检索相关字段并解释选择原因。
- 获取数据集 schema 并推荐 SQL 字段。
- 输出 SQL 草稿而不是直接执行 SQL。

## 学习内容详解与笔记

### BI Metadata Assistant
这个项目目标是把业务问题变成字段推荐和 SQL 草稿。

### 业务问题理解
用户通常说“收入趋势”“销售表现”，系统要映射到字段、指标和数据集。

### 字段检索
先用 RAG 找相关字段说明，再用工具确认 schema。

### SQL 草稿
草稿不等于最终执行 SQL，仍要经过校验和用户确认。

### 今日笔记要点
- Metadata Assistant 是 Superset Agent 的上下文层雏形。
- 返回结果要解释为什么选择这些字段。

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
