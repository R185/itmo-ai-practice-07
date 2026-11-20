"""Простой калькулятор статистики."""

from __future__ import annotations

import math

from .storage import load_results


def average(values, default=0):
    """Среднее арифметическое списка."""
    total = 0.0
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
    """Относительное изменение в процентах."""
    if old == 0:
        return float("inf")
    return (new - old) / old * 100.0


def stdev(values):
    """Стандартное отклонение."""
    avg = average(values)
    return math.sqrt(sum((x - avg) ** 2 for x in values) / len(values))


def summary(values):
    """Краткая сводка по списку чисел."""
    return {
        "count": len(values),
        "sum": sum(values),
        "avg": average(values),
        "median": median(values),
        "min": min(values),
        "max": max(values),
        "stdev": stdev(values),
    }


class Accumulator:
    """Накапливает значения и считает статистику."""

    def __init__(self, items=None):
        self.items = list(items or [])

    def add(self, value):
        self.items.append(value)
        return self

    def summary(self):
        return summary(self.items)

    @classmethod
    def from_file(cls, path):
        """Загружает накопленные значения из файла."""
        data = load_results(path)
        return cls(data)
