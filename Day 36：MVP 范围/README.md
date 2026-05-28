# Day 36：MVP 范围

## 今日目标
按照原计划完成 Day 36 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

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
写 MVP scope：

包含：
- 目标用户
- 用户故事
- 功能范围
- 不做什么
- 风险控制
- 成功标准
```

产出：

```text
projects/week6_superset_agent_mvp/mvp_scope.md
```

## 今日学习内容
- 写 Superset AI Agent MVP scope。
- 明确目标用户。
- 写用户故事。
- 定义功能范围和不做什么。
- 定义风险控制和成功标准。

## 学习内容详解与笔记

### MVP scope
MVP scope 定义第一版做什么、不做什么。范围越清楚，项目越容易完成。

### 目标用户
明确是数据分析师、业务运营、BI 开发，还是普通看板用户。

### 用户故事
用“作为某类用户，我想要……以便……”描述需求。

### 功能范围
只放最关键闭环，例如自然语言生成 SQL 草稿并等待确认。

### 不做什么
明确不做自动执行 SQL、不做跨权限访问、不做复杂图表编辑。

### 风险控制
列出 SQL guard、权限检查、用户确认、审计日志。

### 成功标准
成功标准要可验证，例如 5 个示例问题都能生成安全 SQL。

## 学习来源
- Hugging Face Agents Course Unit 4 Final Project：https://huggingface.co/learn/agents-course/en/unit4/introduction
- Superset 文档入口：https://superset.apache.org/docs/intro/
- OpenAI Function Calling：https://developers.openai.com/api/docs/guides/function-calling
- LangGraph 官方文档：https://langchain-ai.github.io/langgraph/
- 学习方法：把前 5 周能力整合成 Superset AI Agent MVP，重点是能演示、能解释、能评估、能控制风险。

## Hugging Face Agents Course
- 阅读范围：Unit 4 Final Project。
- 重点：最终作品要可运行、可展示、可解释、可评估。
- 写进作业：说明你的 Superset Agent MVP 如何满足最终项目标准。

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
