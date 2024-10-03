"""
@File         : exercise_5_monday_temperatures.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-10-03 11:07:06
@Email        : cuixuanstephen@gmail.com
@Description  : 周一气温
"""

import pandas as pd
import numpy as np

g = np.random.default_rng(0)
g.normal(20, 5, 28)
days = "Sun Mon Tue Wed Thu Fri Sat".split()
s = pd.Series(g.normal(20, 5, 28), index=days * 4).round().astype(np.int8)
