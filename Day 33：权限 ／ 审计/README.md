# Day 33：权限 ／ 审计

## 今日目标
按照原计划完成 Day 33 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

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
设计 audit log schema：

user_id
session_id
tool_name
input_hash
risk_level
timestamp
status
error
model_provider
token_usage
```

产出：

```text
assignments/week5/audit_log_design.md
```

## 今日学习内容
- 设计 audit log schema。
- 理解 user_id、session_id、tool_name、input_hash 的作用。
- 记录 risk_level、timestamp、status、error。
- 记录 model_provider 和 token_usage。
- 思考敏感信息脱敏和可追踪性之间的平衡。

## 学习内容详解与笔记

### Audit log
Audit log 记录 Agent 做过什么、谁触发的、用了什么工具、结果如何。

### input_hash
不要直接记录敏感输入全文，可以记录 hash，必要字段脱敏。

### risk_level
risk_level 帮助筛选高风险行为，例如 SQL 写入、图表创建、跨 dataset 访问。

### token_usage
token_usage 用于成本分析和异常检测。

### status / error
每次工具调用都要知道成功或失败，失败原因是什么。

### 今日笔记要点
- 审计是生产 Agent 的底线。
- 日志要能回答“谁在什么时候让 Agent 做了什么”。

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

## 本章代码
- [code/README.md](code/README.md)

## 本章笔记
- [notes/day33_permission_audit.md](notes/day33_permission_audit.md)

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
