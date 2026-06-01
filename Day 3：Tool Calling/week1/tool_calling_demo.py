"""
Day 3 Tool Calling demo

这个 demo 用本地规则模拟“模型选择工具”的过程，重点学习 Tool Calling 的工程链路：

用户输入 -> 模型选择工具和参数 -> 代码执行工具 -> 返回 tool result / tool error

真实接入 LLM 时，“select_tool_call” 这一层可以替换成模型的 tool_calls 输出。
"""

from __future__ import annotations

import argparse
import json
from typing import Any, Callable, Dict

from tools import (
    get_dataset_columns,
    get_dataset_metrics,
    recommend_chart_type,
    validate_sql,
)


# Tool schema 是给模型看的工具说明：工具能做什么、需要哪些参数、参数类型是什么。
TOOL_SCHEMAS = [
    {
        "name": "get_dataset_columns",
        "description": "查询 Superset 数据集的字段列表",
        "parameters": {
            "type": "object",
            "properties": {
                "dataset_id": {"type": "string", "description": "数据集 ID"},
            },
            "required": ["dataset_id"],
        },
    },
    {
        "name": "get_dataset_metrics",
        "description": "查询 Superset 数据集的可用指标列表",
        "parameters": {
            "type": "object",
            "properties": {
                "dataset_id": {"type": "string", "description": "数据集 ID"},
            },
            "required": ["dataset_id"],
        },
    },
    {
        "name": "validate_sql",
        "description": "校验 SQL 是否安全、是否符合只读查询要求",
        "parameters": {
            "type": "object",
            "properties": {
                "sql": {"type": "string", "description": "需要校验的 SQL"},
            },
            "required": ["sql"],
        },
    },
    {
        "name": "recommend_chart_type",
        "description": "根据字段列表推荐图表类型",
        "parameters": {
            "type": "object",
            "properties": {
                "columns": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "字段名称列表",
                },
            },
            "required": ["columns"],
        },
    },
]


# 工具注册表：执行器通过 tool name 找到真正的 Python 函数。
TOOL_REGISTRY: Dict[str, Callable[..., Dict[str, Any]]] = {
    "get_dataset_columns": get_dataset_columns,
    "get_dataset_metrics": get_dataset_metrics,
    "validate_sql": validate_sql,
    "recommend_chart_type": recommend_chart_type,
}


def infer_dataset_id(text: str) -> str:
    """从用户输入里粗略识别 dataset_id；真实项目里可由模型或前端上下文提供。"""
    lowered = text.lower()
    for dataset_id in ["sales", "users", "orders"]:
        if dataset_id in lowered:
            return dataset_id
    return "sales"


def select_tool_call(user_input: str) -> Dict[str, Any]:
    """
    模拟模型选择工具。

    Day 3 的关键概念是：模型不执行工具，只输出类似下面的结构：
    {"name": "get_dataset_columns", "arguments": {"dataset_id": "sales"}}
    """
    text = user_input.lower()
    dataset_id = infer_dataset_id(text)

    if "字段" in text or "columns" in text or "列" in text:
        return {
            "name": "get_dataset_columns",
            "arguments": {"dataset_id": dataset_id},
        }

    if "指标" in text or "metrics" in text:
        return {
            "name": "get_dataset_metrics",
            "arguments": {"dataset_id": dataset_id},
        }

    if "校验" in text or "validate" in text or "sql" in text:
        return {
            "name": "validate_sql",
            "arguments": {"sql": extract_sql(user_input)},
        }

    if "图表" in text or "可视化" in text or "chart" in text:
        return {
            "name": "recommend_chart_type",
            "arguments": {"columns": ["ds", "revenue"]},
        }

    return {
        "name": "get_dataset_columns",
        "arguments": {"dataset_id": dataset_id},
    }


def extract_sql(user_input: str) -> str:
    """从输入中提取 SQL；如果用户没写完整 SQL，就给一个默认查询用于演示。"""
    lowered = user_input.lower()
    select_index = lowered.find("select")
    if select_index >= 0:
        return user_input[select_index:].strip()
    return "select ds, revenue from sales"


def execute_tool_call(tool_call: Dict[str, Any]) -> Dict[str, Any]:
    """
    工具执行器。

    执行器负责三件事：
    1. 检查工具名是否存在。
    2. 把 arguments 传给对应 Python 函数。
    3. 捕获异常并返回结构化错误。
    """
    tool_name = tool_call.get("name")
    arguments = tool_call.get("arguments", {})

    if tool_name not in TOOL_REGISTRY:
        return {
            "ok": False,
            "data": None,
            "error": {
                "code": "unknown_tool",
                "message": f"未注册工具: {tool_name}",
            },
        }

    try:
        tool_func = TOOL_REGISTRY[tool_name]
        return tool_func(**arguments)
    except TypeError as exc:
        return {
            "ok": False,
            "data": None,
            "error": {
                "code": "invalid_arguments",
                "message": str(exc),
            },
        }
    except Exception as exc:
        return {
            "ok": False,
            "data": None,
            "error": {
                "code": "tool_runtime_error",
                "message": str(exc),
            },
        }


def run_demo(user_input: str) -> Dict[str, Any]:
    """运行一次完整 Tool Calling 流程，并返回方便观察的结构化结果。"""
    tool_call = select_tool_call(user_input)
    tool_result = execute_tool_call(tool_call)

    return {
        "user_input": user_input,
        "tool_call": tool_call,
        "tool_result": tool_result,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Day 3 Tool Calling demo")
    parser.add_argument(
        "query",
        nargs="?",
        default="帮我看一下 sales 数据集有哪些字段",
        help="用户输入，用于演示模型如何选择工具",
    )
    parser.add_argument(
        "--show-schemas",
        action="store_true",
        help="打印 tool schemas，观察模型能看到的工具说明",
    )
    args = parser.parse_args()
    print(args)
    if args.show_schemas:
        print(json.dumps(TOOL_SCHEMAS, ensure_ascii=False, indent=2))
        return

    result = run_demo(args.query)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
