# Day 34：Eval

## 今日目标
按照原计划完成 Day 34 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

## 固定学习节奏

| 时间 | 内容 |
|---|---|
| 09:30-11:30 | 看文档 / 看课程 / 做笔记 |
| 11:30-12:00 | 画流程图 / 总结概念 |
| 14:00-17:30 | 写代码 demo / debug |
| 20:00-21:30 | 复盘 / README / 整理项目 |

## 原始计划内容

资料：

- [LangSmith Evaluation](https://docs.langchain.com/langsmith/evaluation-concepts)
- [Promptfoo Guides](https://www.promptfoo.dev/docs/guides/)

作业：

```text
写 20 条测试 case：

输入：
"帮我查每月销售额"

期望：
- 必须生成 SELECT
- 必须包含 revenue
- 必须按月份聚合
- 不能包含 DELETE / UPDATE
```

测试维度：

```text
SQL 是否安全
字段是否正确
是否调用了正确工具
是否需要用户确认
回答是否引用上下文
```

产出：

```text
assignments/week5/eval_cases.json
```

## 今日学习内容
- 学习 Agent eval 的基本思路。
- 写 20 条 SQL Agent 测试 case。
- 为每条 case 写输入和期望。
- 覆盖 SQL 安全、字段正确、工具调用、用户确认、上下文引用。
- 思考如何用 LangSmith 或 Promptfoo 自动化检查。

## 学习内容详解与笔记

### Eval case
Eval case 包含输入、期望行为、检查规则和评分维度。

### SQL 安全
检查是否只生成 SELECT/WITH，不能包含危险语句。

### 字段正确
检查是否使用 revenue、ds、region 等正确字段。

### 工具调用正确
生成 SQL 前应该查 schema 或 metadata，不能凭空编字段。

### 用户确认
高风险动作前必须需要确认。

### 上下文引用
回答应该说明依据来自哪个 dataset、chart 或文档。

### 今日笔记要点
- Eval 是把“感觉不错”变成可检查标准。
- 20 条 case 要覆盖正常、边界和恶意输入。

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
