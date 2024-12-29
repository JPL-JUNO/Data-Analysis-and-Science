# Excel 自动化

## 开始使用 xlwings

### 将 Excel 用作数据查看器

获得对数据的直观感受，一种方法是绘制图像，因为图像可以让你发现异常的数据。然而在某些时候，真正有用的是直接浏览数据表。你已经知道如何在 DataFrame 中使用 `to_excel` 方法,但还是有点儿麻烦：需要给 Excel 文件取一个名字，在文件系统中找到它，打开它，在对 DataFrame 进行修改后，需要关闭 Excel 文件然后再重新执行这个过程。一种更好的方法是执行 `df.to_clipboard()`，其可以将 DataFrame df 复制到剪贴板，这样你就可以把它粘贴到 Excel。不过还有一种更简单的方法，即使用 xlwings 中的 `view` 函数。

`view` 函数可以接受所有常见的 Python 对象，包括数字、字符串、列表、字典、元组、NumPy 数组和 pandas.DataFrame。在默认情况下，它会打开一个新的工作簿，然后将对象粘贴到第一张工作表的 A1 单元格。它甚至会通过 Excel 的自动适应功能来调整列宽。不必每次都打开一个新的工作簿，你也可以通过为 `view` 函数提供一个 xlwings sheet 对象作为第二个参数来重复利用同一个工作簿文件：`xw.view(df, mysheet)`。

### Excel 对象模型

当利用程序控制 Excel 时，你会和它的各种组件（比如工作簿或工作表）进行交互。这些组件以 Excel 对象模型的形式进行组织。Excel 对象模型是一种表示 Excel 图形用户界面的层次结构。

![xlwings 实现的 Excel 对象模型（部分）](../IMAGES/fig9-1.png)

- app 包含 book 的集合。
- book 包含 sheet 的集合。
- 通过 sheet 可以访问 range 对象和 charts 等集合。
- range 包含一个或多个连续的单元格作为其元素。

`Book` 让你可以新建工作簿并连接至现有的工作簿

|命令|描述|
|---|---|
|`xw.Book()`|返回代表活动的 Excel 实例中新的 Excel 工作簿的 book 对象。如果没有活动的 Excel 实例，则会启动一个|
|`xw.Book("Book1")`|返回表示未保存的名为 Book1（名称中不含文件扩展名）的工作簿的 book 对象|
|`xw.Book("Book1.xlsx")`|返回代表之前保存过的名为 Book1.xlsx（名称中包含文件扩展名）的工作簿的对象。该文件必须是已打开的，或者位于当前的工作目录|
|`xw.Book(r"C:\path\Book1.xlsx")`|返回代表之前保存过的工作簿（完整文件路径）的对象。该文件可以是打开的也可以是关闭的。路径字符串开头的 r 会将字符串转化为原始字符串，以使路径中的反斜杠（\）在 Windows 中按照字面进行解释。在 macOS 中，r 不是必需的，因为 macOS 的文件路径使用的是斜杠而不是反斜杠|
|`xw.books.active`|返回代表活动的 Excel 实例中活动的工作簿的 book 对象|

下面来看看如何从 `book` 对象开始沿着 Excel 对象模型的层次结构一路向下到 `range` 对象：

```python
book = xw.Book()
sheet1 = book.sheets[0]
# sheet1 = book.sheets['Sheet1']
sheet1.range("A1")
```

有了 range 对象之后，就到达了 Excel 对象模型的最底层。在尖括号之间打印的字符串向你提供了该对象的一些有用的信息，但要真正利用它们完成一些工作，通常需要访问它们的属性。

```python
sheet1.range('A1').value = [[1, 2], [3, 4]]
sheet1.range('A4').value = 'Hello!'
```

在默认情况下，xlwings 的 `range` 对象在接受单个单元格作为参数时，其 `value` 属性返回的是一个标量；在接受二维区域作为参数时，返回的是一个嵌套列表。

下表是对 xlwings 的 range 可接受的字符串格式总结。

|引用|描述|
|---|---|
|`"A1"`|单个单元格|
|`"A1:B2"`|从 A1 到 B2 的单元格区域|
|`"A:A"`|A 列|
|`"A:B"`|A 列到 B 列|
|`"1:1"`|1 行|
|`"1:2"`|1 行到 2 行|

