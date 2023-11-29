"""
@Title: 对 MA 模型进行滚动预测
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-11-30 00:09:05
@Description: 
"""

from pandas import DataFrame
from statsmodels.tsa.statespace.sarimax import SARIMAX
import numpy as np


def _naive_mean(df, train_len, total_len, window):
    pred = []
    for i in range(train_len, total_len, window):
        mean = np.mean(df[:i].values)
        pred.extend(mean for _ in range(window))
    return pred


def _naive_last(df, train_len, total_len, window):
    pred = []
    for i in range(train_len, total_len, window):
        last_value = df[:i].iloc[-1].values[0]
        pred.extend(last_value for _ in range(window))
    return pred


def _ma(df, train_len, total_len, window):
    pred = []
    for i in range(train_len, total_len, window):
        model = SARIMAX(df[:i], order=(0, 0, 2))
        res = model.fit(disp=False)
        predictions = res.get_prediction(0, i + window - 1)
        oos_pred = predictions.predicted_mean.iloc[-window:]
        pred.extend(oos_pred)
    return pred


methods = {'mean': _naive_mean,
           'last': _naive_last,
           'MA': _ma}


def rolling_forecast(df: DataFrame, train_len: int, horizon: int,
                     window: int, method: str) -> list:
    total_len = train_len + horizon
    assert method in methods, '预测方法不存在'

    pred = methods[method](df, train_len, total_len, window)
    return pred
    # pred = []
    # if method == 'mean':
    #     for i in range(train_len, total_len, window):
    #         mean = np.mean(df[:i].values)
    #         pred.extend(mean for _ in range(window))
    #     return pred
    # elif method == 'last':
    #     for i in range(train_len, total_len, window):
    #         last_value = df[:i].iloc[-1].values[0]
    #         pred.extend(last_value for _ in range(window))
    #     return pred

    # elif method == 'MA':
    #     for i in range(train_len, total_len, window):
    #         model = SARIMAX(0, 0, 2)
    #         res = model.fit(disp=False)
    #         predictions = res.get_prediction(0, i + window - 1)
    #         oos_pred = predictions.predicted_mean.iloc[-window:]
    #         pred.extend(oos_pred)
    #     return pred
