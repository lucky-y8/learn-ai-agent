# Day 25：Human-in-the-loop 学习笔记

## 今日学习内容
- 学习 Human-in-the-loop 的暂停与继续。
- 在 SQL 生成后暂停，等待用户确认。
- 确认前只展示 SQL 和解释，不执行动作。
- 用户确认后继续流程，取消后停止。
- 理解人工确认是 SQL Agent 的安全边界。

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

## Hugging Face 对应内容
- 阅读范围：Unit 2.3 LangGraph。
- 重点：StateGraph、节点、边、条件路由、checkpoint、human-in-the-loop。
- 写进作业：对比你的图工作流和课程中的 graph building blocks。

## 我的理解
- 

## 今日疑问
- 

## 今日小结
- 
