"""
@Description: High-Performance Pandas: eval and query
@Author:Stephen CUI
@Time: 2023-04-06 10:54:35
"""

import numexpr
import numpy as np
import pandas as pd

rng = np.random.default_rng(seed=42)
x = rng.random(1_000_000)
y = rng.random(1_000_000)
mask = (x > .5) & (y < .5)
mask_numexpr = numexpr.evaluate('(x > .5) & (y < .5)')
assert np.all(mask == mask_numexpr)


nrows, ncols = 100_000, 100
df1, df2, df3, df4 = (pd.DataFrame(rng.random(size=(nrows, ncols)))
                      for i in range(4))


assert np.allclose(df1 + df2 + df3 + df4,
                   pd.eval('df1 + df2 + df3 + df4'))

df1, df2, df3, df4, df5 = (pd.DataFrame(rng.integers(0, 1000, size=(100, 3)))
                           for i in range(5))


result1 = -df1 * df2 / (df3 + df4) - df5
result2 = pd.eval('-df1 * df2 / (df3 + df4) - df5')
assert np.allclose(result1, result2)


result1 = (df1 < df2) & (df2 <= df3) & (df3 != df4)
result2 = pd.eval('df1 < df2 <= df3 != df4')
assert np.allclose(result1, result2)


result1 = (df1 < .5) & (df2 < .5) | (df3 < df4)
result2 = pd.eval('(df1 < .5) & (df2 < .5) | (df3 < df4)')
assert np.allclose(result1, result2)

result3 = pd.eval('(df1 < .5) and (df2 < .5) or (df3 < df4)')
assert np.allclose(result1, result3)


result1 = df2.T[0] + df3.iloc[1]
result2 = pd.eval('df2.T[0] + df3.iloc[1]')
assert np.allclose(result1, result2)


df = pd.DataFrame(rng.random(size=(1000, 3)), columns=['A', 'B', 'C'])
df.head()

result1 = (df['A'] + df['B']) / (df['C'] - 1)
result2 = pd.eval('(df.A + df.B) / (df.C - 1)')
assert np.allclose(result1, result2)


result3 = df.eval('(A + B) / (C - 1)')
assert np.allclose(result1, result3)


df.eval('D = (A + B) / C', inplace=True)


df.eval('D = (A - B) / C', inplace=True)


column_mean = df.mean(axis=1)
result1 = df['A'] + column_mean
result2 = df.eval('A + @column_mean')
assert np.allclose(result1, result2)


result1 = df[(df.A < .5) & (df.B < .5)]
result2 = pd.eval('df[(df.A < .5) & (df.B < .5)]')
assert np.allclose(result1, result2)


C_mean = df['C'].mean()
result1 = df[(df.A < C_mean) & (df.B < C_mean)]
result2 = df.query('A < @C_mean and B < @C_mean')
assert np.allclose(result1, result2)
