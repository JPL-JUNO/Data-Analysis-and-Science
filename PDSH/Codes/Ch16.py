"""
@Description: Handling Missing Data
@Author:Stephen CUI
@Time: 2023-04-03 13:52:16
"""
import pandas as pd
import numpy as np

vals1 = np.array([1, None, 3, 4])
vals1


vals2 = np.array([1, np.nan, 3, 4])
vals2.dtype  # dtype('float64')
1 + np.nan

0 * np.nan

vals2.max(), vals2.min(), vals2.sum()
np.nanmax(vals2), np.nanmin(vals2), np.nansum(vals2)


pd.Series([1, np.nan, 2, None])

x = pd.Series(range(2), dtype=int)
x[0] = None
x.dtype

pd.Series([1, np.nan, 2, None, pd.NA], dtype='Int32')


data = pd.Series([1, np.nan, 'hello', None])
data.isnull()

data[data.notnull()]

data.dropna()

df = pd.DataFrame([[1, np.nan, 2],
                   [2, 3, 5],
                   [np.nan, 4, 6]])

df.dropna()

df.dropna(axis=1)
df.dropna(axis='columns')

df[3] = np.nan
df

df.dropna(axis=1, how='all')

df.dropna(axis='rows', thresh=3)


data = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'),
                 dtype='Int32')

data.fillna(0)
data.fillna(method='ffill')
data.fillna(method='bfill')


df.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)
