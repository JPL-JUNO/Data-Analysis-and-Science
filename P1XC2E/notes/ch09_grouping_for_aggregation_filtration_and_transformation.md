# 聚合、过滤和转换分组

## 介绍

数据分析过程中最基本的任务之一涉及将数据分成独立的组，然后对每个组进行计算。这种方法已经存在相当长一段时间了，但最近被称为“拆分-应用-组合”。这里将介绍强大的 `.groupby` 方法，它允许你以任何可以想象的方式对数据进行分组，并在返回单个数据集之前将任何类型的函数独立地应用于每个组。

所有基本的 groupby 操作都有分组列，这些列中值的每个唯一组合都代表数据的独立分组。语法如下：

```python
df.groupby(['list', 'of', 'grouping', 'columns'])
df.groupby('single_column') # when grouping by a single column
```

`.groupby` 方法最常见的用途是执行**聚合**（aggregation）。什么是聚合？当许多输入的序列被汇总或组合成单个值输出时，就会发生聚合。例如，对列的所有值求和或找到其最大值是应用于数据序列的聚合。聚合采用一个序列并将其减少为单个值。

## 定义一个聚合

这里我们对数据集并执行最简单的聚合，仅涉及单个分组列、单个聚合列和单个聚合函数。

```python
>>> import pandas as pd
>>> import numpy as np
>>> flights = pd.read_csv("../data/flights.csv")
>>> 
```

### 怎么做

定义分组列 (AIRLINE)、聚合列 (ARR_DELAY) 和聚合函数 (mean)。将分组列放入 `.groupby` 方法中，然后使用将聚合列与其聚合函数配对的字典来调用 `.agg` 方法。如果你传入一个字典，它会返回一个 DataFrame 实例：

```python
>>> flights.groupby("AIRLINE").agg({"ARR_DELAY": "mean"})
         ARR_DELAY
AIRLINE
AA        5.542661
AS       -0.833333
B6        8.692593
DL        0.339691
EV        7.034580
F9       13.630651
HA        4.972973
MQ        6.860591
NK       18.436070
OO        7.593463
UA        7.765755
US        1.681105
VX        5.348884
WN        6.397353
>>>
```

或者，你可以将聚合列放在索引运算符中，然后将聚合函数作为字符串传递给 `.agg`。这将返回一个 Series：

```python
>>> flights.groupby("AIRLINE")["ARR_DELAY"].agg("mean")
AIRLINE
AA     5.542661
AS    -0.833333
B6     8.692593
DL     0.339691
EV     7.034580
F9    13.630651
HA     4.972973
MQ     6.860591
NK    18.436070
OO     7.593463
UA     7.765755
US     1.681105
VX     5.348884
WN     6.397353
Name: ARR_DELAY, dtype: float64
>>>
```

上面使用的字符串名称是 pandas 为你提供引用特定聚合函数的便利。 你可以将任何聚合函数直接传递给 `.agg` 方法，例如 NumPy `np.mean` 函数。pandas 中提供的聚合方法是优化过的，效率更高。

```python
flights.groupby("AIRLINE")["ARR_DELAY"].agg(np.mean)
```

在这种情况下，可以完全掠过 agg 方法并直接使用调用方法。

```python
flights.groupby("AIRLINE")["ARR_DELAY"].mean()
```

`.groupby` 方法的语法不像其他方法那么直接。他首先生成一个全新的中间对象，具有自己独特的属性和方法。此阶段不进行任何计算。pandas 仅验证分组列。该 `groupby` 对象有一个 .agg 方法来执行聚合。使用此方法的方法之一是向其传递一个字典，将聚合列映射到聚合函数。

```python
>>> grouped = flights.groupby("AIRLINE")
>>> type(grouped)
<class 'pandas.core.groupby.generic.DataFrameGroupBy'>
>>>
```

最后展示了一种语法风格。当你仅应用一个聚合函数时，你通常可以直接将其作为 `groupby` 对象本身的方法调用，而无需使用 `.agg`。并非所有聚合函数都有等效的方法，但大多数都有。

### 更多 1

如果你在 `.agg` 中使用的不是聚合函数，pandas 会引发异常。

```python
>>> flights.groupby("AIRLINE")["ARR_DELAY"].agg(np.sqrt)
... output ignored ...
ValueError: Must produce aggregated value
>>>
```

