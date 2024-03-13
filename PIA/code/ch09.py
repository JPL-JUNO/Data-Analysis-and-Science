"""
@File         : ch09.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-03-13 20:31:30
@Email        : cuixuanstephen@gmail.com
@Description  : GroupBy 对象
"""

import pandas as pd

food_data = {
    "Item": ["Banana", "Cucumber", "Orange", "Tomato", "Watermelon"],
    "Type": ["Fruit", "Vegetable", "Fruit", "Vegetable", "Fruit"],
    "Price": [0.99, 1.25, 0.25, 0.33, 3.00],
}
supermarket = pd.DataFrame(data=food_data)
supermarket
