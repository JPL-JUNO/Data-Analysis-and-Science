"""
@File         : to_html_test.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-29 19:02:54
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""
import numpy as np
import pandas as pd

weather_df = pd.DataFrame(
    np.random.rand(10, 2) * 5,
    index=pd.date_range(start="2021-01-01", periods=10),
    columns=["Tokyo", "Beijing"],
)


def rain_condition(v):
    if v < 1.75:
        return "Dry"
    elif v < 2.75:
        return "Rain"
    return "Heavy Rain"


df3 = pd.DataFrame(
    np.random.randn(4, 4),
    pd.MultiIndex.from_product([["A", "B"], ["r1", "r2"]]),
    columns=["c1", "c2", "c3", "c4"],
)


def highlight_max(s, props=""):
    return np.where(s == np.nanmax(s.values), props, "")
