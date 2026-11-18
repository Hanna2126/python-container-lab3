# -*- coding: utf-8 -*-
"""覆盖五个任务与拓展的单元测试。"""
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src import extra_nested, task1_slice, task2_hash, task3_set_ops, task4_dedupe, task5_courses  # noqa: E402


# ---------- 任务1 ----------
def test_slice_step3():
    assert task1_slice.delete_by_slice(list(range(10)), slice(None, None, 3)) == [1, 2, 4, 5, 7, 8]


def test_slice_start1_step3():
    assert task1_slice.delete_by_slice(list(range(10)), slice(1, None, 3)) == [0, 2, 3, 5, 6, 8, 9]


def test_slice_negative_step():
    assert task1_slice.delete_by_slice(list(range(6)), slice(None, None, -2)) == [0, 2, 4]


def test_remove_while_iterating_leaves_one_even():
    assert task1_slice.remove_even_while_iterating([1, 2, 3, 4, 5, 6]) == [1, 3, 5]


def test_remove_while_iterating_misses_consecutive_even():
    assert task1_slice.remove_even_while_iterating([2, 4, 6]) == [4]
    assert task1_slice.remove_even_while_iterating([2, 2, 2, 3]) == [2, 3]


def test_safe_removal_by_comprehension():
    assert task1_slice.remove_even_safely([1, 2, 3, 4, 5, 6]) == [1, 3, 5]


# ---------- 任务2 ----------
def test_tuple_of_ints_hashable():
    assert hash((1, 2, 3)) is not None


def test_tuple_with_list_unhashable():
    with pytest.raises(TypeError):
        hash((1, [2, 3]))


def test_list_unhashable():
    with pytest.raises(TypeError):
        hash([1, 2])


def test_frozenset_hashable_and_nestable():
    fs = frozenset({1, 2})
    assert hash(fs) is not None
    s = {fs}
    assert fs in s


def test_set_unhashable():
    with pytest.raises(TypeError):
        hash({1, 2})


# ---------- 任务3 ----------
def test_set_operations():
    A, B = task3_set_ops.A, task3_set_ops.B
    assert A & B == {6, 12}
    assert A | B == {2, 3, 4, 6, 8, 9, 10, 12, 15}
    assert A - B == {2, 4, 8, 10}
    assert B - A == {3, 9, 15}
    assert A ^ B == {2, 3, 4, 8, 9, 10, 15}


def test_set_comprehension_multiples_of_4():
    assert {x for x in range(1, 31) if x % 4 == 0} == {4, 8, 12, 16, 20, 24, 28}


# ---------- 任务4 ----------
def test_set_dedupe_loses_order_but_unique():
    out = task4_dedupe.dedupe_by_set(task4_dedupe.DATA)
    assert sorted(out) == [1, 2, 3, 5, 7, 9]
    assert len(out) == len(set(task4_dedupe.DATA))


def test_loop_dedupe_keeps_order():
    assert task4_dedupe.dedupe_keep_order_loop(task4_dedupe.DATA) == [5, 2, 7, 9, 3, 1]


def test_dict_dedupe_keeps_order():
    assert task4_dedupe.dedupe_keep_order_dict(task4_dedupe.DATA) == [5, 2, 7, 9, 3, 1]


# ---------- 任务5 ----------
def test_unique_lists_keep_order():
    r = task5_courses.run.__globals__["unique_keep_order"]([101, 103, 105, 107, 109, 103, 101])
    assert r == [101, 103, 105, 107, 109]


def test_intersection():
    r = task5_courses.run()
    assert r["both"] == {107, 109}


def test_symmetric_difference():
    r = task5_courses.run()
    assert r["only_one"] == {101, 102, 103, 104, 105, 106, 108}


def test_only_class1():
    r = task5_courses.run()
    assert r["only_c1"] == {101, 103, 105}


def test_intersection_tuple_hashable():
    r = task5_courses.run()
    t = r["tuple"]
    assert isinstance(t, tuple)
    assert hash(t) is not None
    assert t in {t}


# ---------- 拓展 ----------
def test_nested_dedupe():
    r = extra_nested.run()
    assert r["result"] == [[1, 2], [3, 4], [5, 6]]
    assert r["tuples"] == {(1, 2), (3, 4), (5, 6)}
