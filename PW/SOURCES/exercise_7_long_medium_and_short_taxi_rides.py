"""
@File         : exercise_7_long_medium_and_short_taxi_rides.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-10-03 12:10:51
@Email        : cuixuanstephen@gmail.com
@Description  : 长途、中程和短途出租车行程
"""

import pandas as pd
import numpy as np

s = pd.read_csv("../DATA/taxi-distance.csv", header=None).squeeze()
# s 是有名字的，0
categories = s.astype(str)
categories.loc[:] = "medium"
categories.loc[s <= 2] = "short"
categories.loc[s > 10] = "long"
categories.value_counts()

pd.cut(
    s, bins=[0, 2, 10, s.max()], include_lowest=True, labels=["short", "medium", "long"]
).value_counts()

passenger_count = pd.read_csv("../DATA/taxi-passenger-count.csv", header=None).squeeze()
pd.cut(
    s[passenger_count == 1],
    bins=[s.min(), 2, 10, s.max()],
    include_lowest=True,
    labels=["short", "medium", "long"],
).value_counts()

pd.cut(
    s[passenger_count == 1], bins=3, labels=["short", "medium", "long"]
).value_counts()
