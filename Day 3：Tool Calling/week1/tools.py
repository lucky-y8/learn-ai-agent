"""
Day 3 Tool Calling - Superset / BI mock tools

这份文件只负责定义“工具本身”：
1. 每个工具接收结构化参数。
2. 每个工具返回结构化结果。
3. 工具失败时返回 error 信息，而不是让程序直接崩掉。

后面的 tool_calling_demo.py 会演示“模型选择工具 -> 代码执行工具 -> 返回观察结果”。
"""

from __future__ import annotations

import re
from typing import Any, Dict, List


# mock 数据集元数据，模拟 Superset 里 dataset / chart 会依赖的字段信息。
DATASETS: Dict[str, Dict[str, List[str]]] = {
    "sales": {
        "columns": ["ds", "region", "revenue", "quantity"],
        "metrics": ["sum_revenue", "avg_order_value", "total_quantity"],
    },
    "users": {
        "columns": ["ds", "country", "new_users", "active_users"],
        "metrics": ["new_user_count", "active_user_count", "retention_rate"],
    },
    "orders": {
        "columns": ["order_id", "ds", "status", "amount"],
        "metrics": ["order_count", "paid_amount", "refund_amount"],
    },
}


def tool_success(data: Dict[str, Any]) -> Dict[str, Any]:
    """统一成功返回格式，便于 Agent 把结果当成 observation 继续处理。"""
    return {
        "ok": True,
        "data": data,
        "error": None,
    }


def tool_error(message: str, code: str = "tool_error") -> Dict[str, Any]:
    """统一失败返回格式，避免工具异常直接中断 Agent 流程。"""
    return {
        "ok": False,
        "data": None,
        "error": {
            "code": code,
            "message": message,
        },
    }


def get_dataset_columns(dataset_id: str) -> Dict[str, Any]:
    """
    查询数据集字段列表。

    示例：
    get_dataset_columns("sales")
    -> {"ok": true, "data": {"columns": ["ds", "region", "revenue", "quantity"]}}
    """
    dataset = DATASETS.get(dataset_id)
    if not dataset:
        return tool_error(f"未知 dataset_id: {dataset_id}", code="dataset_not_found")

    return tool_success(
        {
            "dataset_id": dataset_id,
            "columns": dataset["columns"],
        }
    )


def get_dataset_metrics(dataset_id: str) -> Dict[str, Any]:
    """查询数据集可用指标列表。"""
    dataset = DATASETS.get(dataset_id)
    if not dataset:
        return tool_error(f"未知 dataset_id: {dataset_id}", code="dataset_not_found")

    return tool_success(
        {
            "dataset_id": dataset_id,
            "metrics": dataset["metrics"],
        }
    )


def validate_sql(sql: str) -> Dict[str, Any]:
    """
    做一个轻量 SQL 安全校验。

    真实生产环境会使用 SQL parser、权限系统和数据库方言校验。
    这里先用 mock 规则表达 Tool Calling 的输入输出契约。
    """
    normalized = sql.strip().lower()

    if not normalized:
        return tool_error("SQL 不能为空", code="empty_sql")

    # 课堂作业里只允许 SELECT 查询，防止 UPDATE / DELETE / DROP 等写操作。
    if not normalized.startswith("select"):
        return tool_success(
            {
                "valid": False,
                "reason": "只允许 SELECT 查询",
                "risk_level": "high",
            }
        )

    # 拦截常见危险关键字。这里是简化版，生产中不能只靠正则。
    dangerous_patterns = [
        r"\binsert\b",
        r"\bupdate\b",
        r"\bdelete\b",
        r"\bdrop\b",
        r"\balter\b",
        r"\btruncate\b",
    ]
    for pattern in dangerous_patterns:
        if re.search(pattern, normalized):
            return tool_success(
                {
                    "valid": False,
                    "reason": f"SQL 包含危险关键字: {pattern.strip('\\b')}",
                    "risk_level": "high",
                }
            )

    # 简单要求必须有 FROM，避免用户只写 select 1 这种不贴合 BI 数据集的查询。
    if " from " not in f" {normalized} ":
        return tool_success(
            {
                "valid": False,
                "reason": "查询缺少 FROM 子句",
                "risk_level": "medium",
            }
        )

    return tool_success(
        {
            "valid": True,
            "reason": "SQL 通过 mock 校验",
            "risk_level": "low",
        }
    )


def recommend_chart_type(columns: List[str]) -> Dict[str, Any]:
    """
    根据字段名称推荐图表类型。

    这是一个很小的启发式规则：
    - 有时间字段和数值字段：折线图。
    - 有类别字段和数值字段：柱状图。
    - 只有类别字段：表格。
    """
    if not columns:
        return tool_error("columns 不能为空", code="empty_columns")

    normalized = [column.lower() for column in columns]
    time_columns = {"ds", "date", "day", "created_at"}
    metric_columns = {
        "revenue",
        "quantity",
        "amount",
        "new_users",
        "active_users",
    }
    category_columns = {"region", "country", "status"}

    has_time = any(column in time_columns for column in normalized)
    has_metric = any(column in metric_columns for column in normalized)
    has_category = any(column in category_columns for column in normalized)

    if has_time and has_metric:
        chart_type = "line"
        reason = "包含时间字段和指标字段，适合观察趋势"
    elif has_category and has_metric:
        chart_type = "bar"
        reason = "包含类别字段和指标字段，适合做分组对比"
    else:
        chart_type = "table"
        reason = "字段结构不够明确，先用表格展示最稳妥"

    return tool_success(
        {
            "chart_type": chart_type,
            "reason": reason,
            "input_columns": columns,
        }
    )


def main() -> None:
    """直接运行本文件时，展示四个工具的最小自测结果。"""
    examples = [
        ("get_dataset_columns", get_dataset_columns("sales")),
        ("get_dataset_metrics", get_dataset_metrics("sales")),
        ("validate_sql", validate_sql("select ds, revenue from sales")),
        ("recommend_chart_type", recommend_chart_type(["ds", "revenue"])),
    ]

    for name, result in examples:
        print(f"{name}: {result}")


if __name__ == "__main__":
    main()
