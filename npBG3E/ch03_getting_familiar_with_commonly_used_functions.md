# 常用函数

将以分析历史股价为例，介绍怎样从文件中载入数据，以及怎样使用 NumPy 的基本数学和统计分析函数。这里还将学习读写文件的方法，并尝试函数式编程和 NumPy 线性代数运算。

```python
import numpy as np
```

## 文件读写

通常情况下，数据是以文件形式存储的。学会读写文件是深入学习 NumPy 的基础。

```python
>>> i2 = np.eye(2)
>>> i2
array([[1., 0.],
       [0., 1.]])
>>> 
>>> np.savetxt("eye.txt", i2)
>>> 
```

不仅仅可以使用文件名，也可以使用文件句柄（[file handle](https://diveintopython3.net/files.html)）

## 读入 CSV 文件

CSV（Comma-Separated Value，逗号分隔值）格式是一种常见的文件格式。通常，数据库的转存文件就是 CSV 格式的，文件中的各个字段对应于数据库表中的列。众所周知，电子表格软件（如Microsoft Excel）可以处理 CSV 文件。

```python
# usecols 获取的是第 7 和第8 列
# unpack 参数设置为 True 使得不同列的数据分开存储
c, v = np.loadtxt("./data/AAPL.csv", delimiter=",", usecols=(6, 7), unpack=True)
```

## 成交量加权平均价格（VWAP）

VWAP（Volume-Weighted Average Price，成交量加权平均价格）是一个非常重要的金融指标，它代表着金融资产的“平均”价格。某个价格的成交量越高，该价格所占的权重就越大。VWAP 就是以成交量为权重计算出来的加权平均值，常用于算法交易。

### 计算 VWAP

```python
>>> vwap = np.average(c, weights=v)
>>> print("VWAP =", vwap)
VWAP = 350.5895493532009
>>>
```

仅仅调用了 `np.average` 函数，并将 `v` 作为权重参数使用，就完成了 VWAP 的计算。此外，NumPy 中也有计算算术平均值的函数。

### 算术平均值函数

`np.mean` 函数可以计算数组元素的算术平均值。

```python
>>> print("mean =", np.mean(c))
mean = 351.0376666666667
>>>
```

### 时间加权平均价格

在金融中，TWAP（Time-Weighted Average Price，时间加权平均价格）是另一种“平均”价格的指标。TWAP只是一个变种而已，基本的思想就是最近的价格重要性大一些，所以我们应该对近期的价格给以较高的权重。最简单的方法就是用 `np.arange` 函数创建一个从 0 开始依次增长的自然数序列，自然数的个数即为收盘价的个数。当然，这并不一定是正确的计算 TWAP 的方式，这里仅仅是为了说明问题。

```python
>>> t = np.arange(len(c))
>>> print("twap =", np.average(c, weights=t))
twap = 352.4283218390804
>>>
```

## 值域

通常，我们不仅仅想知道一组数据的平均值，还希望知道数据的极值以及完整的取值范围——最大值和最小值。我们的股价示例数据中已经包含了每天的股价范围——最高价和最低价。但是，我们还需要知道最高价的最大值以及最低价的最小值。

### 找到最大值和最小值

```python
# 需要再次读入数据，将每日最高价和最低价的数据载入数组：
>>> h, l = np.loadtxt("./data/AAPL.csv", delimiter=",", usecols=(4, 5), unpack=True)
>>> print("highest =", np.max(h))
highest = 364.9
>>> print("lowest =", np.min(l))
lowest = 333.53
>>>
```

NumPy 中有一个 `np.ptp` 函数可以计算数组的取值范围（极差）。该函数返回的是数组元素的最大值和最小值之间的差值。也就是说，返回值等于

$$\max(array) - \min(array)$$

```python
>>> print("Spread high price:", np.ptp(h))
Spread high price: 24.859999999999957
>>> print("Spread low price:", np.ptp(l))
Spread low price: 26.970000000000027
>>>
```

## 统计分析

股票交易者对于收盘价的预测很感兴趣。常识告诉我们，这个价格应该接近于某种均值。算数平均值和加权平均值都是在数值分布中寻找中心点的方法。然而，它们对于异常值（outlier）既不鲁棒也不敏感。举例来说，如果我们有一个高达 100 万美元的收盘价，这将影响到我们的计算结果。

### 简单统计分析

我们可以用一些阈值来除去异常值，但其实有更好的方法，那就是中位数。

```python
>>> c = np.loadtxt("./data/AAPL.csv", delimiter=",", usecols=(6,), unpack=True)
>>> print("median =", np.median(c))
median = 352.055
>>>
```

另外一个我们关心的统计量就是方差。方差能够体现变量变化的程度。在我们的例子中，方差还可以告诉我们投资风险的大小。那些股价变动过于剧烈的股票一定会给持有者制造麻烦。

```python
>>> print("variance =", np.var(c))
variance = 50.126517888888884
>>>
```

## 股票收益率

在学术文献中，收盘价的分析常常是基于股票收益率和对数收益率的。简单收益率是指相邻两个价格之间的变化率，而对数收益率是指所有价格取对数后两两之间的差值。对数收益率也可以用来衡量价格的变化率。注意，由于收益率是一个比值，例如我们用美元除以美元（也可以是其他货币单位），因此它是无量纲的。投资者最感兴趣的是收益率的方差或标准差，因为这代表着投资风险的大小。

### 分析股票收益率

NumPy 中的 `np.diff` 函数可以返回一个由相邻数组元素的差值构成的数组。不过这里要注意， `np.diff` 返回的数组比原数组少一个元素。

```python
# 伪代码不能运行
returns = np.diff(arr) / arr[:-1]
```

对数收益率计算起来甚至更简单一些。我们先用 `np.log` 函数得到每一个收盘价的对数，再对结果使用 `np.diff` 函数即可。

```python
>>> log_returns = np.diff(np.log(c))
>>> log_returns
array([ 0.00953488,  0.01668775, -0.00205991, -0.00255903,  0.00887039,
        0.01540739,  0.0093908 ,  0.0082988 , -0.01015864,  0.00649435,
        0.00650813,  0.00200256,  0.00893468, -0.01339027, -0.02183875,
       -0.03468287,  0.01177296,  0.00075857,  0.01528161,  0.01440064,
       -0.011103  ,  0.00801225,  0.02090904,  0.00122297, -0.01297267,
        0.00112499, -0.00929083, -0.01659219,  0.01522945])
>>>
```

一般情况下，我们应检查输入数组以确保其不含有零和负数。否则，将得到一个错误提示。

我们很可能对哪些交易日的收益率为正值非常感兴趣。在完成了前面的步骤之后，我们只需要用 `np.where` 函数就可以做到这一点。`np.where` 函数可以根据指定的条件返回所有满足条件的数组元素的索引值。

```python
>>> position_ret_indices = np.where(log_returns > 0)
>>> position_ret_indices
(array([ 0,  1,  4,  5,  6,  7,  9, 10, 11, 12, 16, 17, 18, 19, 21, 22, 23,
       25, 28], dtype=int64),)
>>>
```

在投资学中，波动率（volatility）是对价格变动的一种度量。历史波动率可以根据历史价格数据计算得出。计算历史波动率（如年波动率或月波动率）时，需要用到对数收益率。年波动率等于对数收益率的标准差除以其均值，再除以交易日倒数的平方根，通常交易日取 252 天。(**这个波动率好像不太对**)

```python
>>> annual_volatility = np.std(log_returns) / np.mean(log_returns)
>>> annual_volatility = annual_volatility / np.sqrt(1 / 252.0)
>>> print("Annual volatility", annual_volatility)
Annual volatility 129.27478991115132
>>> print("Monthly volatility", annual_volatility * np.sqrt(1.0 / 12.0))
Monthly volatility 37.318417377317765
>>>
```

## 日期分析

### 分析日期数据

程序员不喜欢日期，因为处理日期总是很烦琐。NumPy 是面向浮点数运算的，因此需要对日期做一些专门的处理。下面的代码会直接报错：

```python
>>> dates, close = np.loadtxt("./data/AAPL.csv", delimiter=",", usecols=(1, 6), unpack=True)
Traceback (most recent call last):
...
ValueError: could not convert string '28-01-2011' to float64 at row 0, column 2.
>>>
```

显然，NumPy 尝试把日期转换成浮点数。我们需要做的是显式地告诉 NumPy 怎样来转换日期，而这需要用到 `np.loadtxt` 函数中的一个特定的参数。这个参数就是 `converters`，它是数据列和转换函数之间进行映射的字典。

```python
>>> from datetime import datetime
>>>
>>>
>>> def datestr2num(s: bytes):
...     return datetime.strptime(s.decode("utf-8"), "%d-%m-%Y").date().weekday()
... 
>>>
>>> dates, close = np.loadtxt(
...     "./data/AAPL.csv",
...     delimiter=",",
...     usecols=(1, 6),
...     unpack=True,
...     converters={1: datestr2num},
... )
>>> print("Dates =", dates)
Dates = [4. 0. 1. 2. 3. 4. 0. 1. 2. 3. 4. 0. 1. 2. 3. 4. 1. 2. 3. 4. 0. 1. 2. 3.
 4. 0. 1. 2. 3. 4.]
>>>
```

`np.where` 函数会根据指定的条件返回所有满足条件的数组元素的索引值。`np.take` 函数可以按照这些索引值从数组中取出相应的元素。我们可以把每个工作日的数据都取出来，然后计算：

```python
>>> averages = np.zeros(5)
>>>
>>> for i in range(5):
...     indices = np.where(dates == i)
...     prices = np.take(close, indices)
...     avg = np.mean(prices)
...     print("Day", i, "prices", prices, "Average", avg)
...     averages[i] = avg
...
Day 0 prices [[339.32 351.88 359.18 353.21 355.36]] Average 351.7900000000001
Day 1 prices [[345.03 355.2  359.9  338.61 349.31 355.76]] Average 350.63500000000005
Day 2 prices [[344.32 358.16 363.13 342.62 352.12 352.47]] Average 352.1366666666666
Day 3 prices [[343.44 354.54 358.3  342.88 359.56 346.67]] Average 350.8983333333333
Day 4 prices [[336.1  346.5  356.85 350.56 348.16 360.   351.99]] Average 350.0228571428571
>>>
```

如果你愿意，还可以找出哪个工作日的平均收盘价是最高的，哪个是最低的。这很容易做到，用 `np.max` 和 `np.min` 函数即可。

```python
top = np.max(averages)
print("Highest average", top)
print("Top day of the week", np.argmax(averages))
bottom = np.min(averages)
print("Lowest average", bottom)
# argmin 函数返回的是 averages 数组中最小元素的索引值
print("Bottom day of the week", np.argmin(averages))
```

### 使用 datetime64 数据类型

datetime64 数据类型是在 NumPy 1.7.0 中引入的：

```python
>>> np.datetime64("2024-03-24")
numpy.datetime64('2024-03-24')
>>>
```

我们使用 YYYY-MM-DD 格式，其中 Y 对应年份，M 对应月份，D 对应月份中的日期。NumPy 使用 [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) 标准。这是表示日期和时间的国际标准。ISO 8601 允许使用 YYYY-MM-DD、YYYY-MM 和 YYYYMMDD 格式。

```python
>>> np.datetime64("20240324")
numpy.datetime64('20240324')
>>> np.datetime64("2024-03")
numpy.datetime64('2024-03')
>>>
```

默认情况下，ISO 8601 使用本地时区。可以使用格式 `T[hh:mm:ss]` 指定时间。

```python
>>> local_time = np.datetime64("1677-01-01T20:19")
>>> local_time
numpy.datetime64('1677-01-01T20:19')
>>>
```

将两个 `datetime64` 对象相减将创建一个 NumPy `timedelta64` 对象。我们还可以向 datetime64 对象添加或减去天数。 例如，2015 年 4 月 22 日恰好是星期三。使用 `np.arange()` 函数创建一个数组，其中包含从 2015 年 4 月 22 日到 2015 年 5 月 22 日的所有星期三，如下所示：

```python
>>> np.arange("2015-04-22", "2015-07-22", 7, dtype="datetime64")
array(['2015-04-22', '2015-04-29', '2015-05-06', '2015-05-13',
       '2015-05-20', '2015-05-27', '2015-06-03', '2015-06-10',
       '2015-06-17', '2015-06-24', '2015-07-01', '2015-07-08',
       '2015-07-15'], dtype='datetime64[D]')
>>>
```

## 汇总

有些时候，我们可能会看周线，月线，这时候就需要按照与原数据不同的角度进行汇总。比如说统计每周的 OHLC

```python
>>> dates, open_price, high_price, low_price, close_price = np.loadtxt(
...     "./data/AAPL.csv",
...     delimiter=",",
...     usecols=(1, 3, 4, 5, 6),
...     converters={1: datestr2num},
...     unpack=True,
... )
>>> close_price = close_price[:16] # 为了简单起见，我们只考虑前三周的数据
>>> dates = dates[:16]
>>>
>>> # 找到第一个星期一
>>> first_monday = np.ravel(np.where(dates == 0))[0]
>>> print("The first Monday index is", first_monday)
The first Monday index is 1
>>> # 找到最后一个星期五
>>> last_friday = np.ravel(np.where(dates == 4))[-1]
>>> print("The last Friday index is", last_friday)
The last Friday index is 15
>>>
>>> week_indices = np.arange(first_monday, last_friday + 1)
>>> print("Week indices initial", week_indices)
Week indices initial [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
>>>
>>> weeks_indices = np.split(week_indices, 3)
>>>
>>>
>>> def summarize(a, o, h, l, c):
...     monday_open = o[a[0]]
...     week_high = np.max(np.take(h, a))
...     week_low = np.min(np.take(l, a))
...     friday_close = c[a[-1]]
...     return ("AAPL", monday_open, week_high, week_low, friday_close)
...
>>>
>>> week_summary = np.apply_along_axis(
...     summarize,
...     1,
...     weeks_indices,
...     open_price,
...     high_price,
...     low_price,
...     close_price,
... )
>>>
>>> week_summary
array([['AAPL', '335.8', '346.7', '334.3', '346.5'],
       ['AAPL', '347.89', '360.0', '347.64', '356.85'],
       ['AAPL', '356.79', '364.9', '349.52', '350.56']], dtype='<U32')
>>>
>>> np.savetxt("./data/week_summary.txt", week_summary, delimiter=",", fmt="%s")
>>>
```

`np.apply_along_axis` 函数，这个函数会调用另外一个由我们给出的函数，作用于每一个数组元素上。

格式字符串以一个百分号开始。接下来是一个可选的标志字符：- 表示结果左对齐，0 表示
左端补 0，+ 表示输出符号（正号 + 或负号 -）。第三部分为可选的输出宽度参数，表示输出的最小位数。第四部分是精度格式符，以"."开头，后面跟一个表示精度的整数。最后是一个类型指定字符，这里指定为字符串类型。

|字符编码|含义|
|--|--|
|c|单个字符|
|d或i|十进制有符号整数|
|e或E|科学记数法表示的浮点数|
|f|浮点数|
|g或G|自动在e、E和f中选择合适的表示法|
|o|八进制有符号整数|
|s|字符串|
|u|十进制无符号整数|
|x或X|十六进制无符号整数|

## 真实波动幅度均值（ATR）

ATR（Average True Range，真实波动幅度均值）是一个用来衡量股价波动性的技术指标。

### 计算真实波动幅度均值

1. ATR 是基于 N 个交易日的最高价和最低价进行计算的，通常取最近 20 个交易日。

2. 对于每一个交易日，计算以下各项
    - h - l 当日股价范围，即当日最高价和最低价之差。
    - h – previous_close 当日最高价和前一个交易日收盘价之差。
    - previous_close – l 前一个交易日收盘价和当日最低价之差。
3. 基于上面计算的 3 个数值，我们来计算所谓的真实波动幅度，也就是这三者的最大值。现在我们想在一组数组之间按照元素挑选最大值——也就是在所有的数组中第一个元素的最大值、第二个元素的最大值等。为此，需要用 NumPy 中的 `np.maximum` 函数，而不是 `np.max` 函数。
4. ATR 数组的首个元素就是数组元素的平均值。
5. 用如下公式计算其他元素的值：

$$\frac{(N-1)PATR+TR}{N}$$

这里，$PATR$ 表示前一个交易日的 ATR 值，$TR$ 即当日的真实波动幅度。

```python
>>> h, l, c = np.loadtxt("./data/AAPL.csv", delimiter=",", usecols=(4, 5, 6), unpack=True)
>>> N = 5
>>> h = h[-N:]
>>> l = l[-N:]
>>>
>>> print("len(h)", len(h), "len(l)", len(l))
len(h) 5 len(l) 5
>>> print("Close", c)
Close [336.1  339.32 345.03 344.32 343.44 346.5  351.88 355.2  358.16 354.54
 356.85 359.18 359.9  363.13 358.3  350.56 338.61 342.62 342.88 348.16
 353.21 349.31 352.12 359.56 360.   355.36 355.76 352.47 346.67 351.99]
>>> previous_close = c[-N - 1 : -1]
>>>
>>> print("len(previous_close)", len(previous_close))
len(previous_close) 5
>>> print("Previous close", previous_close)
Previous close [360.   355.36 355.76 352.47 346.67]
>>>
>>> true_range = np.maximum(h - l, h - previous_close, previous_close - l)
>>> print("True range", true_range)
True range [10.36  5.15  4.16  4.87  7.32]
>>>
>>> atr = np.zeros(N)
>>> atr[0] = np.mean(true_range)
>>> for i in range(1, N):
...     atr[i] = (N - 1) * atr[i - 1] + true_range[i]
...     atr[i] /= N
...
>>> atr
array([6.372    , 6.1276   , 5.73408  , 5.561264 , 5.9130112])
>>>
```

## 简单移动平均线

简单移动平均线（simple moving average）通常用于分析时间序列上的数据。为了计算它，我们需要定义一个N个周期的移动窗口，在我们的例子中即N个交易日。我们按照时间序列滑动这个窗口，并计算窗口内数据的均值。

### 计算简单移动平均线

移动平均线只需要少量的循环和均值函数即可计算得出，但使用 NumPy 还有更优的选择 —— `np.convolve` 函数。简单移动平均线只不过是计算与等权重的指示函数的卷积，当然，也可以是不等权重的。
