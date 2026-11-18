# -*- coding: utf-8 -*-
"""任务5：综合设计题（两份选课名单）。

步骤对应题目 ①～⑤，每一步都打印文字说明。
"""
from __future__ import annotations

CLASS1 = [101, 103, 105, 107, 109, 103, 101]
CLASS2 = [102, 104, 106, 108, 109, 107, 102]


def unique_keep_order(data: list[int]) -> list[int]:
    return list(dict.fromkeys(data))


def run() -> dict:
    print("=" * 62)
    print("任务5　综合设计题：两份选课名单")
    print("=" * 62)
    print(f"1 班原始名单：{CLASS1}")
    print(f"2 班原始名单：{CLASS2}")

    # ① 保序去重
    u1 = unique_keep_order(CLASS1)
    u2 = unique_keep_order(CLASS2)
    print(f"\n① 不重复名单（保序）")
    print(f"   1 班：{u1}  （原有 {len(CLASS1)} 条，去重后 {len(u1)} 人）")
    print(f"   2 班：{u2}  （原有 {len(CLASS2)} 条，去重后 {len(u2)} 人）")
    print("   说明：名单里有重复报名，用 dict.fromkeys 保留第一次出现的顺序。")

    s1, s2 = set(u1), set(u2)

    # ② 交集
    both = s1 & s2
    both_sorted = sorted(both)
    print(f"\n② 同时选两门课的学生")
    print(f"   s1 & s2 = {both_sorted}  （共 {len(both)} 人）")
    print("   说明：同时出现在两个集合里，就是交集。")

    # ③ 对称差
    only_one = s1 ^ s2
    print(f"\n③ 只选其中一门课的学生（对称差）")
    print(f"   s1.symmetric_difference(s2) = {sorted(only_one)}  （共 {len(only_one)} 人）")
    print("   等价的运算符写法是 s1 ^ s2；它把“两边都有”的 107、109 排除，")
    print("   只留下只出现过一次的人。")

    # ④ 差集
    only_c1 = s1 - s2
    print(f"\n④ 选了 1 班但没选 2 班的学生")
    print(f"   s1 - s2 = {sorted(only_c1)}  （共 {len(only_c1)} 人）")
    print("   说明：差集是“在左边、不在右边”，方向不能反。")

    # ⑤ 转元组
    t_both = tuple(both_sorted)
    print(f"\n⑤ 交集结果转元组")
    print(f"   tuple(sorted(s1 & s2)) = {t_both}，长度 {len(t_both)}")
    print("   说明：交集里都是 int，int 可哈希，所以 tuple 也可哈希，")
    print("         换成元组后既不可变、又能继续放进集合或当字典键。")
    test_set = {t_both, ("x", 1)}
    print(f"   验证：{{t_both, ('x', 1)}} 可以正常创建 → {test_set}")

    # 补充：姓名映射，便于阅读
    names = {101: "张一", 103: "李三", 105: "王五", 107: "赵七",
             109: "钱九", 102: "孙二", 104: "周四", 106: "吴六", 108: "郑八"}
    print("\n补充：把编号换成姓名看一遍")
    print("   同时选两门：" + "、".join(names[i] for i in both_sorted))
    print("   只选 1 班：" + "、".join(names[i] for i in sorted(only_c1)))

    return {
        "u1": u1,
        "u2": u2,
        "both": both,
        "only_one": only_one,
        "only_c1": only_c1,
        "tuple": t_both,
    }


if __name__ == "__main__":
    run()
