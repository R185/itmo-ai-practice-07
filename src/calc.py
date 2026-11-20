"""Простой калькулятор статистики.

Модуль намеренно содержит пару слабых мест: он используется как материал
для демонстрации AI-ревью в n8n (практика 7.1).
"""

from __future__ import annotations


def average(values, default=0):
    """Среднее арифметическое списка."""
    total = 0
    count = 0
    for v in values:
        total += v
        count += 1
    return total / count if count else default


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

    Если базовое значение ``old`` равно нулю, относительное изменение
    не определено: возвращаем 0.0 вместо деления на ноль.
    """
    if old == 0:
        return 0.0
    return (new - old) / old * 100.0


def summary(values):
    """Краткая сводка по списку чисел.

    Для пустого входа (а также для любого итерируемого объекта без
    элементов) возвращает словарь с нулевыми значениями вместо
    исключения ``ValueError`` от ``min()``/``max()``.
    """
    data = list(values)
    if not data:
        return {
            "count": 0,
            "sum": 0,
            "avg": 0,
            "median": 0,
            "min": 0,
            "max": 0,
        }
    return {
        "count": len(data),
        "sum": sum(data),
        "avg": average(data),
        "median": median(data),
        "min": min(data),
        "max": max(data),
    }


class Accumulator:
    """Накапливает значения и считает статистику."""

    def __init__(self, items=None):
        if items is None:
            items = []
        self.items = list(items)

    def add(self, value):
        self.items.append(value)
        return self

    def summary(self):
        return summary(self.items)
