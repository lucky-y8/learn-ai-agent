# Day 6：周项目 1 学习笔记

## 今日学习内容
- 把第 1 周的 intent、tool、SQL generation、SQL validation 串起来。
- 实现 Mini SQL Assistant v0 的完整 happy path。
- 补齐 unknown intent、tool error、SQL invalid 等错误路径。
- 写 README、日志和示例输入输出。
- 确认项目不依赖任何 Agent 框架。

### Mini SQL Assistant v0 的闭环
本项目把 intent classifier、mock schema tool、SQL generation、validate_sql 串成一个最小助手。重点不是模型多强，而是流程是否清楚。

### 不依赖 Agent 框架
本周项目要求不用 LangGraph、CrewAI、AutoGen。你要自己写清楚每一步函数调用和状态传递。

### 错误处理
至少处理 unknown intent、dataset 不存在、SQL 校验失败、工具异常。错误返回要能被用户看懂，也能被日志记录。

### 日志
记录每次用户输入、intent、工具调用、SQL 校验结果、最终回答。日志会帮助后面做 audit 和 eval。

### README
README 要说明运行方式、示例输入输出、模块结构、限制。一个 demo 能不能被别人跑起来，README 很关键。

### 今日笔记要点
- 周项目是把零散知识变成可运行作品。
- 最小可用比功能多更重要。
- 先跑通 happy path，再补错误路径。

## 学习来源
- Hugging Face Agents Course Unit 1：https://huggingface.co/learn/agents-course/en/unit1/introduction
- Datawhale Hello-Agents：https://github.com/datawhalechina/hello-agents
- 学习方法：复盘 Agent、Tool Calling、ReAct，把概念落到 Mini SQL Assistant。

## Hugging Face 对应内容
- 阅读范围：Unit 1 Agent Fundamentals。
- 重点：Agent、Tool、Message、Thought、Action、Observation、ReAct。
- 写进作业：今天的实现或复盘如何体现这些概念。

## 我的理解
- 

## 今日疑问
- 

## 今日小结
- 
