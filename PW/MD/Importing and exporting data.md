# Importing and exporting data

当我们从 CSV 文件读取数据（使用 `pd.read_csv`）或写入数据时转换为 CSV（使用 `df.to_csv`），我们可以从许多参数中进行选择，每个参数都会影响 CSV 的呈现形式：

- `sep`: 字段分隔符，默认情况下（可能很明显）是逗号但通常可以是制表符(`\t`)
- `header`: 是否有描述列名的标题，以及它们出现在文件的哪个行中
- `index_col`: 如果有的话，哪一列应该设置为我们数据框的索引
- `usecols`: 文件中的哪些列应该包含在数据框中

![read_csv 参数](../IMAGES/3-0.png)

## 数据框和 dtype

当我们从 CSV 文件读取数据时，pandas 会尝试推断每列的 `dtype`。请记住，CSV 文件实际上是文本文件，因此 pandas 必须检查数据以选择最佳 `dtype`。它将选择以下三种类型之一：

- 如果值都可以转换成整数，则选择 `int64`。
- 如果所有值都可以转换为浮点数（包括NaN），则选择 `float64`。
- 否则，它选择 `object`，即核心 Python 对象。

但是，让 pandas 以这种方式分析和选择数据存在几个问题。首先，虽然这些默认选择还不错，但对于许多值来说，它们可能过大。我们通常不需要 64 位数字，因此选择 `int64` 或 `float64` 会浪费内存。

第二个问题更加微妙：如果 pandas 要正确猜测列的 `dtype`，它必须检查该列中的所有值。但是，如果一列有数百万行，则该过程可能会占用大量内存。出于这个原因，`read_csv` 将文件分块读入内存，依次检查每个部分，然后从所有部分创建一个数据框。通常不会知道发生了什么；pandas 这样做是为了节省内存。

例如，如果 pandas 在文件顶部找到看起来像整数的值，而在文件底部找到看起来像字符串的值，则可能会导致问题。在这种情况下，最终会得到 `object` 的 `dtype` 和不同类型的值。

这几乎肯定是件坏事，pandas 会用 `DtypeWarning` 警告你。

避免这种混合数据类型问题的一种方法是告诉 pandas 不要吝惜内存，并且可以检查所有数据。您可以通过将 `False` 值传递给 `read_csv` 中的 `low_memory` 参数来实现这一点。默认情况下，`low_memory` 设置为 `True`，从而
导致我在此处描述的行为。

> 但请记住，将 `low_memory` 设置为 `False` 可能会占用大量内存，如果您的数据集很大，这可能是一个大问题。

更好的解决方案是告诉 pandas 不想让它猜测 `dtype` ，而是希望明确地告诉它。可以通过将 `dtype` 参数传递给 `read_csv` 来实现这一点，并将 Python 字典作为其参数。字典的键将是字符串，是从磁盘读取的列的名称，值将是想要使用的数据类型。通常使用来自 pandas 和 NumPy 的数据类型，但如果指定 `int` 或 `float`，pandas 将简单地使用 `np.int64` 或 `np.float64`。如果指定 `str`， pandas 将把数据存储为 Python 字符串，并分配 `object` 的 `dtype`。

```python
df_2019_jul = pd.read_csv(
    "../../data/nyc_taxi_2019-07.csv",
    usecols=["passenger_count", "total_amount", "payment_type"],
    dtype={
        "passenger_count": np.int8,
        "total_amount": np.float32,
        "payment_type": np.int8,
    },
)
```

最后，设置整数 `dtype` 往往很诱人。但请记住，如果列包含 `NaN`，则不能将其定义为整数 `dtype`。相反，需要将列读取为浮点数据，删除或插入 `NaN` 值，然后将列（使用 `astype`）转换为所需的整数类型。

## 字段分隔符和正则表达式

如果字段可以用 : 或 , 分隔，然后我们该怎么做？

Pandas 有一个很好的解决方案：如果 `sep` 包含多个字符，则将其视为正则表达式。因此，如果你想允许冒号或逗号，你可以传递 `[:,]` 分隔符。

通常情况下，pandas 使用 C 语言编写的库来解析 CSV 文件。如果字段分隔符使用正则表达式，它需要使用用 Python 编写的解析器，该解析器执行速度较慢且占用更多内存。考虑是否需要此功能以及基于 Python 的解析器造成的性能损失。

## JSON

毫无疑问，CSV 是一种重要、有用且流行的格式。但在某些方面，它已被另一种格式所取代：JSON，又称  JavaScript Object Notation。JSON 允许我们以文本格式存储数字、文本、列表和字典，这种格式可以用各种编程语言读取和写入，因为它更容易。由于 JSON 比 XML 更易于使用、更小、比 CSV 更具表现力，因此 JSON 成为存储和交换数据的常用格式也就不足为奇了。JSON 还成为互联网 API 的标准格式，使我们能够以跨平台的方式访问各种服务。

将 JSON 文件读入数据框并不困难；在这种情况下，它很容易。部分原因是这个特定的 JSON 文件是一个对象数组，或者 Python 人员称之为“字典列表”。当 `read_json` 看到这个文件时，它会将每个字典视为一条记录，并使用键作为列名。

> 在许多方面，读取这种 JSON 文件类似于使用字典列表创建数据框。
