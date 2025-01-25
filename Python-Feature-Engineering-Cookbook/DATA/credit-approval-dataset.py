"""
@File         : credit-approval-dataset.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2025-01-25 12:25:38
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import random
import numpy as np
import pandas as pd

data = pd.read_csv("DATA/crx.data", header=None)

varnames = [f"A{s}" for s in range(1, 17)]
data.columns = varnames

data = data.replace("?", np.nan)
data = data.assign(A2=data["A2"].astype(float), A14=data["A14"].astype(float))

data["A16"] = data["A16"].map({"+": 1, "-": 0})
data = data.rename(columns={"A16": "target"})

random.seed(9001)

var_list = ["A3", "A8", "A9", "A10"]
for i in range(4):
    values = list(set([random.randint(i, len(data)) for i in range(0, 100)]))
    data.loc[values, var_list] = np.nan


data.to_csv("DATA/credit_approval_uci.csv", index=False)
