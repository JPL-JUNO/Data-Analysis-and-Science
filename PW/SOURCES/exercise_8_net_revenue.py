"""
@File         : exercise_8_net_revenue.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-10-03 15:02:43
@Email        : cuixuanstephen@gmail.com
@Description  : 净收入
"""

import pandas as pd
import numpy as np

df = pd.DataFrame(
    [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]],
    index=list("xyz"),
    columns=list("abcd"),
)

df = pd.DataFrame(
    [
        {"a": 10, "b": 20, "c": 30, "d": 40},
        {"a": 50, "b": 60, "c": 70, "d": 80},
        {"a": 90, "b": 100, "c": 110, "d": 120},
    ],
    index=list("xyz"),
)
df = pd.DataFrame(
    {"a": [10, 50, 90], "b": [20, 60, 100], "c": [30, 70, 110], "d": [40, 80, 120]},
    index=list("xyz"),
)


df = pd.DataFrame(
    np.random.randint(0, 10, [3, 4]), columns=list("abcd"), index=list("xyz")
)

df = pd.DataFrame(
    [
        {
            "product_id": 23,
            "name": "computer",
            "wholesale_price": 500,
            "retail_price": 1000,
            "sales": 100,
        },
        {
            "product_id": 96,
            "name": "Python Workout",
            "wholesale_price": 35,
            "retail_price": 75,
            "sales": 1000,
        },
        {
            "product_id": 97,
            "name": "Pandas Workout",
            "wholesale_price": 35,
            "retail_price": 75,
            "sales": 500,
        },
        {
            "product_id": 15,
            "name": "banana",
            "wholesale_price": 0.5,
            "retail_price": 1,
            "sales": 200,
        },
        {
            "product_id": 87,
            "name": "sandwich",
            "wholesale_price": 3,
            "retail_price": 5,
            "sales": 300,
        },
    ]
)

((df.retail_price - df.wholesale_price) * df.sales).sum()
