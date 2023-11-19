"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-11-19 16:20:37
@Description: 
"""

import numpy as np


def mape(y_true, y_pred) -> float:
    return 100 * np.mean(np.abs((y_true - y_pred) / y_true))
