# -*- coding: utf-8 -*-
"""任务4：去重算法对比（集合去重 vs 保序去重）。

三种写法：list(set(data))、手写循环、dict.fromkeys；顺带做一次 20 万条数据的耗时对比。
"""
from __future__ import annotations

import random
import time

DATA = [5, 2, 7, 2, 5, 9, 7, 3, 9, 1]


def dedupe_by_set(data: list[int]) -> list[int]:
    """集合去重：最简单，但丢顺序。"""
    return list(set(data))


def dedupe_keep_order_loop(data: list[int]) -> list[int]:
    """手写保序去重：新列表里没有才 append。"""
    out: list[int] = []
    for item in data:
        if item not in out:
            out.append(item)
    return out


def dedupe_keep_order_dict(data: list[int]) -> list[int]:
    """字典键去重：dict.fromkeys 天然保序（3.7 起字典保持插入顺序）。"""
    return list(dict.fromkeys(data))


def benchmark(n: int = 200_000) -> list[tuple[str, float]]:
    """生成 n 个随机整数，比较三种方法的耗时。"""
    rng = random.Random(20261118)
    data = [rng.randint(1, 5000) for _ in range(n)]
    timings: list[tuple[str, float]] = []
    for name, fn in (
        ("list(set(data))", dedupe_by_set),
        ("手写循环", dedupe_keep_order_loop),
        ("dict.fromkeys", dedupe_keep_order_dict),
    ):
        t0 = time.perf_counter()
        fn(data)
        timings.append((name, (time.perf_counter() - t0) * 1000))
    return timings


def run() -> dict:
    print("=" * 62)
    print("任务4　去重算法对比")
    print("=" * 62)

    print(f"原始数据：{DATA}")
    res1 = dedupe_by_set(DATA)
    res2 = dedupe_keep_order_loop(DATA)
    res3 = dedupe_keep_order_dict(DATA)
    print(f"方案1 list(set(data))      → {res1}   （顺序被打乱）")
    print("      注意：这一组恰好看着像升序，是因为小整数 hash(i)==i，")
    print("      集合按哈希槽位遍历；换成字符串或大整数，顺序就未必好看。")
    print(f"方案2 手写循环保序          → {res2}")
    print(f"方案3 list(dict.fromkeys)  → {res3}   （保序，写法最短）")
    print(f"方案2 与方案3 结果一致：{res2 == res3}")
    print("结论：集合去重只保证“不重复”，不保证“顺序”；要保序就用字典键或手写判断。")

    print("\n20 万条随机整数的耗时对比：")
    for name, ms in benchmark():
        print(f"  {name:<16}{ms:8.1f} ms")
    print("说明：list(set()) 最快但丢顺序；dict.fromkeys 兼顾速度与顺序；")
    print("      手写循环里 `item not in out` 是 O(n) 扫描，数据量大时明显变慢（O(n²)）。")

    return {"set": res1, "loop": res2, "dict": res3}


if __name__ == "__main__":
    run()
