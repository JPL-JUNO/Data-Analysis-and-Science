"""
@Description: Combining Datasets: concat and append
@Author:Stephen CUI
@Time: 2023-04-04 09:20:29
"""

import pandas as pd
import numpy as np
from typing import List


def make_df(cols: str, ind: List[int]):
    """Quickly make a DataFrame

    Args:
        cols (_type_): _description_
        ind (_type_): _description_
    """
    data = {c: [str(c) + str(i) for i in ind] for c in cols}
    return pd.DataFrame(data)


class display(object):
    """Display HTML representation of multiple objects

    Args:
        object (_type_): _description_
    """
    template = """<div style='float: left; padding: 10px;'>
    <p style='font-family: "Courier New", Courier, monospace'>{0}</p>
    {1}
    </div>
    """

    def __init__(self, *args):
        self.args = args

    def _repr_html_(self):
        return '\n'.join(self.template.format(a, eval(a)._repr_html_())
                         for a in self.args)

    def __repr__(self):
        return '\n\n'.join(a + '\n' + repr(eval(a))
                           for a in self.args)


# Recall: Concatenation of NumPy Arrays
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
np.concatenate([x, y, z])


x = [[1, 2],
     [3, 4]]
np.concatenate([x, x], axis=1)
np.concatenate([x, x], axis=0)

# Simple Concatenation with pd.concat


ser1 = pd.Series(['A', 'B', 'C'], index=[1, 2, 3])
ser2 = pd.Series(['D', 'E', 'F'], index=[4, 5, 6])
pd.concat([ser1, ser2])


df1 = make_df('AB', [1, 2])
df2 = make_df('AB', [3, 4])

display('df1', 'df2', 'pd.concat([df1, df2])')


df3 = make_df('AB', [0, 1])
df4 = make_df('CD', [0, 1])
display('df3', 'df4', "pd.concat([df3, df4], axis='columns')")


x = make_df('AB', [0, 1])
y = make_df('AB', [2, 3])

y.index = x.index
display('x', 'y', 'pd.concat([x, y])')

# Treating repeated indices as an error
try:
    pd.concat([x, y], verify_integrity=True)
except ValueError as e:
    print('ValueError:\n', e)

# Ignoring the index
display('x', 'y', 'pd.concat([x, y], ignore_index=True)')

# Adding MultiIndex keys
display('x', 'y', "pd.concat([x, y], keys=['x', 'y'])")


# Concatenation with Joins
df5 = make_df('ABC', [1, 2])
df6 = make_df('BCD', [3, 4])

display('df5', 'df6', 'pd.concat([df5, df6])')

display('df5', 'df6', "pd.concat([df5, df6], join='inner')")

# 如果 columns 的长度不一样怎么办？
pd.concat([df5, df6.reindex(df5.columns, axis=1)])

# The append Method
display('df1', 'df2', 'df1.append(df2)')
