# Day 19：Planner ／ Executor 学习笔记

## 今日学习内容
- 实现 Planner，把用户任务拆成 steps。
- 实现 StepExecutor，逐步执行 steps。
- 设计 step 的状态：pending、running、done、failed。
- 失败时返回 failed step 和 reason。
- 理解 Planner 和 Executor 的职责边界。

### Planner
Planner 把用户任务拆成 steps。比如“生成月销售趋势 SQL”可以拆成识别数据集、获取字段、生成 SQL、校验 SQL、返回解释。

### StepExecutor
StepExecutor 逐步执行 steps，并记录每一步状态。

### 失败处理
失败时要返回 failed_step 和 reason，而不是只说“失败了”。这样用户和开发者能定位问题。

### 计划粒度
步骤太粗无法恢复，太细会增加复杂度。今天用 3-6 步即可。

### 今日笔记要点
- Planner 负责“做什么”，Executor 负责“怎么推进”。
- 计划要能被机器执行，而不是写成空泛自然语言。

## 学习来源
- Datawhale Hello-Agents：https://github.com/datawhalechina/hello-agents
- Hugging Face Agents Course Unit 1：https://huggingface.co/learn/agents-course/en/unit1/introduction
- Hugging Face Agents Course：https://huggingface.co/learn/agents-course/en
- 学习方法：Datawhale 作为中文主线，HF 作为概念校准，目标是手搓 Message/State/Tool/Executor/Memory/Planner。

## Hugging Face 对应内容
- 阅读范围：Unit 1 复习 + Unit 2 框架概览。
- 重点：框架解决的是状态、工具、执行循环、记忆和编排问题。
- 写进作业：说明你手搓的模块对应哪个 Agent 概念。

## 我的理解
- 

## 今日疑问
- 

## 今日小结
- 
