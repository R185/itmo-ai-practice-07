import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from calc import Accumulator, average, median, percent_change, stdev, summary  # noqa: E402


def test_average_basic():
    assert average([1, 2, 3]) == 2


def test_average_empty():
    assert average([]) == 0


def test_median_odd():
    assert median([3, 1, 2]) == 2


def test_median_even():
    assert median([1, 2, 3, 4]) == 2.5


def test_percent_change():
    assert percent_change(10, 12) == 20


def test_percent_change_zero_old():
    assert percent_change(0, 5) == float("inf")


def test_stdev_basic():
    assert round(stdev([2, 4, 4, 4, 5, 5, 7, 9]), 3) == 2.0


def test_stdev_constant():
    assert stdev([3, 3, 3]) == 0


def test_summary_keys():
    s = summary([1, 2, 3])
    assert s["count"] == 3
    assert s["sum"] == 6
    assert "stdev" in s


def test_accumulator_isolated():
    a = Accumulator()
    b = Accumulator()
    a.add(1)
    assert b.items == [], "аккумуляторы не должны делить список"
