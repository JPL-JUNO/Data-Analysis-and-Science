"""
@File         : exercise_11_bestsellers.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-10-03 22:31:21
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import numpy as np
import pandas as pd

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
