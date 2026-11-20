"""Хранилище результатов в JSON-файле."""

from __future__ import annotations

import json
import os
import tempfile


def save_results(path, results):
    """Сохраняет результаты атомарно, добавляя их к существующему файлу."""
    existing = []
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as fh:
                existing = json.load(fh)
        except json.JSONDecodeError:
            existing = []
    existing.append(results)

    directory = os.path.dirname(os.path.abspath(path))
    fd, tmp_path = tempfile.mkstemp(dir=directory, suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        json.dump(existing, fh, ensure_ascii=False, indent=2)
    os.replace(tmp_path, path)


def load_results(path):
    """Читает все сохранённые результаты."""
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def count_by_key(path, key):
    """Считает, сколько раз встречается значение ключа в сохранённых записях."""
    total = {}
    for row in load_results(path):
        value = row[key]
        total[value] = total.get(value, 0) + 1
    return total
