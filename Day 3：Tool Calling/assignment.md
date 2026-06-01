# Day 3 作业：Tool Calling

## 作业要求

```text
实现 4 个 mock tools：

get_dataset_columns(dataset_id)
get_dataset_metrics(dataset_id)
validate_sql(sql)
recommend_chart_type(columns)
```

示例：

```python
get_dataset_columns("sales")
# 返回 ["ds", "region", "revenue", "quantity"]
```

## 需要提交的产出

```text
assignments/week1/tools.py
assignments/week1/tool_calling_demo.py
```

## Hugging Face 阅读检查
- [x] 已阅读/复习 Hugging Face Agents Course Unit 1，并把 Agent 基础概念写入本日总结。

## 提交说明
请在完成后填写下面内容，方便 Codex 批改。

### 我完成了什么
- 完成 `Day 3：Tool Calling/week1/tools.py`。
- 完成 `Day 3：Tool Calling/week1/tool_calling_demo.py`。
- 实现 4 个 Superset / BI 风格 mock tools：`get_dataset_columns`、`get_dataset_metrics`、`validate_sql`、`recommend_chart_type`。
- 统一设计 tool result / tool error 返回格式：`ok`、`data`、`error`。
- 写了 tool schemas、工具注册表和工具执行器，演示“模型选择工具 -> 代码执行工具 -> 返回 observation”的完整流程。
- 给代码补充中文注释，方便复习 Tool Calling 的分工和执行链路。

### 如何运行 / 查看
```bash
python "Day 3：Tool Calling/week1/tools.py"

python "Day 3：Tool Calling/week1/tool_calling_demo.py" "帮我看一下 sales 数据集有哪些字段"

python "Day 3：Tool Calling/week1/tool_calling_demo.py" --show-schemas
```

### 自测结果
- 语法检查通过：

```bash
python -m py_compile "Day 3：Tool Calling/week1/tools.py" "Day 3：Tool Calling/week1/tool_calling_demo.py"
```

- demo 输入：

```text
帮我看一下 sales 数据集有哪些字段
```

- demo 输出包含：

```json
{
  "tool_call": {
    "name": "get_dataset_columns",
    "arguments": {
      "dataset_id": "sales"
    }
  },
  "tool_result": {
    "ok": true,
    "data": {
      "dataset_id": "sales",
      "columns": ["ds", "region", "revenue", "quantity"]
    },
    "error": null
  }
}
```

### 我遇到的问题
- 原始文件还是 TODO 模板，需要补齐真实工具函数、demo 执行流程和中文注释。
- 作业说明里的原始产出路径写的是 `assignments/week1/...`，实际按当前项目结构放在 `Day 3：Tool Calling/week1/...`。

### 想让 Codex 重点批改
- 4 个 mock tools 的输入输出契约是否清楚。
- `validate_sql` 的安全校验和 reason 是否足够明确。
- tool schema、tool registry、tool executor 的拆分是否适合后续扩展到 ToolRegistry。
- 是否贴合 Superset / BI / SQL Agent 主线。

## Codex 批改区

### 评分
- 完成度：
- 正确性：
- 工程质量：
- Superset 贴合度：

### 问题清单
- 

### 修改建议
- 
