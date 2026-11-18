# -*- coding: utf-8 -*-
"""任务3：集合全部运算 + 集合推导式。"""
from __future__ import annotations

A = {2, 4, 6, 8, 10, 12}
B = {3, 6, 9, 12, 15}


def run() -> dict:
    print("=" * 62)
    print("任务3　集合运算与集合推导式")
    print("=" * 62)

    inter = A & B
    union = A | B
    a_minus_b = A - B
    b_minus_a = B - A
    sym = A ^ B

    print(f"A = {A}")
    print(f"B = {B}")
    print(f"交集  A & B  = {sorted(inter)}  → 两门都满足的元素")
    print(f"并集  A | B  = {sorted(union)}  → 出现在 A 或 B 里的全部元素")
    print(f"差集  A - B  = {sorted(a_minus_b)}  → 在 A 中但不在 B 中")
    print(f"差集  B - A  = {sorted(b_minus_a)}  → 在 B 中但不在 A 中")
    print(f"对称差 A ^ B = {sorted(sym)}  → 只属于其中一边的元素（= 并集 - 交集）")

    comp = {x for x in range(1, 31) if x % 4 == 0}
    print(f"\n集合推导式：{{x for x in range(1, 31) if x % 4 == 0}} → {sorted(comp)}")

    # 用另一种写法交叉验证对称差
    check = (A | B) - (A & B)
    print(f"交叉验证： (A|B) - (A&B) = {sorted(check)}，与 A ^ B 相同 → {check == sym}")

    return {
        "inter": inter,
        "union": union,
        "a_minus_b": a_minus_b,
        "b_minus_a": b_minus_a,
        "sym": sym,
        "comp": comp,
    }


if __name__ == "__main__":
    run()
