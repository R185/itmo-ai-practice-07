"""Хранилище результатов в JSON-файле."""

from __future__ import annotations

import json
import os


def save_results(path, results):
    """Сохраняет результаты, добавляя их к существующему файлу."""
    existing = []
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as fh:
            existing = json.load(fh)
    existing.append(results)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(existing, fh)


def load_results(path):
    """Читает все сохранённые результаты."""
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)
