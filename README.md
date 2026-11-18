# Python 容器实验（列表 / 元组 / 集合）

Python 程序设计课程实验：切片删除、可哈希判定、集合运算与保序去重。只用标准库，无第三方依赖。

实验博客：[实验 3：列表、元组、集合——那些“看起来对、其实靠运气”的写法](blog/lab3-containers.md)

## 任务清单

| 编号 | 内容 | 实现 |
| --- | --- | --- |
| 任务 1 | 切片删除深度探究（`del ls[::3]`、`del ls[1::3]`、`del ls[::-2]`、循环删偶数） | `src/task1_slice.py` |
| 任务 2 | 嵌套容器与可哈希辨析（5 组测试） | `src/task2_hash.py` |
| 任务 3 | 集合交并差对称差 + 集合推导式 | `src/task3_set_ops.py` |
| 任务 4 | 去重对比（集合去重 / 手写保序 / dict.fromkeys）+ 20 万条耗时 | `src/task4_dedupe.py` |
| 任务 5 | 选课名单综合题（保序去重、交集、对称差、差集、转元组） | `src/task5_courses.py` |
| 拓展 | 嵌套列表去重（list → tuple → set） | `src/extra_nested.py` |

## 快速开始

```bash
python run_all.py            # 一键运行全部任务
python -m src.task1_slice    # 单独运行某个任务
python -m pytest tests -v    # 22 条单元测试
```

## 实测结果

| 操作 | 结果 |
| --- | --- |
| `del ls[::3]` | `[1, 2, 4, 5, 7, 8]` |
| `del ls[1::3]` | `[0, 2, 3, 5, 6, 8, 9]` |
| `del ls[::-2]` | `[0, 2, 4]` |
| 循环删偶数 `[1..6]` | `[1, 3, 5]`（碰巧正确，反例 `[2,4,6]` → `[4]`） |
| 集合去重 | `[1, 2, 3, 5, 7, 9]` |
| 保序去重 | `[5, 2, 7, 9, 3, 1]` |
| 同时选两门 | `{107, 109}` |
| 只选一门 | `{101, 102, 103, 104, 105, 106, 108}` |
| 只选 1 班 | `{101, 103, 105}` |

## 目录结构

```text
python-container-lab3/
├─ run_all.py                 # 统一入口
├─ src/                       # 6 个任务模块
├─ tests/test_containers.py   # 22 条 pytest 用例
├─ 截图/                      # 8 张真实运行截图
├─ blog/                      # 博客与配图
├─ logs/                      # 运行与测试日志
├─ 实验报告.docx
├─ 验证记录.md
└─ README.md
```

## 环境

- Windows 11
- Python 3.13.18
- pytest 9.2.0
- 截图全部来自本机 Windows PowerShell 真实运行
