# -*- coding: utf-8 -*-
"""任务2：嵌套容器与可哈希深度辨析。

逐个尝试把不同类型的对象放进集合，记录成功或报错，并给出理由。
"""
from __future__ import annotations

REASONS = {
    "tuple_ints": "元组本身不可变，且三个元素都是 int（可哈希），整体可哈希。",
    "tuple_with_list": "元组里含有 list，list 可变 → hash 值不固定 → 整个元组不可哈希。",
    "list": "list 是可变对象，内容一变哈希值就变，Python 不允许其作为集合元素。",
    "frozenset": "frozenset 是冻结集合，创建后内容不可变，哈希值固定，可以放进集合。",
    "set": "普通 set 可变，本身不可哈希，因此既不能放进 set 也不能当 dict 的键。",
}


def try_add(target: set, value, key: str) -> tuple[bool, str]:
    """尝试把 value 加入集合，返回 (是否成功, 说明)。"""
    try:
        target.add(value)
        return True, "成功加入"
    except TypeError as exc:
        return False, f"{type(exc).__name__}: {exc}"


def run() -> dict:
    print("=" * 62)
    print("任务2　嵌套容器与可哈希深度辨析")
    print("=" * 62)

    cases = [
        ("tuple_ints", "s.add((1, 2, 3))", (1, 2, 3)),
        ("tuple_with_list", "s.add((1, [2, 3]))", (1, [2, 3])),
        ("list", "s.add([1, 2])", [1, 2]),
        ("frozenset", "s.add(frozenset({1, 2}))", frozenset({1, 2})),
        ("set", "s.add({1, 2})", {1, 2}),
    ]

    s: set = set()
    log: dict[str, bool] = {}
    for key, expr, value in cases:
        ok, msg = try_add(s, value, key)
        log[key] = ok
        mark = "OK  " if ok else "FAIL"
        print(f"[{mark}] {expr}")
        print(f"       结果：{msg}")
        print(f"       理由：{REASONS[key]}")

    print(f"\n最终集合内容：{s}")
    print("集合里只有可哈希的两类对象：纯 int 元组、frozenset。")

    # 演示“集合里放集合”的正确做法
    nested = {frozenset({1, 2}), frozenset({2, 3}), frozenset()}
    print(f"\n需要“集合套集合”时的写法：{{frozenset(...), frozenset(...)}} → {nested}")
    print("注意：frozenset() 空集合与 {} 不同，{} 是空字典。")
    return log


if __name__ == "__main__":
    run()
