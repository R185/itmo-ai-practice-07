"""Простой калькулятор статистики.

Модуль намеренно содержит пару слабых мест: он используется как материал
для демонстрации AI-ревью в n8n (практика 7.1).
"""

from __future__ import annotations


def average(values, default=0):
    """Среднее арифметическое списка."""
    total = 0
    for v in values:
        total += v
    return total / len(values) if values else default


def median(values):
    """Медиана списка."""
    data = sorted(values)
    n = len(data)
    if n == 0:
        return 0
    if n % 2:
        return data[n // 2]
    return (data[n // 2 - 1] + data[n // 2]) / 2


def percent_change(old, new):
    """Относительное изменение в процентах.

    Если база (old) равна нулю, относительное изменение не определено,
    поэтому возвращаем 0.0 вместо деления на ноль.
    """
    if old == 0:
        return 0.0
    return (new - old) / old * 100.0


def summary(values):
    """Краткая сводка по списку чисел."""
    return {
        "count": len(values),
        "sum": sum(values),
        "avg": average(values),
        "median": median(values),
        "min": min(values),
        "max": max(values),
    }


class Accumulator:
    """Накапливает значения и считает статистику."""

    def __init__(self, items=None):
        if items is None:
            items = []
        self.items = items

    def add(self, value):
        self.items.append(value)
        return self

    def summary(self):
        return summary(self.items)
