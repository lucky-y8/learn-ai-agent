# Day 29：SQL Guard

## 今日目标
按照原计划完成 Day 29 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

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
实现 sql_guard(sql)

只允许：
SELECT
WITH

禁止：
DROP
DELETE
UPDATE
INSERT
ALTER
TRUNCATE
CREATE
MERGE
CALL
```

产出：

```text
assignments/week5/sql_guard.py
```

## 今日学习内容
- 学习 SQL Guard 的 allowlist 思路。
- 只允许 SELECT 和 WITH。
- 禁止 DROP、DELETE、UPDATE、INSERT、ALTER、TRUNCATE、CREATE、MERGE、CALL。
- 实现 normalize 和关键字检查。
- 返回结构化安全检查结果和 reason。

## 学习内容详解与笔记

### SQL Guard
SQL Guard 是安全闸门，用来拒绝危险 SQL。

### 只允许 SELECT / WITH
BI 查询通常只需要只读语句。WITH 是 CTE，常用于复杂查询。

### 禁止语句
DROP、DELETE、UPDATE、INSERT、ALTER、TRUNCATE、CREATE、MERGE、CALL 都可能改变数据、结构或触发副作用。

### 解析策略
简单实现可以先做 normalize + 关键字检查；更稳的是使用 SQL parser。

### 今日笔记要点
- 黑名单不够，最好用 allowlist。
- Guard 要返回明确 reason。

## 学习来源
- OpenAI Function Calling / tools 设计：https://developers.openai.com/api/docs/guides/function-calling
- Hugging Face Bonus Unit 2 Observability and Evaluation：https://huggingface.co/learn/agents-course/en/bonus-unit2/introduction
- Superset 文档入口：https://superset.apache.org/docs/intro/
- 学习方法：结合 Superset 的权限和 SQL 使用场景，设计 SQL guard、context builder、tool layer、audit log。

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
