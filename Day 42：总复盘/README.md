# Day 42：总复盘

## 今日目标
按照原计划完成 Day 42 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

## 固定学习节奏

| 时间 | 内容 |
|---|---|
| 09:30-11:30 | 看文档 / 看课程 / 做笔记 |
| 11:30-12:00 | 画流程图 / 总结概念 |
| 14:00-17:30 | 写代码 demo / debug |
| 20:00-21:30 | 复盘 / README / 整理项目 |

## 原始计划内容

最终答辩问题：

```text
1. 为什么用 DAG + ReAct？
2. 为什么不能让模型直接执行 SQL？
3. Superset 上下文怎么构建？
4. 权限怎么保证？
5. SQL 安全怎么做？
6. 如何评估 Agent 质量？
7. 为什么不绑定 Microsoft Agent Framework？
8. 如果换成百炼 / DeepSeek / 豆包，架构哪些地方需要改？
```

最终产出：

```text
projects/week6_superset_agent_mvp/
```

## 今日学习内容
- 完成总复盘和答辩问题。
- 解释为什么用 DAG + ReAct。
- 解释为什么不能让模型直接执行 SQL。
- 说明 Superset 上下文、权限、SQL 安全和评估方案。
- 说明如果换模型 provider，架构哪些地方需要改。

## 学习内容详解与笔记

### DAG + ReAct
DAG 让流程可控，ReAct 让局部步骤能根据观察调整。两者结合适合生产 Agent。

### 不直接执行 SQL
模型输出必须经过 SQL guard、权限检查和用户确认，避免破坏数据或泄露信息。

### Superset 上下文
上下文来自 dashboard、chart、dataset、filters、SQL Lab、用户权限和业务 metadata。

### 权限保证
每次工具调用都要带 user/session，并检查资源权限。

### SQL 安全
只允许 SELECT/WITH，禁止危险语句，执行前校验，必要时 parser 解析。

### Agent 评估
用 eval cases 检查安全、字段、工具调用、确认流程、引用和回答质量。

### Provider 可替换
换百炼、DeepSeek、豆包时，主要改 ModelClient 配置；Tool Layer、State、Safety、Eval 不应该大改。

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

## 本章代码
- [code/README.md](code/README.md)

## 本章笔记
- [notes/day42_final_review.md](notes/day42_final_review.md)

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
