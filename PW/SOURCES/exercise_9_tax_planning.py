"""
@File         : exercise_9_tax_planning.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-10-03 15:30:59
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import pandas as pd
import numpy as np

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

df["current_net"] = (df["retail_price"] - df["wholesale_price"]) * df["sales"]

df["after_tax"] = pd.cut(
    df["retail_price"],
    bins=[0, 30, 80, df["retail_price"].max()],
    labels=[1, 0.9, 0.75],
).astype(np.float64)
