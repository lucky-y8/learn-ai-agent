# Day 35：复盘

## 今日目标
按照原计划完成 Day 35 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

## 固定学习节奏

| 时间 | 内容 |
|---|---|
| 09:30-11:30 | 看文档 / 看课程 / 做笔记 |
| 11:30-12:00 | 画流程图 / 总结概念 |
| 14:00-17:30 | 写代码 demo / debug |
| 20:00-21:30 | 复盘 / README / 整理项目 |

## 原始计划内容

作业：

```text
写一篇：
为什么生产 Agent 必须有 Safety / Audit / Eval？

必须结合 Superset：
1. 权限
2. SQL 安全
3. 数据泄露
4. 用户确认
5. 日志审计
```

产出：

```text
notes/week5_summary.md
```

## 第 6 周：Superset AI Agent MVP

目标：做一个能讲清楚的作品。

## 今日学习内容
- 复盘 Safety、Audit、Eval 为什么是生产 Agent 必备能力。
- 结合 Superset 权限说明安全边界。
- 结合 SQL 安全说明只读和确认机制。
- 结合数据泄露说明上下文控制。
- 结合日志审计说明可追踪性。

## 学习内容详解与笔记

### Safety
Safety 负责防止危险 SQL、越权访问、数据泄露和副作用动作。

### Audit
Audit 负责事后追踪和合规，能还原 Agent 行为。

### Eval
Eval 负责持续检查质量，避免改代码后能力退化。

### Superset 场景
Superset 涉及真实业务数据、权限边界、仪表盘共享和 SQL 执行，所以生产 Agent 必须比普通聊天更谨慎。

### 今日笔记要点
- 复盘要结合权限、SQL 安全、数据泄露、用户确认、日志审计。

## 学习来源
- Hugging Face Bonus Unit 2 Observability and Evaluation：https://huggingface.co/learn/agents-course/en/bonus-unit2/introduction
- LangSmith Evaluation Concepts：https://docs.langchain.com/langsmith/evaluation-concepts
- Promptfoo Eval Guides：https://www.promptfoo.dev/docs/guides/
- 学习方法：把 eval case 写成可检查的输入、期望、评分维度，关注 SQL 安全、字段正确性、工具调用和用户确认。

## Hugging Face Agents Course
- 阅读范围：Bonus Unit 2 Observability and Evaluation。
- 重点：trace、tool usage、latency、token usage、用户反馈、评估集。
- 写进作业：说明 Safety / Audit / Eval 如何让 Agent 可控。

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
