"""
@Description: Hierarchical Indexing
@Author:Stephen CUI
@Time: 2023-04-03 16:27:18
"""
import pandas as pd
import numpy as np

index = [('California', 2010), ('California', 2020),
         ('New York', 2010), ('New York', 2020),
         ('Texas', 2010), ('Texas', 2020)]
populations = [37253956, 39538223,
               19378102, 20201249,
               25145561, 29145505]
pop = pd.Series(populations, index=index)


index = pd.MultiIndex.from_tuples(index)
pop = pop.reindex(index)


pop['Texas', 2020]
pop[:, 2020]
pop['New York', :]


pop_df = pop.unstack()

pop_df.stack()

pop_df = pd.DataFrame({'total': pop,
                       'under18': [9284094, 8898092,
                                   4318033, 4181528,
                                   6879014, 7432474]})

f_u18 = pop_df['under18'] / pop_df['total']

df = pd.DataFrame(np.random.rand(4, 2),
                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=['data1', 'data2'])

data = {('California', 2010): 37253956,
        ('California', 2020): 39538223,
        ('New York', 2010): 19378102,
        ('New York', 2020): 20201249,
        ('Texas', 2010): 25145561,
        ('Texas', 2020): 29145505}
pd.Series(data)


pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b'],
                           [1, 2, 1, 2]])
pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1), ('b', 2)])

pd.MultiIndex.from_product([['a', 'b'], [1, 2]])

pd.MultiIndex(levels=[['a', 'b'], [1, 2]],
              codes=[[0, 0, 0, 1, 1, 1], [0, 1, 1, 0, 0, 1]])


pop.index.names = ['state', 'year']


index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]],
                                   names=['year', 'visit'])
columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'],
                                      ['HR', 'Temp']],
                                     names=['subject', 'type'])


data = np.round(np.random.randn(4, 6), 1)
data[:, ::2] *= 10

data += 37
health_data = pd.DataFrame(data, index=index, columns=columns)

pop['California', 2010]

pop['California']

pop.loc['California':'New York']

pop[:, 2010]

pop[pop > 22_000_000]

pop[['California', 'New York']]

health_data['Guido', 'HR']

health_data.iloc[:2, :2]

health_data.loc[:, ('Bob', 'HR')]


# health_data.loc[(:, 1), (:, 'HR')]


idx = pd.IndexSlice
health_data.loc[idx[:, 1], idx[:, 'HR']]

# Rearranging Multi-Indexes
#       Sorted and Unsorted Indices
index = pd.MultiIndex.from_product([['a', 'c', 'b'], [1, 2]])
data = pd.Series(np.random.rand(6), index=index)
data.index.names = ['char', 'int']

try:
    data['a': 'b']
except KeyError as e:
    print('KeyError:', e)

data = data.sort_index()
data['a':'b']


pop.unstack(level=0)
pop.unstack(level=1)
pop.unstack().stack()

#        Index Setting and Resetting
pop_flat = pop.reset_index(name='population')

pop_flat.set_index(['state', 'year'])
