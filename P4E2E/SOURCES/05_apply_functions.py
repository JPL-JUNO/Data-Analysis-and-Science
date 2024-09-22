"""
@File         : 05_apply_functions.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-09-22 16:06:27
@Email        : cuixuanstephen@gmail.com
@Description  : Apply functions
"""

import pandas as pd

df = pd.DataFrame({"a": [10, 20, 30], "b": [20, 30, 40]})


def my_sq(x):
    return x**2


def avg_2(x, y):
    return (x + y) / 2


# 我们给 .apply() 我们想要使用的函数的引用，但此时我们并没有调用该函数。
sq = df["a"].apply(my_sq)


def my_exp(x, e):
    return x**e


# 我们将第二个参数作为关键字参数传递给 .apply()
ex = df["a"].apply(my_exp, e=2)
ex = df["a"].apply(my_exp, e=3)


def print_me(x):
    print(x)


df.apply(print_me, axis=0)  # 处于性能问题 axis=1 或者 axis='column' 是不合理的


def avg3(x, y, z):
    return (x + y + z) / 3


df.apply(avg3)  # 这会报错，因为 entire column is passed into the first argument


def avg3_apply(col):
    x, y, z, *_ = col
    return (x + y + z) / 3


import numpy as np


def avg_2_mod(x, y):
    # 如果 x 和 y 是标量的话，那么是能运行的，但是 x 如果是向量就会报错
    if x == 20:
        return np.NaN
    else:
        return (x + y) / 2


avg_2_mod_vec = np.vectorize(avg_2_mod)


@np.vectorize
def v_avg_2_mod(x, y):
    if x == 20:
        return np.NaN
    else:
        return (x + y) / 2


import numba


@numba.vectorize
def v_avg_2_numba(x, y):
    if x == 20:
        return np.NaN
    else:
        return (x + y) / 2
