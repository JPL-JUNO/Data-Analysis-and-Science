"""
@File         : exercise_2_scaling_test_scores.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-09-24 22:40:43
@Email        : cuixuanstephen@gmail.com
@Description  : 缩放测试分数
"""

import pandas as pd
import numpy as np

s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series([100, 200, 300, 400])

s1 = pd.Series([10, 20, 30, 40], index=list("abcd"))
s2 = pd.Series([100, 200, 300, 400], index=list("dcba"))

g = np.random.default_rng(0)

months = "Sep Oct Nov Dec Jan Feb Mar Apr May Jun".split()
s = pd.Series(g.integers(40, 60, 10), index=months)


s[s > s.mean() + s.std()]

s[(s > s.mean() + s.std()) & (s > s.mean())]

s[(s > (s.mean() - s.std())) & (s < s.mean())]


s[(s < s.mean() - 2 * s.std()) | (s > s.mean() + 2 * s.std())]