## 使用多个列和函数进行分组和聚合

可以对多个列进行分组和聚合，其语法与使用单列进行分组和聚合的语法略有不同，但与任何类型的分组操作一样，它有助于相同的三个组件：分组列、聚合列和聚合函数。

通过下面的三个问题来体现多分组列，多聚合列和聚合函数的灵活性：

- 查找每个工作日每个航空公司取消的航班数量
- 查找每家航空公司每个工作日取消和改道航班的数量和百分比
- 对于每个出发地和目的地，查找航班总数、取消航班的数量和百分比以及飞行时间的平均值和方差

```python
flights.groupby(["AIRLINE", "WEEKDAY"])["CANCELLED"].agg("sum")

flights.groupby(["AIRLINE", "WEEKDAY"])[["CANCELLED", "DIVERTED"]].agg(["sum", "mean"])

flights.groupby(["ORG_AIR", "DEST_AIR"]).agg(
    {"CANCELLED": ["sum", "mean", "size"], "AIR_TIME": ["mean", "var"]}
)
```

想要手动来计算，也可以使用 `named aggregation` 对象来避免多层级列：

```python
flights.groupby(["ORG_AIR", "DEST_AIR"]).agg(
    sum_cancelled=pd.NamedAgg(column="CANCELLED", aggfunc="sum"),
    mean_cancelled=pd.NamedAgg(column="CANCELLED", aggfunc="mean"),
    size_cancelled=pd.NamedAgg(column="CANCELLED", aggfunc="size"),
    mean_air_time=pd.NamedAgg(column="AIR_TIME", aggfunc="mean"),
    var_air_time=pd.NamedAgg(column="AIR_TIME", aggfunc="var"),
)
```

### 如何实现的

要想按多列进行分组，我们将字符串名称列表传递给 .groupby 方法。AIRLINE 和 WEEKDAY 的每个不同组合都形成自己的组。在每个组中，计算已取消航班的总和，然后作为 Series 返回。

针对问题 2，按航空公司和工作日进行分组，但这次聚合了两列。它使用字符串 sum 和mean 将两个聚合函数中的每一个应用于每列，从而每组返回四个列。

针对问题 3 更进一步，使用字典将特定聚合列映射到不同的聚合函数。请注意，`size` 聚合函数返回每组的总行数。这与 `count` 聚合函数不同，`count` 聚合函数返回每组非缺失值的数量。

额外使用 `named aggregations` 创建了单层列（非多级列，与多级索引类似）的新语法。

### 更多 2

展平多级列可以使用 `.to_flat_index` 方法

```python
>>> res = flights.groupby(["ORG_AIR", "DEST_AIR"]).agg(
...     {"CANCELLED": ["sum", "mean", "size"], "AIR_TIME": ["mean", "var"]}
... )
>>> res.columns = ["_".join(x) for x in res.columns.to_flat_index()]
>>> res.head()
                  CANCELLED_sum  CANCELLED_mean  CANCELLED_size  AIR_TIME_mean  AIR_TIME_var
ORG_AIR DEST_AIR
ATL     ABE                   0             0.0              31      96.387097     45.778495
        ABQ                   0             0.0              16     170.500000     87.866667
        ABY                   0             0.0              19      28.578947      6.590643
        ACY                   0             0.0               6      91.333333     11.466667
        AEX                   0             0.0              40      78.725000     47.332692
>>>
```

如果觉得这有点难看，可以使用链式操作来展平列。可惜，`.reindex` 方法不支持展平。作为替代，我们必须利用 `.pipe` 方法：

```python
>>> def flatten_cols(df):
...     df.columns = ["_".join(x) for x in df.columns.to_flat_index()]
...     return df
...
>>>
>>> res = (
...     flights.groupby(["ORG_AIR", "DEST_AIR"])
...     .agg({"CANCELLED": ["sum", "mean", "size"], "AIR_TIME": ["mean", "var"]})
...     .pipe(flatten_cols)
... )
>>>
```

这里还有一点需要注意，当对多个列进行分组时，pandas 会创建分层索引或者叫多重索引。在前面的示例中，它返回 1,130 行。但是，如果我们分组的其中一列是分类的（并且具有 `category` 类型，而不是 `object` 类型），则 pandas 将为每个级别创建所有组合的笛卡尔积。在本例中，它返回 2,710 行：

