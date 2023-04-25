"""
@Description: Vectorized String Operations
@Author:Stephen CUI
@Time: 2023-04-05 14:24:34
"""

import numpy as np
x = np.array([2, 3, 5, 7, 11, 13])
x * 2

data = ['peter', 'Paul', 'MARY', 'gUIDO']
[s.capitalize() for s in data]

data = ['peter', 'Paul', None, 'MARY', 'gUIDO']
[s if s is None else s.capitalize() for s in data]


import pandas as pd
names = pd.Series(data)
names.str.capitalize()

monte = pd.Series(['Graham Chapman', 'John Cleese', 'Terry Gilliam',
                   'Eric Idle', 'Terry Jones', 'Michael Palin'])


monte.str.lower()
monte.str.len()
monte.str.startswith('T')
monte.str.split()


monte.str.extract('([A-Za-z]+)', expand=False)
monte.str.findall(r'^[^AEIOU].*[^aeiou]$')


monte.str.slice(0, 3)

monte.str[0: 3]


monte.str.split().str.get(-1)
monte.str.split().str[-1]


full_monte = pd.DataFrame({'name': monte,
                           'info': ['B|C|D', 'B|D', 'A|C',
                                    'B|D', 'B|C', 'B|C|D']})
full_monte

full_monte['info'].str.get_dummies('|')


recipes = pd.read_json('data/openrecipes.txt', lines=True)

recipes.ingredients.str.len().describe()

recipes.name[np.argmax(recipes.ingredients.str.len())]

recipes.description.str.contains('[Bb]reakfast').sum()
# 材料中使用了 Cinnamon （肉桂）的
recipes.ingredients.str.contains('[Cc]innamon').sum()

recipes.ingredients.str.contains('[Cc]inamon').sum()


spice_list = ['salt', 'pepper', 'oregano', 'sage', 'parsley',
              'rosemary', 'tarragon', 'thyme', 'paprika', 'cumin']
import re
spice_df = pd.DataFrame({
    spice: recipes.ingredients.str.contains(spice, re.IGNORECASE)
    for spice in spice_list
})
spice_df.sample(5)

# 欧芹和辣椒粉
selection = spice_df.query('parsley & paprika')
len(selection)

recipes.name[selection.index]
