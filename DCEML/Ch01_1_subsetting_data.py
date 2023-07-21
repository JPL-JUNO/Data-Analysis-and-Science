"""
@Description: subsetting data
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-07-21 20:18:14
"""

import numpy as np
import pandas as pd
nls97 = pd.read_csv('data/nls97.csv', index_col='personid')

demo_cols = ['gender', 'birthyear', 'maritalstatus', 'weeksworked16',
             'wageincome', 'highestdegree']
nls97_demo = nls97[demo_cols]
assert nls97_demo.index.name == 'personid'

print(nls97_demo[1000:1004].T)

print(nls97_demo[1000:1004:2].T)

print(nls97_demo[:3].T)
