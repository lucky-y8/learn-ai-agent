# Day 25：Human-in-the-loop

## 今日目标
按照原计划完成 Day 25 的学习、代码或文档产出，并把结果整理到作业文件中，方便 Codex 批改。

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
SQL 生成后暂停：

Agent:
"这是生成的 SQL，是否插入 SQL Lab？"

用户确认后继续。
```

产出：

```text
assignments/week4/human_confirm_sql.py
```

## 今日学习内容
- 学习 Human-in-the-loop 的暂停与继续。
- 在 SQL 生成后暂停，等待用户确认。
- 确认前只展示 SQL 和解释，不执行动作。
- 用户确认后继续流程，取消后停止。
- 理解人工确认是 SQL Agent 的安全边界。

## 学习内容详解与笔记

### Human-in-the-loop
有风险的动作需要暂停等待用户确认。SQL 插入 SQL Lab 就属于需要确认的动作。

### 暂停点
SQL 生成后、执行或插入前是最合适的暂停点。用户要看到 SQL 和解释。

### 继续执行
用户确认后，workflow 从暂停状态继续；用户取消则停止任务。

### 今日笔记要点
- 人工确认是安全机制，不是 UI 装饰。
- 确认前不能执行有副作用动作。

## 学习来源
- LangGraph 官方文档：https://langchain-ai.github.io/langgraph/
- Hugging Face Agents Course Unit 2.3 LangGraph：https://huggingface.co/learn/agents-course/en/unit2/langgraph/introduction
- 学习方法：HF 先看图工作流的概念，LangGraph 官方文档看 StateGraph、node、edge、checkpoint 的实现。

## Hugging Face Agents Course
- 阅读范围：Unit 2.3 LangGraph。
- 重点：StateGraph、节点、边、条件路由、checkpoint、human-in-the-loop。
- 写进作业：对比你的图工作流和课程中的 graph building blocks。

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
