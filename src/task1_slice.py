# -*- coding: utf-8 -*-
"""任务1：切片删除深度探究。

先给出预判，再真实执行，最后逐条核对“预判 vs 实际”。
"""
from __future__ import annotations


def delete_by_slice(start_list: list[int], sl: slice) -> list[int]:
    """返回执行 del start_list[sl] 之后的列表（不修改入参）。"""
    ls = start_list.copy()
    del ls[sl]
    return ls


def remove_even_while_iterating(nums: list[int]) -> list[int]:
    """复现“边遍历边删除”的经典 bug。"""
    ls = nums.copy()
    for i in ls:
        if i % 2 == 0:
            ls.remove(i)
    return ls


def remove_even_safely(nums: list[int]) -> list[int]:
    """安全写法：不在原列表上边遍历边删，而是用推导式生成新列表。"""
    return [x for x in nums if x % 2 != 0]


def run() -> dict:
    print("=" * 62)
    print("任务1　切片删除深度探究")
    print("=" * 62)

    base = list(range(10))
    results: dict[str, list[int]] = {}

    # 1) del ls[::3]
    predicted1 = [1, 2, 4, 5, 7, 8]
    actual1 = delete_by_slice(base, slice(None, None, 3))
    results["ls1"] = actual1
    print(f"[1] del ls1[::3]")
    print(f"    预判：{predicted1}")
    print(f"    实际：{actual1}")
    print(f"    结论：{'一致' if predicted1 == actual1 else '不一致'}")
    print("    原因：步长 3 从索引 0 开始取 0、3、6、9，删除后剩 1、2、4、5、7、8。")

    # 2) del ls[1::3]
    predicted2 = [0, 2, 3, 5, 6, 8, 9]
    actual2 = delete_by_slice(base, slice(1, None, 3))
    results["ls2"] = actual2
    print(f"[2] del ls2[1::3]")
    print(f"    预判：{predicted2}")
    print(f"    实际：{actual2}")
    print(f"    结论：{'一致' if predicted2 == actual2 else '不一致'}")
    print("    原因：起点 1，步长 3 取 1、4、7；起点变了，删掉的元素也跟着平移。")

    # 3) del ls[::-2]：负步长
    predicted3 = [0, 2, 4]
    actual3 = delete_by_slice(list(range(6)), slice(None, None, -2))
    results["ls3"] = actual3
    print(f"[3] del ls3[::-2]（负步长）")
    print(f"    预判：{predicted3}")
    print(f"    实际：{actual3}")
    print(f"    结论：{'一致' if predicted3 == actual3 else '不一致'}")
    print("    原因：负步长从末尾开始，取索引 5、3、1，删除后剩 0、2、4。")

    # 4) 循环里 remove
    predicted4 = [1, 3, 5]
    actual4 = remove_even_while_iterating([1, 2, 3, 4, 5, 6])
    results["ls4"] = actual4
    print(f"[4] for 循环中 ls4.remove(i) 删除偶数")
    print(f"    预判：{predicted4}")
    print(f"    实际：{actual4}")
    print(f"    结论：{'一致' if predicted4 == actual4 else '不一致'}")
    print("    说明：这组数据的结果“看起来对”，但过程并不可靠：")
    print("          remove 让后面的元素整体左移，而迭代器下标照旧 +1，")
    print("          一旦被删元素的后面紧跟另一个待删元素，它就被跳过。")

    # 用两个反例暴露 bug
    counter1 = remove_even_while_iterating([2, 4, 6])
    counter2 = remove_even_while_iterating([2, 2, 2, 3])
    print(f"    反例1：对 [2, 4, 6] 同法删除 → {counter1}（4 被跳过，没删干净）")
    print(f"    反例2：对 [2, 2, 2, 3] 同法删除 → {counter2}（还剩一个 2）")
    print(f"    安全写法：[x for x in nums if x % 2 != 0] → "
          f"{remove_even_safely([1, 2, 3, 4, 5, 6])}")

    # 验证“切片是一次性按下标算好的”
    demo = list(range(10))
    del demo[1:9:2]  # 删索引 1、3、5、7
    print(f"\n    再加一组：对 [0..9] 执行 del demo[1:9:2]，结果 {demo}")
    print("    说明切片先按原列表下标算出待删集合，再一次性删除，不是边删边重新取下标。")
    return results


if __name__ == "__main__":
    run()
