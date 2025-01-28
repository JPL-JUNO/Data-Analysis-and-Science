"""
@File         : credit-approval-dataset.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2025-01-28 16:49:04
@Email        : cuixuanstephen@gmail.com
@Description  : 生成一份文件，主要为了演示 Encoding Categorical Variables，与填充缺失值的文件稍微有些不一样
"""

import pandas as pd
import numpy as np

data = pd.read_csv("DATA/crx.data", header=None)
var_names = [f"A{s}" for s in range(1, 17)]
data.columns = var_names

data = data.replace("?", np.nan)
data["A2"] = data["A2"].astype("float")
data["A14"] = data["A14"].astype("float")

data["A16"] = data["A16"].map({"+": 1, "-": 0})
data.rename(columns={"A16": "target"}, inplace=True)

cat_cols = [c for c in data.columns if data[c].dtypes == "O"]
num_cols = [c for c in data.columns if data[c].dtypes != "O"]

data[num_cols] = data[num_cols].fillna(0)
data[cat_cols] = data[cat_cols].fillna("Missing")

data.to_csv(
    "NOTEBOOKS/CH02_Encoding_Categorical_Variables/credit_approval_uci.csv",
    index=False,
)