也可以对 xlwings 的 `range` 对象进行索引和切片，通过观察尖括号之间的地址（打印出来的字符串表示）来确认你最终会得到怎样的单元格区域：

```python
>>> sheet1.range('A1:B2')[0, 0]
<Range [Book2]Sheet1!$A$1>
>>> sheet1.range('A1:B2')[:, 1]
<Range [Book2]Sheet1!$B$1:$B$2>
```

除了显式地使用 `sheet` 对象的 `range` 属性，也可以通过对 `sheet` 对象进行索引和切片来获得一个 `range` 对象。利用 A1 表示法可以让你少敲些字，而使用整数切片可以让 Excel 工作表看起来像 NumPy 数组。

不过，有时候通过引用区域左上角和右下角的元素来定义一个区域可能更直观。

```python
>>> sheet1[9, 3]
<Range [Book2]Sheet1!$D$10>
>>> sheet1.range((10, 4))
<Range [Book2]Sheet1!$D$10>
>>> sheet1[9:11, 3:6]
<Range [Book2]Sheet1!$D$10:$F$11>
>>> sheet1.range((10, 4), (11, 6))
<Range [Book2]Sheet1!$D$10:$F$11>
```

> **从 0 开始的索引和从 1 开始的索引**
>
> 作为一个 Python 包，只要你通过 Python 的索引或切片语法（通过方括号）访问元素，xlwings 就始终使用从 0 开始的索引。不过 xlwings 的 `range` 对象使用的是和 Excel 一样从 1 开始的行列索引。和 Excel 的用户接口采用同样的行列索引在某些时候是有利的。如果你更喜欢使用 Python 的从 0 开始的索引，那么可以直接使用 `sheet[row_selection, column_selection]` 语法。

下面的示例展示了如何从一个 `range` 对象（`sheet["A1"]`）自底向上得到 `app` 对象。要记住 `app` 对象代表的是 Excel 实例（尖括号之间的输出代表的是 Excel 的进程 ID）。

```python
>>> sheet1['A1'].sheet.book.app
<App [excel] 15304>
```

如果你想在多个 Excel 实例中打开同一个工作簿，或是出于性能方面的原因想要将多个工作簿分发给多个实例，那么就需要显式地使用 `app` 对象。`app` 对象的另一个常见用例是在隐藏的 Excel 实例中打开工作簿：这样你就可以在后台运行 xlwings 脚本且同时在 Excel 中完成其他工作。

如果你在两个 Excel 实例中打开了同一个工作簿，或者想要指定某个 Excel 实例打开某个工作簿，就不能再使用 `xw.book` 了。此时需要使用下表中列出的 `books` 集合。注意，`myapp` 代表一个 xlwings `app` 对象。如果将 `myapp.books` 替换成 `xw.books`，则 xlwings 会使用活动的 `app`。

|命令|描述|
|---|---|
|`myapp.books.add()`|在 myapp 引用的 Excel 实例中创建一个新的 Excel 工作簿并返回对应的 `book` 对象|
|`myapp.books.open(r"C:\path\Book.xlsx")`|如果对应的 `book` 对象已打开就直接返回该对象，否则应该首先在 `myapp` 引用的 Excel 实例中打开该工作簿。记住，字符串开头的 r 会将文件路径转化为原始字符串，从而可以按字面意思解释反斜杠|
|`myapp.books["Book1.xlsx"]`|如果对应的工作簿已打开就直接返回该 `book` 对象。如果尚未打开则会引发 `KeyError` 错误。一定要使用文件名而非完整路径。如果你想知道一个工作簿是否已经在 Excel 中打开，就可以使用该命令|

### 运行 VBA 代码

## 转换器、选项和集合

### 处理DataFrame

将 DataFrame 写入 Excel 与将标量或嵌套列表写入 Excel 并无二致：只需将 DataFrame 赋值给 Excel 区域的左上角单元格即可。

如果你想去掉列标题或索引（也可以同时去掉两者），那么可以像下面这样使用 `options` 方法：

```python
sheet1['B10'].options(header=False, index=False).value = df
```

要将 Excel 区域以 DataFrame 的形式读取，需要将 DataFrame 类传递给 `options` 方法的 `convert` 参数。在默认情况下，你的数据必须同时具备标题和索引，但是你可以通过 `index` 参数和 `header` 参数来改变这种行为。除了使用转换器，还可以将这些值读取为嵌套列表，然后手动构造 DataFrame。不过使用转换器可以更方便地处理索引和标题。

