# Day 1：LLM API 和 Prompt 基础 学习笔记

## 今日学习内容
- 理解 Chat Completions 的输入输出结构：messages -> assistant reply。
- 区分 system prompt 和 user prompt 的职责。
- 理解 token、context window、temperature、streaming 的实际意义。
- 跑通一个 OpenAI-compatible API provider。
- 记录 provider 切换方式、环境变量和运行命令。

### Chat Completions
Chat Completions 是最基础的对话式模型调用方式。你把一组 messages 发给模型，模型根据历史消息、system 约束和 user 请求生成 assistant 回复。今天只需要理解三件事：输入是消息列表，不是一整段裸文本；输出通常包含 assistant message；多轮对话就是把历史消息继续追加进去。

### System prompt
System prompt 是给模型的长期行为约束，例如“你是一个 SQL 助手，只生成只读查询”。它适合放角色、边界、输出格式、安全规则，不适合放用户每次变化的问题。写 system prompt 时要明确、短、可执行。

### User prompt
User prompt 是用户当前这一次请求，例如“帮我写查询每月销售额趋势的 SQL”。它是任务输入，不是行为规则。真实 Agent 里，user prompt 会和上下文、工具结果、历史消息一起传给模型。

### Token / context window
Token 可以粗略理解为模型读写文本的计量单位。context window 是模型一次能看到的最大 token 范围。历史消息、系统提示、工具结果、检索上下文都会占 token，所以 Agent 不能无限塞上下文，需要摘要、裁剪和只放必要信息。

### Temperature
Temperature 控制输出随机性。值越低，输出越稳定，适合 SQL、JSON、分类、工具参数；值越高，表达更发散，适合创意文案。做 SQL Agent 时默认用低 temperature，因为稳定和可校验比灵感更重要。

### Streaming
Streaming 是边生成边返回，用户能更快看到输出。它对长回答和前端体验有用，但对工具调用、JSON 校验、SQL 安全检查要小心：不能因为流式展示就跳过最终校验。

### OpenAI-compatible API
OpenAI-compatible API 指很多厂商提供相似的请求格式，例如 base_url、api_key、model、messages。这样你可以把阿里百炼、DeepSeek、豆包等 provider 封装成同一个 ModelClient。核心思想是 provider 可替换，Tool Layer、State、Safety 不跟具体模型绑定。

### 今日笔记要点
- Chat demo 的最小闭环是：读取配置 -> 组装 messages -> 调模型 -> 打印 assistant 回复。
- provider 切换最好通过环境变量或配置文件完成，不要把 API key 写死在代码里。
- README 里至少记录 base_url、model、api_key 环境变量名、运行命令和一个示例输入输出。

## 学习来源
- Hugging Face Agents Course Unit 1：https://huggingface.co/learn/agents-course/en/unit1/introduction
- OpenAI API Quickstart：https://developers.openai.com/api/docs/quickstart
- OpenAI Text Generation：https://developers.openai.com/api/docs/guides/text
- OpenAI Chat API Reference：https://developers.openai.com/api/reference/resources/chat
- 学习方法：先看 HF 理解 Agent/LLM/message 概念，再用 OpenAI-compatible API 文档跑通最小 chat demo。

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
