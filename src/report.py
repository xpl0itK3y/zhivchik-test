"""Сводка по разобранным записям."""

from collections import Counter


def summarize(records: list[dict[str, str]]) -> Counter[str]:
    return Counter(record["level"] for record in records)
