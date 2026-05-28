# Day 32：Tool Layer 设计

## 今日目标
按照原计划完成 Day 32 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

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
设计 10 个 Superset tools：

get_dataset_columns
get_dataset_metrics
get_chart_metadata
get_dashboard_charts
get_dashboard_filters
validate_sql
preview_sql
generate_chart_config
insert_sql_to_sqllab
create_chart_draft
```

每个工具写：

```text
input schema
output schema
permission
risk level
timeout
audit log fields
```

产出：

```text
assignments/week5/superset_tools_design.md
```

## 今日学习内容
- 设计 10 个 Superset tools。
- 为每个工具写 input schema 和 output schema。
- 为每个工具标注 permission 和 risk level。
- 为每个工具设计 timeout。
- 为每个工具列出 audit log fields。

## 学习内容详解与笔记

### Tool Layer
Tool Layer 是 Superset Agent 与系统能力之间的边界。

### Input / output schema
每个工具都要写清输入输出，避免模型猜参数。

### Permission
工具执行前要检查用户是否有权限访问 dataset、chart、dashboard 或执行动作。

### Risk level
读 metadata 风险低；preview_sql 中等；insert_sql_to_sqllab 或 create_chart_draft 风险更高，需要确认和审计。

### Timeout
每个工具要有超时时间，避免 Agent 卡住。

### Audit log fields
记录 user_id、session_id、tool_name、input_hash、status、error、duration_ms。

### 今日笔记要点
- 工具设计不是函数列表，而是权限和风险边界设计。

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
- [notes/day32_tool_layer_design.md](notes/day32_tool_layer_design.md)

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
