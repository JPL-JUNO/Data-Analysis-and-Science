"""
@Description: Combining Datasets: merge and join
@Author:Stephen CUI
@Time: 2023-04-04 10:43:35
"""

import pandas as pd
import numbers as np


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


# Relational Algebra

# One-to-One Joins
df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'group': ['Accounting', 'Engineering',
                              'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
                    'hire_date': [2004, 2008, 2012, 2014]})
display('df1', 'df2')

df3 = pd.merge(df1, df2)

# Many-to-One Joins
df4 = pd.DataFrame({'group': ['Accounting', 'Engineering', 'HR'],
                    'supervisor': ['Carly', 'Guido', 'Steve']})
display('df3', 'df4', 'pd.merge(df3, df4)')


df5 = pd.DataFrame({'group': ['Accounting', 'Accounting',
                              'Engineering', 'Engineering', 'HR', 'HR'],
                    'skills': ['math', 'spreadsheets', 'software', 'math',
                               'spreadsheets', 'organization']})
display('df1', 'df5', "pd.merge(df1, df5)")


# The on Keyword
display('df1', 'df2', "pd.merge(df1, df2, on='employee')")


df3 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                   'salary': [70000, 80000, 120000, 90000]})
display('df1', 'df3', "pd.merge(df1, df3, left_on='employee', right_on='name')")

pd.merge(df1, df3, left_on='employee', right_on='name').drop('name', axis=1)


df1a = df1.set_index('employee')
df2a = df2.set_index('employee')
display('df1a', 'df2a')


display('df1a', 'df2a', 'pd.merge(df1a, df2a, left_index=True, right_index=True)')


df1a.join(df2a)


display('df1a', 'df3', "pd.merge(df1a, df3, left_index=True, right_on='name')")

# Specifying Set Arithmetic for Joins
df6 = pd.DataFrame({'name': ['Peter', 'Paul', 'Mary'],
                    'food': ['fish', 'beans', 'bread']})
df7 = pd.DataFrame({'name': ['Mary', 'Joseph'],
                    'drink': ['wine', 'beer']})
display('df6', 'df7', 'pd.merge(df6, df7)')

pd.merge(df6, df7, how='inner')


display('df6', 'df7', "pd.merge(df6, df7, how='outer')")

display('df6', 'df7', "pd.merge(df6, df7, how='left')")

# Overlapping Column Names: The suffixes Keyword
df8 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'rank': [1, 2, 3, 4]})
df9 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'rank': [3, 1, 4, 2]})
display('df8', 'df9', "pd.merge(df8, df9, on='name')")


pd.merge(df8, df9, on='name', suffixes=['_L', '_R'])

# Example: US States Data
pop = pd.read_csv('data/state-population.csv')
areas = pd.read_csv('data/state-areas.csv')
abbrevs = pd.read_csv('data/state-abbrevs.csv')

display('pop.head()', 'areas.head()', 'abbrevs.head()')

merged = pd.merge(pop, abbrevs, how='outer',
                  left_on='state/region', right_on='abbreviation').drop('abbreviation', axis=1)
merged.head()

# 它的结果表名，如果不适用 outer 会删掉一些数据，并且 population 和 state 存在一些缺失值
merged.isnull().any()

# 使用 mask 找到 population 的空值
merged[merged['population'].isnull()].head()

merged.loc[merged['state'].isnull(), 'state/region'].unique()

merged.loc[merged['state/region'] == 'PR', 'state'] = 'Puerto Rico'
merged.loc[merged['state/region'] == 'USA', 'state'] = 'United States'
merged.isnull().any()

final = pd.merge(merged, areas, on='state', how='left')
final.head()

# area 和 population 存在缺失值
final.isnull().any()

final['state'][final['area (sq. mi)'].isnull()].unique()

final.dropna(inplace=True)
final.head()

data_2010 = final.query("year == 2010 & ages == 'total'")
data_2010.head()

data_2010.set_index('state', inplace=True)
# Series
density = data_2010['population'] / data_2010['area (sq. mi)']
density.sort_values(ascending=False, inplace=True)
density.head()

density.tail()
