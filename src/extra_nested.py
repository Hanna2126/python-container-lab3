# -*- coding: utf-8 -*-
"""拓展任务：嵌套列表去重。

内层 list 不可哈希 → 转 tuple 建集合去重 → 需要时再转回 list。
"""
from __future__ import annotations

NEST = [[1, 2], [3, 4], [1, 2], [5, 6]]


def dedupe_nested(nest: list[list[int]]) -> list[list[int]]:
    """按“第一次出现”的顺序去重嵌套列表。"""
    seen = set()
    out: list[list[int]] = []
    for item in nest:
        key = tuple(item)          # list 不可哈希，先转成元组
        if key not in seen:
            seen.add(key)
            out.append(item)       # 输出仍保留 list 形态
    return out


def run() -> dict:
    print("=" * 62)
    print("拓展　嵌套列表去重")
    print("=" * 62)
    print(f"原始嵌套列表：{NEST}")

    try:
        hash(NEST[0])
        print("直接 hash 内层 list：居然成功了？")
    except TypeError as exc:
        print(f"直接 hash 内层 list → TypeError: {exc}")
        print("原因：list 可变、不可哈希，不能直接放进 set 做去重键。")

    result = dedupe_nested(NEST)
    print(f"\n先转 tuple 再去重，结果：{result}")
    print(f"去重前 {len(NEST)} 组，去重后 {len(result)} 组。")

    # 只想要集合形式的写法
    as_tuples = {tuple(x) for x in NEST}
    print(f"如果只需要集合结果：{{tuple(x) for x in NEST}} → {as_tuples}")
    return {"result": result, "tuples": as_tuples}


if __name__ == "__main__":
    run()