```python
>>> res = (
...     flights.assign(ORG_AIR=flights.ORG_AIR.astype("category"))
...     .groupby(["ORG_AIR", "DEST_AIR"])
...     .agg({"CANCELLED": ["sum", "mean", "size"], "AIR_TIME": ["mean", "var"]})
... )
>>> res.shape
(2710, 5)
>>>
```

要避免分组的组合过多，可以使用 `observed=True` 参数，这将使得分类分组的工作方式类似于字符串类型的分组，并且仅显示观察到的值，而不显示笛卡尔积：

```python
>>> res = (
...     flights.assign(ORG_AIR=flights.ORG_AIR.astype("category"))
...     .groupby(["ORG_AIR", "DEST_AIR"], observed=True)
...     .agg({"CANCELLED": ["sum", "mean", "size"], "AIR_TIME": ["mean", "var"]})
... )
>>> res.shape
(1130, 5)
>>>
```

## 分组后删除 `MultiIndex`

当使用 `groupby` 时，不可避免地会创建一个 `MultiIndex`。多重索引可以发生在索引和列中。具有多索引的 DataFrame 更难以定位，并且偶尔也会出现令人困惑的列名称。

这里，我们使用 .groupby 方法执行聚合，以创建一个具有行和列 `MultiIndex` 的 DataFrame。然后，我们操作索引，使其具有单一级别并且列名具有描述性。

```python
airline_info = (
    flights.groupby(["AIRLINE", "WEEKDAY"])
    .agg({"DIST": ["sum", "mean"], "ARR_DELAY": ["min", "max"]})
    .astype(int)
)
airline_info
```

这里的 `airline_info` 行和列都由具有两个级别的 MultiIndex 标记。让我们将两者压缩为一个级别。我们使用 MultiIndex 方法 `.to_flat_index`。首先我们显示每个级别的输出，然后连接两个级别，然后将其设置为新的列值：

```python
>>> airline_info.columns.get_level_values(0)
Index(['DIST', 'DIST', 'ARR_DELAY', 'ARR_DELAY'], dtype='object')
>>> airline_info.columns.get_level_values(1)
Index(['sum', 'mean', 'min', 'max'], dtype='object')
>>> airline_info.columns.to_flat_index()
Index([('DIST', 'sum'), ('DIST', 'mean'), ('ARR_DELAY', 'min'),
       ('ARR_DELAY', 'max')],
      dtype='object')
>>>
>>> airline_info.columns = ["_".join(x) for x in airline_info.columns.to_flat_index()]
>>> airline_info.columns
Index(['DIST_sum', 'DIST_mean', 'ARR_DELAY_min', 'ARR_DELAY_max'], dtype='object')
>>>
```

解决行 `MultiIndex` 的快速方法是使用 `.reset_index` 方法：

```python
airline_info.reset_index()
```

当然，可以手动用 `NamedAgg` 对象，并调用 `reset_index`。

### 更多3

默认情况下，在 `groupby` 操作结束时，pandas 将所有分组列放入索引中。`.groupby` 方法中的 `as_index` 参数可以设置为 False 以避免这种行为。

```python
>>> flights.groupby(["AIRLINE"], as_index=False)["DIST"].agg("mean").round(0)
   AIRLINE    DIST
0       AA  1114.0
1       AS  1066.0
2       B6  1772.0
3       DL   866.0
4       EV   460.0
5       F9   970.0
6       HA  2615.0
7       MQ   404.0
8       NK  1047.0
9       OO   511.0
10      UA  1231.0
11      US  1181.0
12      VX  1240.0
13      WN   810.0
>>>
```

默认情况下，pandas 对分组列进行排序。`sort` 参数存在于 `.groupby` 方法中，默认为 `True`。 你可以将其设置为 `False` 以保持分组列的顺序与它们在数据集中遇到的顺序相同。通过不对数据进行排序，性能会略有提高。

```python
flights.groupby(["AIRLINE"], as_index=False, sort=False)["DIST"].agg("mean").round(0)
```

## 自定义聚合函数

pandas 提供了许多与 groupby 对象一起使用的聚合函数。在某些时候，你可能需要编写自己的自定义用户定义函数，但 pandas 或 NumPy 中不存在该函数。

