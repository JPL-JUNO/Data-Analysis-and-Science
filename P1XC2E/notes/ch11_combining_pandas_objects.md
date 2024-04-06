# 组合 pandas 对象

有多种选项可用于将两个或多个 DataFrame 或 Series 组合在一起。`append` 是最不灵活的，只允许将新行追加到 DataFrame 中。`concat` 方法非常通用，可以在任一轴上组合任意数量的 DataFrame 或 Series。`join` 方法通过将一个 DataFrame 的列与其他 DataFrame 的索引对齐来提供快速查找。`merge` 方法提供了类似 SQL 的功能来将两个 DataFrame 连接在一起。

## 向 DataFrames 中追加新行

执行数据分析时，创建新列比创建新行更为常见。这是因为新的一行数据通常代表一个新的观察结果，而作为分析师，持续捕获新数据通常不是你的工作。数据捕获通常留给其他平台，例如关系数据库管理系统。尽管如此，这是一个必须了解的功能，因为它会时不时地出现。

目前首先使用 `.loc` 属性将行附加到一个小数据集，然后过渡到使用 `.append` 方法。

```python
import pandas as pd
import numpy as np

names = pd.read_csv('../data/names.csv')
names
```

```python
new_data_list = ['Aria', 1]
names.loc[4] = new_data_list
names.loc['five'] = ['Zach', 3]
names.loc[len(names)] = {'Name': 'Zayd', 'Age': 2}
names.loc[len(names)] = pd.Series({'Age': 32, 'Name': 'Dean'})
```

![names](../csdn/result1.png)

前面的操作都使用 `.loc` 属性来就地更改名称 DataFrame。没有返回 DataFrame 的单独副本。接下来，我们将查看 `.append` 方法，该方法不会修改调用的 DataFrame。相反，它返回带有附加行的 DataFrame 的新副本。`.append` 的第一个参数必须是另一个 DataFrame、Series、字典以及 DataFrame 或 Series 组成的列表。让我们看看当我们尝试将字典与 `.append` 一起使用时会发生什么：

```python
names = pd.read_csv('../data/names.csv')
names.append({'Name': 'Aria', 'Age': 1})

FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version.
Traceback (most recent call last)
...
TypeError: Can only append a dict if ignore_index=True
```

此错误消息似乎有点不正确。我们传递的是 dict 而不是 Series，但尽管如此，它还是给了我们如何纠正它的说明，我们需要传递 `ignore_index = True` 参数。

这是可行的，但 `ignore_index` 是一个有副作用的参数。当设置为 `True` 时，旧索引将被完全删除并替换为从 `0` 到 `n-1` 的 `RangeIndex`。

让我们使用 `.append` 方法附加一个具有 name 属性的 Series：

```python
names.index = ['Canada', 'Canada', 'USA', 'USA']
s = pd.Series({'Name': 'Zach', 'Age': 3}, name=len(names))
names.append(s)
```

这里 name 的属性是必须指明的，否则与传递一个字典无异（报错）。逻辑在于，pandas 必须要知道索引名，否则没有办法建立索引，当然，可以设置 `ignore_index = True`:scream:。

`.append` 方法比 `.loc` 属性更灵活。它支持同时追加多行。实现此目的的一种方法是传递 Series 列表：

```python
s1 = pd.Series({'Name': 'Zach', 'Age': 3}, name=len(names))
s2 = pd.Series({'Name': 'Zayd', 'Age': 2}, name='USA')

names.append([s1, s2])
```

可以看到，这里的字段名都是我们自动手动在字典中输入的，这对于仅有两个字段的小数据集没什么关系。但是一旦数据集的字典增加，这将非常糟糕。

```python
bball_16 = pd.read_csv('../data/baseball16.csv')
assert bball_16.shape == (16, 22)
```

该数据集包含 22 列，如果你手动输入新的数据行，很容易输错列名或完全忘记列名。为了帮助防止这些错误，让我们选择一行作为 Series 并将 `.to_dict` 方法链接到它以获取全部的字段名与值：

```python
>>> data_dict = bball_16.iloc[0].to_dict()
>>> data_dict
{'playerID': 'altuvjo01', 'yearID': 2016, 'stint': 1, 'teamID': 'HOU', 'lgID': 'AL', 'G': 161, 'AB': 640, 'R': 108, 'H': 216, '2B': 42, '3B': 5, 'HR': 24, 'RBI': 96.0, 'SB': 30.0, 'CS': 10.0, 'BB': 60, 'SO': 70.0, 'IBB': 11.0, 'HBP': 7.0, 'SH': 3.0, 'SF': 7.0, 'GIDP': 15.0}
>>>
```

使用字典理解清除旧值，将任何先前的字符串值指定为空字符串，将所有其他值指定为缺失值。该字典现在可以用作你想要输入的任何新数据的模板：

```python
new_data_dict = {k: "" if isinstance(v, str) else np.nan for k, v in data_dict.items()}
new_data_dict
```

这种方法应该不到万不得已不会使用吧:confused:。

## 将多个 DataFrame 连接在一起

`concat` 函数可以将两个或多个 DataFrame（或 Series）垂直和水平连接在一起。像往常一样，当同时处理多个 pandas 对象时，串联不会随意发生，而是按索引对齐每个对象。

这里，我们使用 `concat` 函数将 DataFrame 水平和垂直组合起来，然后更改参数值以产生不同的结果。
