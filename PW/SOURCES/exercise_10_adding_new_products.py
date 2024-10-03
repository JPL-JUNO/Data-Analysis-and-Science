"""
@File         : exercise_10_adding_new_products.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-10-03 21:19:24
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import pandas as pd
import numpy as np

new_products = pd.DataFrame(
    [
        {
            "product_id": 24,
            "name": "phone",
            "wholesale_price": 200,
            "retail_price": 500,
        },
        {"product_id": 16, "name": "apple", "wholesale_price": 0.5, "retail_price": 1},
        {"product_id": 17, "name": "pear", "wholesale_price": 0.6, "retail_price": 1.2},
    ],
    index=range(5, 8),
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
