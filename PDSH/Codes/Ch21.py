"""
@Description: Pivot Tables
@Author:Stephen CUI
@Time: 2023-04-04 22:07:48
"""

import numpy as np
import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
titanic.head()

# Pivot Tables by Hand
titanic.groupby('sex')[['survived']].mean()

# MultiIndex
titanic.groupby(['sex', 'class'])['survived'].mean()
titanic.groupby(['sex', 'class'])['survived'].aggregate('mean').unstack()


titanic.pivot_table('survived', index='sex', columns='class', aggfunc='mean')


age = pd.cut(titanic['age'], [0, 18, 80])
titanic.pivot_table('survived', index=[
                    'sex', age], columns='class', aggfunc='mean')

fare = pd.qcut(titanic['fare'], 2)
titanic.pivot_table('survived', index=['sex', age],
                    columns=[fare, 'class'], aggfunc='mean')


# Additional Pivot Table Options
titanic.pivot_table(index='sex', columns='class',
                    aggfunc={'survived': sum, 'fare': 'mean'})

# margin 返回的一行和一列的聚合函数的聚合结果
titanic.pivot_table('survived', index='sex',
                    columns='class', aggfunc='sum', margins=True)

# Example: Birthrate Data
births = pd.read_csv('data/births.csv')
births.sample(5)


births['decade'] = 10 * (births['year'] // 10)
births.pivot_table('births', index='decade', columns='gender',
                   aggfunc='sum')


import matplotlib.pyplot as plt
plt.style.use('ggplot')
births.pivot_table('births', index='year', columns='gender',
                   aggfunc='sum').plot()
plt.ylabel('total births per year')
plt.show()

quartiles = np.percentile(births['births'], [25, 50, 75])
mu = quartiles[1]
sig = .74 * (quartiles[2] - quartiles[0])

births = births.query('(births > @mu - 5 * @sig) & (births < @mu + 5 * @sig)')
births['day'] = births['day'].astype(int)

births.index = pd.to_datetime(10000 * births['year'] +
                              100 * births['month'] +
                              births['day'], format='%Y%m%d')
births['dayofweek'] = births.index.dayofweek


births.pivot_table('births', index='dayofweek',
                   columns='decade', aggfunc='mean').plot()
plt.gca().set(xticks=range(7),
              xticklabels=['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])
plt.ylabel('mean births by day')
plt.show()


births_by_date = births.pivot_table(
    'births', index=[births.index.month, births.index.day])
births_by_date.head()

# making sure to choose a leap year so February 29th is correctly handled!
from datetime import datetime
births_by_date.index = [datetime(2012, month, day)
                        for (month, day) in births_by_date.index]
births_by_date.head()


fig, ax = plt.subplots(figsize=(12, 4))
births_by_date.plot(ax=ax)
plt.show()
