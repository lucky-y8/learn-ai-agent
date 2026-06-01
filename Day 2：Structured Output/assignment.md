# Day 2 作业：Structured Output

## 作业要求

```text
实现 intent classifier。

输入：
"帮我看一下这个 SQL 哪里错了"

输出：
{
  "intent": "fix_sql",
  "confidence": 0.92,
  "needs_tool": true
}
```

要求支持：

```text
generate_sql
fix_sql
explain_sql
summarize_dashboard
recommend_chart
unknown
```

## 需要提交的产出

```text
assignments/week1/intent_classifier.py
```

## Hugging Face 阅读检查
- [x] 已阅读/复习 Hugging Face Agents Course Unit 1，并把 Agent 基础概念写入本日总结。

## 提交说明
请在完成后填写下面内容，方便 Codex 批改。

### 我完成了什么
- 完成 `Day 2：Structured Output/week1/intent_classifier.py`。
- 参考 Day 1 的 OpenAI 兼容客户端写法，支持 OpenAI / DeepSeek / 豆包 / 阿里百炼多厂商切换。
- 实现 SQL Agent intent classifier，支持 `generate_sql`、`fix_sql`、`explain_sql`、`summarize_dashboard`、`recommend_chart`、`unknown`。
- 实现结构化 JSON 输出提示、字段校验、有限重试和 `unknown` 安全兜底。
- 增加 `--mock` 模式，便于没有模型网络时验证输出结构和示例结果。

### 如何运行 / 查看
```bash
python "Day 2：Structured Output/week1/intent_classifier.py" "帮我看一下这个 SQL 哪里错了"

# 无模型网络或只想验证作业示例时：
python "Day 2：Structured Output/week1/intent_classifier.py" "帮我看一下这个 SQL 哪里错了" --mock
```

### 自测结果
- 语法检查通过：`python -m py_compile "Day 2：Structured Output/week1/intent_classifier.py"`
- mock 示例输出：

```json
{
  "intent": "fix_sql",
  "confidence": 0.92,
  "needs_tool": true
}
```

### 我遇到的问题
- 当前本机 `.venv` 在 Codex 沙箱里启动失败，报错为缺少 `encodings` 模块，所以自测时使用 Codex 桌面内置 Python 完成语法检查和 mock 运行。
- Codex 桌面内置 Python 没有安装 `python-dotenv` 和 `openai`，因此作业代码对 `.env` 加了轻量兼容加载；真实模型调用仍需要项目环境安装 `requirements.txt`。

### 想让 Codex 重点批改
- 模型提示词是否足够约束“只返回 JSON”。
- JSON 校验、重试和兜底逻辑是否符合 Structured Output 的工程要求。
- intent 分类是否贴合 SQL Agent / Superset 场景。

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
