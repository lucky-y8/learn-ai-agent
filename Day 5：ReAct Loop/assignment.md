# Day 5 作业：ReAct Loop

## 作业要求

```text
写一个最小 ReAct SQL Agent。

用户输入：
"帮我写一个查询每月销售额趋势的 SQL"

Agent 流程：
1. 调 get_dataset_columns
2. 根据字段生成 SQL
3. 调 validate_sql
4. 返回 SQL 和解释
```

限制：

```text
最多 5 次工具调用
工具失败后最多重试 1 次
必须输出最终 answer
```

## 需要提交的产出

```text
assignments/week1/react_sql_agent.py
```

## Hugging Face 阅读检查
- [ ] 已阅读/复习 Hugging Face Agents Course Unit 1，并把 Agent 基础概念写入本日总结。

## 提交说明
请在完成后填写下面内容，方便 Codex 批改。

### 我完成了什么
- 

### 如何运行 / 查看
```bash
# 在这里写运行命令或查看路径
```

### 自测结果
- 

### 我遇到的问题
- 

### 想让 Codex 重点批改
- 

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
