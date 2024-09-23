"""
@File         : 01_series.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-09-23 22:01:40
@Email        : cuixuanstephen@gmail.com
@Description  : 主要介绍一些 Series 的方法，数据类型的重要性，sum 在字符串上的问题
"""

import numpy as np
import pandas as pd

# np.random.randint(70, 100, size=10)  # [70, 100)
g = np.random.default_rng(0)  # random-number generator object
g.integers(70, 101, 10)  # [70, 101)

s = pd.Series(g.integers(70, 101, 10))
s.index = "Sep Oct Nov Dec Jan Feb Mar Apr May Jun".split()

g = np.random.default_rng(0)
months = "Sep Oct Nov Dec Jan Feb Mar Apr May Jun".split()
s = pd.Series(g.integers(70, 101, 10), index=months)

first_half_average = s["Sep":"Jan"].mean()
second_half_average = s["Feb":"Jun"].mean()
print(f"First half average: {first_half_average}")
print(f"Second half average: {second_half_average}")
print(f"Improvement: {second_half_average - first_half_average}")

# 如果最大值是在两个中如何办？即九月和六月的成绩是一样的
s.sort_values(ascending=False).index[0]
s[s == s.max()].index[0]
s.idxmax()

s.sort_values(ascending=False)[:5]

s.round(-1)

s = pd.Series("abcd efgh ijkl".split())
s.sum()

s = pd.Series("1234 5678 9012".split())
s.sum()

s = pd.Series("10 20 30".split())
s.dtype
