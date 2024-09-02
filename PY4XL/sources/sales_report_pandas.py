"""
@File         : ales_report_pandas.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-09-02 09:27:19
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

from pathlib import Path
import pandas as pd

# 文件的目录
# 在 Jupyter 笔记本中运行这段脚本，那么需要将这行代码替换成
# this_dir = Path(".").resolve()，用点来表示当前目录。
this_dir = Path(__file__).resolve().parent.parent

# 从 sales_data 的所有子文件夹中读取 Excel 文件
parts = []
for path in (this_dir / "sales_data").rglob("*.xls*"):
    # [!~$]*.xls*。这样就可以忽略临时的 Excel 文件（文件名以 ~$ 开头）。
    print(f"Reading {path.name}")
    part = pd.read_excel(path, index_col="transaction_id")
    parts.append(part)

df = pd.concat(parts)

pivot = pd.pivot_table(
    df, index="transaction_date", columns="store", values="amount", aggfunc="sum"
)

summary = pivot.resample("M").sum()
summary.to_excel(this_dir / "res/sales_report_pandas.xlsx")
