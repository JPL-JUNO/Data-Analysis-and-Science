"""
@File         : EXERCISE 4 Descriptive statistics.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-09-25 22:44:52
@Email        : cuixuanstephen@gmail.com
@Description  : 描述统计
"""

import pandas as pd
import numpy as np

g = np.random.default_rng(0)
s = pd.Series(g.normal(0, 100, 100_000))
