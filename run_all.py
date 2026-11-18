# -*- coding: utf-8 -*-
"""一键运行全部任务：python run_all.py"""
from __future__ import annotations

import platform
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from src import extra_nested, task1_slice, task2_hash, task3_set_ops, task4_dedupe, task5_courses  # noqa: E402


def main() -> None:
    print("Python 列表、元组、集合　实验实训")
    print(f"Python {sys.version.split()[0]} | {platform.system()} {platform.release()}")
    print()

    results = {}
    results["task1"] = task1_slice.run()
    print()
    results["task2"] = task2_hash.run()
    print()
    results["task3"] = task3_set_ops.run()
    print()
    results["task4"] = task4_dedupe.run()
    print()
    results["task5"] = task5_courses.run()
    print()
    results["extra"] = extra_nested.run()

    print()
    print("=" * 62)
    print("全部任务执行完毕")
    print("=" * 62)


if __name__ == "__main__":
    main()