```python
college = pd.read_csv("../data/college.csv")
```

假设我们想找到每个分组中，偏离标准差的最大程度是多少？pandas 没有提供这个聚合函数，这就需要我们自己编写自定义聚合函数来操作。

```python
>>> def max_deviation(s):
...     std_score = s - s.mean() / s.std()
...     return std_score.abs().max()
...
>>>
>>> college.groupby("STABBR")["UGDS"].agg(max_deviation).round(1)
STABBR
AK     12864.4
AL     29850.4
AR     21404.5
AS         NaN
AZ    151557.7
... 省略一些行 ...
```

你会注意到函数名称被放置在 `.agg` 方法内，而不是直接被调用。参数 `s` 没有显式传递给 `max_deviation`。相反，pandas 隐式地将 `UGDS` 列作为 Series 传递给 `max_deviation`。每个组都会调用一次 `max_deviation` 函数。 由于 s 是一个 Series ，因此所有普通 Series 方法都可用。

当然也可以将自定义函数应用于多个聚合列：

```python
>>> college.groupby("STABBR")[["UGDS", "SATVRMID", "SATMTMID"]].agg(max_deviation).round(1)
            UGDS  SATVRMID  SATMTMID
STABBR
AK       12864.4       NaN       NaN
AL       29850.4     585.7     581.4
AR       21404.5     589.8     586.7
... 省略一些行 ...
```

也可以使用自定义函数与预置函数：

```python
>>> college.groupby("STABBR")[["UGDS", "SATVRMID", "SATMTMID"]].agg(
...     [max_deviation, "mean", "std"]
... ).round(1)
                UGDS                       SATVRMID                    SATMTMID
       max_deviation    mean      std max_deviation   mean    std max_deviation   mean    std
STABBR
AK           12864.4  2493.2   4051.7           NaN  555.0    NaN           NaN  503.0    NaN
AL           29850.4  2789.9   4657.9         585.7  508.5   54.5         581.4  504.3   58.9
AR           21404.5  1644.1   3142.8         589.8  491.9   48.3         586.7  515.9   38.8
AS               NaN  1276.0      NaN           NaN    NaN    NaN           NaN    NaN    NaN
... 省略一些行 ...
```

请注意，pandas 使用函数的名称作为返回列的名称。你可以直接使用 .rename 方法更改列名，也可以修改函数属性 `.__name__`：

```python
>>> max_deviation.__name__
'max_deviation'
>>> max_deviation.__name__ = "Max Deviation"
>>> college.groupby("STABBR")[["UGDS", "SATVRMID", "SATMTMID"]].agg(
...     [max_deviation, "mean", "std"]
... ).round(1)
                UGDS                       SATVRMID                    SATMTMID
       Max Deviation    mean      std Max Deviation   mean    std Max Deviation   mean    std
STABBR
AK           12864.4  2493.2   4051.7           NaN  555.0    NaN           NaN  503.0    NaN
AL           29850.4  2789.9   4657.9         585.7  508.5   54.5         581.4  504.3   58.9
AR           21404.5  1644.1   3142.8         589.8  491.9   48.3         586.7  515.9   38.8
AS               NaN  1276.0      NaN           NaN    NaN    NaN           NaN    NaN    NaN
... 省略一些行 ...
```

## 带有 `*args` 和 `**kwargs` 的自定义聚合函数

当编写你自己的用户定义的自定义聚合函数时，pandas 会隐式地将每个聚合列一次作为一个 Series 传递给它。有时，你需要向函数传递更多参数，而不仅仅是 Series 本身。 为此，你需要了解 Python 向函数传递任意数量的参数的能力。

`.agg` 的签名是 `agg(func, *args, **kwargs)`。`func` 参数是一个归约函数、归约方法的字符串名称、归约函数列表或将列映射到函数或函数列表的字典。如果您有一个需要使用其他参数的归约函数，则可以利用 `*args` 和 `**kwargs` 参数将参数传递给归约函数。您可以使用 `*args` 将任意数量的位置参数传递给自定义聚合函数。同样，`**kwargs` 允许您传递任意数量的关键字参数。

这里的例子是我们将为大学数据集构建一个自定义函数，用于查找按州和宗教信仰划分的本科生人数，其值介于两个值之间的学校百分比。