### 转换器和选项

xlwings `range` 对象的 `options` 方法修改的是读写 Excel 文件时处理值的方式。也就是说，只有在你调用 `range` 对象的 `value` 属性时，`options` 才会进行求值。它的语法如下（其中 `myrange` 是一个 xlwings `range` 对象）：

```python
myrange.options(convert=None, option1=value1, option2=value2, ...).value
```

下表展示了内置的转换器，即 convert 参数可以接受的值。这些转换器之所以被称为内置的，是因为 xlwings 还提供了编写自定义转化器的方法。如果你在写入值之前或读取值之后一次又一次地进行了额外的转换工作，那么能够自己编写转换器是不错的。

|转换器|描述|
|---|---|
|`dict`|未发生嵌套的简单字典，即 `{key1: value1, key2: value2, ...}` 的形式|
|`np.array`|NumPy 数组，需要 `import numpy as np`|
|`pd.Series`|pandas Series，需要 `import pandas as pd`|
|`pd.DataFrame`|pandas DataFrame，需要 `import pandas as pd`|

下表展示了内置选项

|选项|描述|
|---|---|
|`empty`|在默认情况下，空单元格会被读取为 `None`。为 `empty` 参数提供一个值以改变默认值|
|`date`|接受一个函数，该函数会应用到来自按日期格式化的单元格的值|
|`numbers`|接受一个函数，该函数会应用到数值|
|`ndim`|**维数**：`ndim` 可以强制一个区域的值达到某个维度。只能取 `None`、1 和 2 中的一个值。仅在以列表或 NumPy 数组形式读取值时可用|
|`transpose`|将值转置，即把行和列对换|
|`index`|用于 pandas DataFrame 和 pandas Series：在读取时用来定义 Excel 区域是否包含该索引。可以为 `True`/`False` 或整数。整数定义了有多少列会被转化为 `MultiIndex`。例如，2 会使用最左边的两列作为索引。在写入时，你可以通过将 `index` 设置为 `True` 或 `False` 来决定是否要写入索引|
|`header`|类似于 `index`，应用于列标题|

来仔细看一下 `ndim`：在默认情况下，从 Excel 中读取单个单元格时，你会得到一个标量（比如浮点数或字符串）；当读取一行或一列时，你得到的是一个简单列表；当读取一个二维区域时，你得到的是一个嵌套（二维）列表。这样的行为是自洽的，并且和 NumPy 数组切片的行为也是一致的。但一维的情况很特殊：有时候一列可能只是二维区域的特殊情况，在这种情况下，可以用 `ndim=2` 来强制区域的维度为 2。

`ndim=1` 会强制让读到的单个单元格的值生成列表而非标量。在使用 pandas 时无须使用 `ndim` 参数，因为 DataFrame 都是二维的，而 Series 都是一维的。

### 图表、图片和已定义名称

1. Excel 图表
使用 `charts` 集合的 `add` 方法来添加一张新的图表并为其设置图表类型和源数据。

2. 图片：Matplotlib 图像
当你使用 pandas 的默认绘图后端时，你创建的是一张 Matplotlib 的图像。要将这样的图像放进 Excel 中，首先要获取它的 `figure` 对象，然后将其作为参数传递给 `pictures.add`，`pictures.add` 会将 Matplotlib 图像转换为图片然后发送至 Excel。

要想使用新的图像来更新图片，只需调用 `update` 方法并传递另一个 `figure` 对象即可。虽然这样做会替换 Excel 中的图片，但会保留位置、尺寸、名称。

> **确保已安装 Pillow**
>
> 在处理图片时，一定要确保安装了 Pillow，它是 Python 中常用的图片处理库。Pillow 能够保证图片在 Excel 中有正确的尺寸和比例。Anaconda 中包含了 Pillow，所以如果你用的是其他发行版，则需要通过 `conda install pillow` 或者 `pip install pillow` 进行安装。注意，除了接受 Matplotlib 图像，`pictures.add` 也可以接受磁盘上的图片路径。

图表集合（charts）和图片（pictures）集合都可以通过 `sheet` 对象访问。
