"""
@Description: Aggregation and Grouping
@Author:Stephen CUI
@Time: 2023-04-04 14:37:24
"""

import pandas as pd
import numpy as np
import seaborn as sns


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


planets = sns.load_dataset('planets')
planets.shape
planets.head()

# Simple Aggregation in Pandas
rng = np.random.RandomState(42)
ser = pd.Series(rng.rand(5))
ser
ser.sum(), ser.mean(),


df = pd.DataFrame({'A': rng.rand(5),
                   'B': rng.rand(5)})

df

df.mean()
df.sum()

df.mean(axis=1)

planets.dropna().describe()

df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'data': range(6)}, columns=['key', 'data'])


df.groupby('key')
df.groupby('key').sum()

# pandas.core.groupby.generic.DataFrameGroupBy
planets.groupby('method')
# pandas.core.groupby.generic.SeriesGroupBy
planets.groupby('method')['orbital_period']

planets.groupby('method')['orbital_period'].median()


# for method, group in planets.groupby('method'):
#     print("{0:30s} shape={1}".format(method, group.shape))


planets.groupby('method')['year'].describe()


rng = np.random.RandomState(0)
df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'data1': range(6),
                   'data2': rng.randint(0, 10, 6)},
                  columns=['key', 'data1', 'data2'])


df.groupby('key').aggregate(['min', np.median, max])


df.groupby('key').aggregate({'data1': 'min',
                             'data2': 'max'})


def filter_func(x):
    return x['data2'].std() > 2


display('df', "df.groupby('key').std()",
        "df.groupby('key').filter(filter_func)")


# transformation
def center(x):
    return x - x.mean()


df.groupby('key').transform(center)


def norm_by_data2(x):
    x['data1'] /= x['data2'].sum()
    return x


df.groupby('key', group_keys=False).apply(norm_by_data2)


L = [0, 1, 0, 1, 2, 0]
df.groupby(L, group_keys=False).sum(numeric_only=True)

df.groupby(df['key']).sum()  # 似乎比 df.groupby('key').sum() 要蠢一些

df2 = df.set_index('key')
mapping = {'A': 'vowel', 'B': 'consonant', 'C': 'consonant'}
display('df2', 'df2.groupby(mapping).sum()')

df2.groupby(str.lower).mean()

df2.groupby([str.lower, mapping]).mean()


decade = 10 * (planets['year'] // 10)
decade = decade.astype(str) + 's'
decade.name = 'decade'
planets.groupby(['method', decade])['number'].sum().unstack().fillna(0)
