"""
@File         : exercise_3_counting_tens_digits.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-09-25 22:16:20
@Email        : cuixuanstephen@gmail.com
@Description  : 计算十位数字
"""

import pandas as pd
import numpy as np

g = np.random.default_rng(0)
s = pd.Series(g.integers(0, 100, 10))

(s / 10).astype(np.int8)

s = pd.Series(g.integers(0, 10_000, 10))
s.astype(str).str.get(-2).fillna("0").astype(np.int8)

s = pd.Series(np.random.rand(10) * 1000)
s[s.astype(np.int64) % 2 == 0]
