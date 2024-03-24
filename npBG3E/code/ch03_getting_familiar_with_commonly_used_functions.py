"""
@File         : ch03_getting_familiar_with_commonly_used_functions.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-03-24 13:06:05
@Email        : cuixuanstephen@gmail.com
@Description  : 常用函数
"""

import numpy as np

i2 = np.eye(2)
i2

np.savetxt("eye.txt", i2)

# usecols 获取的是第 7 和第8 列
# unpack 参数设置为 True 使得不同列的数据分开存储
c, v = np.loadtxt("./data/AAPL.csv", delimiter=",", usecols=(6, 7), unpack=True)

vwap = np.average(c, weights=v)
print("VWAP = ", vwap)

print("mean = ", np.mean(c))

t = np.arange(len(c))
print("twap = ", np.average(c, weights=t))

h, l = np.loadtxt("./data/AAPL.csv", delimiter=",", usecols=(4, 5), unpack=True)
print("highest = ", np.max(h))
print("lowest =", np.min(l))

print("Spread high price:", np.ptp(h))
print("Spread low price:", np.ptp(l))

c = np.loadtxt("./data/AAPL.csv", delimiter=",", usecols=(6,), unpack=True)
print("median = ", np.median(c))

print("variance =", np.var(c))

log_returns = np.diff(np.log(c))

position_ret_indices = np.where(log_returns > 0)
position_ret_indices

annual_volatility = np.std(log_returns) / np.mean(log_returns)
annual_volatility = annual_volatility / np.sqrt(1 / 252.0)
print("Annual volatility", annual_volatility)
print("Monthly volatility", annual_volatility * np.sqrt(1.0 / 12.0))

dates, close = np.loadtxt("./data/AAPL.csv", delimiter=",", usecols=(1, 6), unpack=True)

from datetime import datetime


def datestr2num(s: bytes):
    return datetime.strptime(s.decode("utf-8"), "%d-%m-%Y").date().weekday()


np.datetime64("2024-03-24")
np.datetime64("20240324")
np.datetime64("2024-03")

local_time = np.datetime64("1677-01-01T20:19")
local_time

np.arange("2015-04-22", "2015-07-22", 7, dtype="datetime64")

dates, close = np.loadtxt(
    "./data/AAPL.csv",
    delimiter=",",
    usecols=(1, 6),
    unpack=True,
    converters={1: datestr2num},
)
print("Dates =", dates)

averages = np.zeros(5)

for i in range(5):
    indices = np.where(dates == i)
    prices = np.take(close, indices)
    avg = np.mean(prices)
    print("Day", i, "prices", prices, "Average", avg)
    averages[i] = avg

top = np.max(averages)
print("Highest average", top)
print("Top day of the week", np.argmax(averages))
bottom = np.min(averages)
print("Lowest average", bottom)
# argmin 函数返回的是 averages 数组中最小元素的索引值
print("Bottom day of the week", np.argmin(averages))

dates, open_price, high_price, low_price, close_price = np.loadtxt(
    "./data/AAPL.csv",
    delimiter=",",
    usecols=(1, 3, 4, 5, 6),
    converters={1: datestr2num},
    unpack=True,
)
close_price = close_price[:16]
dates = dates[:16]

# 找到第一个星期一
first_monday = np.ravel(np.where(dates == 0))[0]
print("The first Monday index is", first_monday)
# 找到最后一个星期五
last_friday = np.ravel(np.where(dates == 4))[-1]
print("The last Friday index is", last_friday)

week_indices = np.arange(first_monday, last_friday + 1)
print("Week indices initial", week_indices)

weeks_indices = np.split(week_indices, 3)


def summarize(a, o, h, l, c):
    monday_open = o[a[0]]
    week_high = np.max(np.take(h, a))
    week_low = np.min(np.take(l, a))
    friday_close = c[a[-1]]
    return ("AAPL", monday_open, week_high, week_low, friday_close)


week_summary = np.apply_along_axis(
    summarize,
    1,
    weeks_indices,
    open_price,
    high_price,
    low_price,
    close_price,
)

week_summary

np.savetxt("./data/week_summary.txt", week_summary, delimiter=",", fmt="%s")

h, l, c = np.loadtxt("./data/AAPL.csv", delimiter=",", usecols=(4, 5, 6), unpack=True)
N = 5
h = h[-N:]
l = l[-N:]

print("len(h)", len(h), "len(l)", len(l))
print("Close", c)
previous_close = c[-N - 1 : -1]

print("len(previous_close)", len(previous_close))
print("Previous close", previous_close)

true_range = np.maximum(h - l, h - previous_close, previous_close - l)
print("True range", true_range)

atr = np.zeros(N)
atr[0] = np.mean(true_range)
for i in range(1, N):
    atr[i] = (N - 1) * atr[i - 1] + true_range[i]
    atr[i] /= N
