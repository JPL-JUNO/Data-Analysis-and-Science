"""
@File         : exercise_6_passenger_frequency.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-10-03 11:53:29
@Email        : cuixuanstephen@gmail.com
@Description  : 乘客频率
"""

import pandas as pd
import numpy as np

s = pd.read_csv("../DATA/taxi-passenger-count.csv", header=None).squeeze()
s.value_counts(normalize=True)[[1, 6]]
