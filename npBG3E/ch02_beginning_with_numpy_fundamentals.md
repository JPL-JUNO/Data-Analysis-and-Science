# NumPy 基础

## NumPy 数组对象

NumPy 中的 ndarray 是一个多维数组对象，该对象由两部分组成：

- 实际的数据；
- 描述这些数据的元数据（metadata）。

大部分的数组操作仅仅修改元数据部分，而不改变底层的实际数据。

NumPy 数组一般是同质的（但有一种特殊的数组类型例外，它是异质的），即数组中的所有元素类型必须是一致的。这样有一个好处：如果我们知道数组中的元素均为同一类型，该数组所需的存储空间就很容易确定下来。

与 Python 一样，NumPy 数组的下标也是从 0 开始的。数组元素的数据类型用专门的对象表示。

数组的 `shape` 属性返回一个元组（tuple），元组中的元素即为 NumPy 数组每一个维度上的大小。

## 动手实践：创建多维数组

```python
>>> m = np.array([np.arange(2), np.arange(2)])
>>> m
array([[0, 1],
       [0, 1]])
>>> m.shape
(2, 2)
>>>
```

`np.array` 函数可以依据给定的对象生成数组。给定的对象应是类数组，如 Python 中的列表。像这样的类数组对象是 `np.array` 函数的唯一必要参数，其余的诸多参数均为有默认值的可选参数。第二个常用的参数应该是 `dtype`。

### 选取数组元素

有时候，我们需要选取数组中的某个特定元素。可以一次选取数组中的每个元素，尽管我觉得这不常用。需要注意的是，数组的下标是从 0 开始的。

```python
>>> a = np.array([[1, 2], [3, 4]])
>>> a
array([[1, 2],
       [3, 4]])
>>> a[0, 0]
1
>>> a[0, 1]
2
>>> a[1, 0]
3
>>> a[1, 1]
4
>>>
```

对于数组 `a`，只需要用 `a[m,n]` 选取各数组元素，其中 `m` 和 `n` 为元素下标。

### NumPy 数值类型

Python 支持的数据类型有整型、浮点型以及复数型，但这些类型不足以满足科学计算的需求，因此 NumPy 添加了很多其他的数据类型。在实际应用中，我们需要不同精度的数据类型，它们占用的内存空间也是不同的。

|类 型| 描 述|
|---|---|
|bool |用一位存储的布尔类型（值为 TRUE 或 FALSE）|
|inti |由所在平台决定其精度的整数（一般为 int32 或 int64）|
|int8 |整数，范围为 -128 至 127|
|int16 |整数，范围为 -32768 至 32767|
|int32 |整数，范围为 -$2^{31}$ 至 $2^{31}$ -1|
|int64 |整数，范围为 -$2^{63}$ 至 $2^{63}$ -1|
|uint8 |无符号整数，范围为 0 至 255|
|uint16 |无符号整数，范围为 0 至 65535|
|uint32 |无符号整数，范围为 0 至 $2^{32}$-1|
|uint64 |无符号整数，范围为 0 至 $2^{64}$-1|
|float16 |半精度浮点数（16 位）：其中用 1 位表示正负号，5 位表示指数，10 位表示尾数|
|float32 |单精度浮点数（32 位）：其中用 1 位表示正负号，8 位表示指数，23 位表示尾数|
|float64或float |双精度浮点数（64 位）：其中用1位表示正负号，11 位表示指数，52 位表示尾数|
|complex64 |复数，分别用两个 32 位浮点数表示实部和虚部|
|complex128或complex |复数，分别用两个 64 位浮点数表示实部和虚部|

对于浮点类型，我们可以使用 `finfo()` 函数获取信息：

```python
>>> np.finfo(np.float32)
finfo(resolution=1e-06, min=-3.4028235e+38, max=3.4028235e+38, dtype=float32)
>>>
```

每一种数据类型均有对应的类型转换函数：

```python
>>> np.float64(False)
0.0
>>> np.float64(42)
42.0
>>> np.int8(42.0)
42
>>> np.bool_(42)
True
>>> np.bool_(0)
False
>>> np.bool_(42.0)
True
>>> np.float64(True)
1.0
>>> np.float64(False)
0.0
>>>
```

在 NumPy 中，许多函数的参数中可以指定数据类型，通常这个参数是可选的：

```python
>>> np.arange(7, dtype=np.uint8)
array([0, 1, 2, 3, 4, 5, 6], dtype=uint8)
>>>
```

需要注意的是，复数是不能转换为整数或者浮点，这将触发 `TypeError` 错误：

```python
>>> np.int16(42.0 + 1.0j)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>>
```

不过，浮点数却可以转换为复数。

```python
>>> np.complex64(1.0)
(1+0j)
>>>
```

### 数据类型对象

数据类型对象是 `numpy.dtype` 类的实例。如前所述，NumPy 数组是有数据类型的，更确切地说，NumPy 数组中的每一个元素均为相同的数据类型。数据类型对象可以给出单个数组元素在内存中占用的字节数，即 `dtype` 类的 `itemsize` 属性：

```python
>>> a.dtype.itemsize
4
>>>
```

### 用字符指定数据类型

NumPy 可以使用字符来表示数据类型，这是为了兼容 NumPy 的前身 Numeric。不推荐使用字符，但有时会用到，因此下面还是列出了字符编码的对应表。应该优先使用 dtype 对象来表示数据类型，而不是这些字符编码。

|数据类型 |字符|
|---|---|
|整数| i|
|无符号整数 |u|
|单精度浮点数 |f|
|双精度浮点数 |d|
|布尔值 |b|
|复数| D|
|字符串| S|
|unicode 字符串| U|
|void（空）| V|

```python
>>> np.arange(7, dtype="f")
array([0., 1., 2., 3., 4., 5., 6.], dtype=float32)
>>> np.arange(7, dtype="D")
array([0.+0.j, 1.+0.j, 2.+0.j, 3.+0.j, 4.+0.j, 5.+0.j, 6.+0.j])
>>>
```

### 数据类型构造函数

Python 类具有函数，如果它们属于一个类，则称为**方法**。其中一些方法很特殊，用于创建新对象。这些专门的方法称为**构造函数**。有很多的方法来创建一个数据类型，这里以浮点数为例：

```python
>>> np.dtype(float)  # Use the general Python float
dtype('float64')
>>> np.dtype("f")  # Specify a single precision float with a character code
dtype('float32')
>>> np.dtype("d")  # Use a double precision float character code
dtype('float64')
>>>
```

还可以将两个字符作为参数传给数据类型的构造函数。此时，第一个字符表示数据类型，第二个字符表示该类型在内存中占用的字节数（2、4、8 分别代表精度为 16、32、64 位的浮点数）：

```python
>>> np.dtype("f8")
dtype('float64')
>>>
```

完整的 NumPy 数据类型列表可以在 sctypeDict.keys() 中找到：

```python
>>> np.sctypeDict.keys()
dict_keys(['?', 0, 'byte', 'b', 省略一些
>>>
```

### dtype 类的属性

dtype 类有很多有用的属性。`char` 可以获取数据类型的字符编码，`type` 属性对应于数组元素的数据类型：

```python
>>> t = np.dtype("float64")
>>> t.char
'd'
>>> t.type
<class 'numpy.float64'>
>>>
```

str 属性可以给出数据类型的字符串表示，该字符串的首个字符表示字节序（endianness），后面如果还有字符的话，将是一个字符编码，接着一个数字表示每个数组元素存储所需的字节数。这里，字节序是指位长为 32 或 64 的字（word）存储的顺序，包括大端序（big-endian）和小端序（little-endian）。大端序是将最高位字节存储在最低的内存地址处，用 > 表示；与之相反，小端序是将最低位字节存储在最低的内存地址处，用 < 表示：

```python
>>> t.str
'<f8'
>>>
```

## 创建自定义数据类型

自定义数据类型是一种异构数据类型，可以当做用来记录电子表格或数据库中一行数据的结构。

```python
>>> t = np.dtype([("name", np.str_, 40), ("num_items", np.int32), ("price", np.float32)])
>>> t
dtype([('name', '<U40'), ('num_items', '<i4'), ('price', '<f4')])
>>> t['name']
dtype('<U40')
>>> itemz = np.array([("Meaning of life DVD", 42, 3.14), ("Butter", 13, 2.72)], dtype=t)
>>> itemz
array([('Meaning of life DVD', 42, 3.14), ('Butter', 13, 2.72)],
      dtype=[('name', '<U40'), ('num_items', '<i4'), ('price', '<f4')])
>>>
```

在用 `np.array` 函数创建数组时，如果没有在参数中指定数据类型，将默认为浮点数类型。而现在，我们想要创建自定义数据类型的数组，就必须在参数中指定数据类型，否则将触发 `TypeError` 错误。

## 一维数组的索引和切片

一维数组的切片操作与 Python 列表的切片操作很相似。

```python
>>> a = np.arange(9)
>>> a[3:7]
array([3, 4, 5, 6])
>>> a[:7:2]
array([0, 2, 4, 6])
>>> a[::-1]
array([8, 7, 6, 5, 4, 3, 2, 1, 0])
>>>
```

和 Python 中一样，我们也可以利用负数下标翻转数组。

## 多维数组的切片和索引

ndarray 支持在多维数组上的切片操作。为了方便起见，我们可以用一个省略号（...）来表示遍历剩下的维度。

```python
>>> b = np.arange(24).reshape(2, 3, 4)
>>> b.shape
(2, 3, 4)
>>> b
array([[[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11]],

       [[12, 13, 14, 15],
        [16, 17, 18, 19],
        [20, 21, 22, 23]]])
>>>
```

```python
>>> b[0, 0, 0]
0
>>> b[:, 0, 0]
array([ 0, 12])
>>> b[0]
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> b[0, :, :]
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> b[0, ...]
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>>
```

多个冒号可以用一个省略号（...）来代替。

如果在多维数组中执行翻转一维数组的命令，将在最前面的维度上翻转元素的顺序：

```python
>>> b[::-1]
array([[[12, 13, 14, 15],
        [16, 17, 18, 19],
        [20, 21, 22, 23]],

       [[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11]]])
>>>
```

## 改变数组的维度

除了 `reshape` 函数，还有一些函数可以将数组数组展平。`ravel` 函数与 `flatten` 函数的功能相同。不过，`flatten` 函数会请求分配内存来保存结果，而 `ravel` 函数只是返回数组的一个**视图**（view）：

```python
>>> b 
array([[[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11]],

       [[12, 13, 14, 15],
        [16, 17, 18, 19],
        [20, 21, 22, 23]]])
>>> b.ravel()
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19, 20, 21, 22, 23])
>>> b.flatten()
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19, 20, 21, 22, 23])
>>>
```

除了可以使用 `reshape` 函数，也可以直接用一个正整数元组来设置数组的维度，

```python
>>> b.shape = (6, 4)
>>> b
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15],
       [16, 17, 18, 19],
       [20, 21, 22, 23]])
>>>
```

`transpose` 在线性代数中，转置矩阵是很常见的操作：

```python
>>> b.transpose()
array([[ 0,  4,  8, 12, 16, 20],
       [ 1,  5,  9, 13, 17, 21],
       [ 2,  6, 10, 14, 18, 22],
       [ 3,  7, 11, 15, 19, 23]])
>>>
```

`resize` 和 `reshape` 函数的功能一样，但 `resize` 会直接修改所操作的数组：

```python
>>> b.resize((2, 12))
>>> b
array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]])
>>>
```

## 数组的组合

NumPy 数组有水平组合、垂直组合和深度组合等多种组合方式，我们将使用 `vstack`、`dstack`、`hstack`、`column_stack`、`row_stack` 以及 `concatenate` 函数来完成数组的组合。

## 组合数组

- 水平组合：将 `ndarray` 对象构成的元组作为参数，传给 `hstack` 函数。

```python
>>> a = np.arange(9).reshape(3, 3)
>>> b = 2 * a
>>> np.hstack((a, b))
array([[ 0,  1,  2,  0,  2,  4],
       [ 3,  4,  5,  6,  8, 10],
       [ 6,  7,  8, 12, 14, 16]])
>>>
```

也可以用 `concatenate` 函数来实现同样的效果：

```python
np.concatenate((a, b), axis=1)
```

- 垂直组合：垂直组合同样需要构造一个元组作为参数，只不过这次的函数变成了 `vstack`。

```python
>>> np.vstack((a, b))
array([[ 0,  1,  2],
       [ 3,  4,  5],
       [ 6,  7,  8],
       [ 0,  2,  4],
       [ 6,  8, 10],
       [12, 14, 16]])
>>> np.concatenate((a, b), axis=0)
>>>
```

- 深度组合：将相同的元组作为参数传给 `dstack` 函数，即可完成数组的深度组合。所谓深度组合，就是将一系列数组沿着纵轴（深度）方向进行层叠组合。举个例子，有若干张二维平面内的图像点阵数据，我们可以将这些图像数据沿纵轴方向层叠在一起，这就形象地解释了什么是深度组合。

```python
>>> np.dstack((a, b))
array([[[ 0,  0],
        [ 1,  2],
        [ 2,  4]],

       [[ 3,  6],
        [ 4,  8],
        [ 5, 10]],

       [[ 6, 12],
        [ 7, 14],
        [ 8, 16]]])
>>>
```

- 列组合：`column_stack` 函数对于一维数组将按列方向进行组合：

```python
oned = np.arange(2)
oned
twice_oned = 2 * oned
np.column_stack((oned, twice_oned))
```

而对于二维数组，`column_stack` 与 `hstack` 的效果是相同的：

```python
>>> np.column_stack((a, b))
array([[ 0,  1,  2,  0,  2,  4],
       [ 3,  4,  5,  6,  8, 10],
       [ 6,  7,  8, 12, 14, 16]])
>>> np.column_stack((a, b)) == np.hstack((a, b))
array([[ True,  True,  True,  True,  True,  True],
       [ True,  True,  True,  True,  True,  True],
       [ True,  True,  True,  True,  True,  True]])
>>>
```

- 行组合：当然，NumPy 中也有按行方向进行组合的函数，它就是 `row_stack`。对于两个一维数组，将直接层叠起来组合成一个二维数组。对于二维数组，`row_stack` 与 `vstack` 的效果是相同的

```python
>>> np.row_stack((oned, twice_oned))
array([[0, 1],
       [0, 2]])
>>> np.row_stack((a, b))
array([[ 0,  1,  2],
       [ 3,  4,  5],
       [ 6,  7,  8],
       [ 0,  2,  4],
       [ 6,  8, 10],
       [12, 14, 16]])
>>> np.row_stack((a, b)) == np.vstack((a, b))
array([[ True,  True,  True],
       [ True,  True,  True],
       [ True,  True,  True],
       [ True,  True,  True],
       [ True,  True,  True],
       [ True,  True,  True]])
>>>
```

|函数|说明|
|---|---|
|vstack() |该函数垂直堆叠数组|
|dstack() |该函数沿第三轴深度堆叠数组|
|hstack() |该函数水平堆叠数组|
|column_stack() |该函数将一维数组作为列堆叠以创建二维数组|
|row_stack() |该函数垂直堆叠数组|
|concatenate() |该函数连接数组的列表或元组|

## 数组的分割

NumPy 数组可以进行水平、垂直或深度分割，相关的函数有 `hsplit`、`vsplit`、`dsplit` 和 `split`。我们可以将数组分割成相同大小的子数组，也可以指定原数组中需要分割的位置。

## 分割数组

- 水平分割（理解为水平轴将被切割为 n 份）：下面的代码将把数组沿着水平方向分割为3个相同大小的子数组：

```python
>>> np.hsplit(a, 3)
[array([[0],
       [3],
       [6]]), array([[1],
       [4],
       [7]]), array([[2],
       [5],
       [8]])]
>>>
```

对同样的数组，调用 `split` 函数并在参数中指定参数 `axis=1`。

```python
np.split(a, 3, axis=1)
```

- 垂直分割：`vsplit` 函数将把数组沿着垂直方向分割，

```python
>>> np.vsplit(a, 3)
[array([[0, 1, 2]]), array([[3, 4, 5]]), array([[6, 7, 8]])]
>>> np.split(a, 3, axis=0)
[array([[0, 1, 2]]), array([[3, 4, 5]]), array([[6, 7, 8]])]
>>>
```

- 深度分割，不出所料，`dsplit` 函数将按深度方向分割数组。

```python
>>> c = np.arange(27).reshape(3, 3, 3)
>>> c
array([[[ 0,  1,  2],
        [ 3,  4,  5],
        [ 6,  7,  8]],

       [[ 9, 10, 11],
        [12, 13, 14],
        [15, 16, 17]],

       [[18, 19, 20],
        [21, 22, 23],
        [24, 25, 26]]])
>>> np.dsplit(c, 3)
[array([[[ 0],
        [ 3],
        [ 6]],

       [[ 9],
        [12],
        [15]],

       [[18],
        [21],
        [24]]]), array([[[ 1],
        [ 4],
        [ 7]],

       [[10],
        [13],
        [16]],

       [[19],
        [22],
        [25]]]), array([[[ 2],
        [ 5],
        [ 8]],

       [[11],
        [14],
        [17]],

       [[20],
        [23],
        [26]]])]
>>>
```

## 数组的属性

除了 `shape` 和 `dtype` 属性以外，ndarray 对象还有很多其他的属性

- `ndim` 属性，给出数组的维数，或数组轴的个数
- `size` 属性，给出数组元素的总个数
- `itemsize` 属性，给出数组中的元素在内存中所占的字节数
- 如果你想知道整个数组所占的存储空间，可以用 `nbytes` 属性来查看。这个属性的值其实就是 `itemsize` 和 `size` 属性值的乘积
- `T` 属性的效果和 `transpose` 函数一样
- 对于一维数组，其 `T` 属性就是原数组。在 NumPy 中，复数的虚部是用 `j` 表示的。
- `real` 属性，给出复数数组的实部。如果数组中只包含实数元素，则其 `real` 属性将输出原数组
- `imag` 属性，给出复数数组的虚部
- 如果数组中包含复数元素，则其数据类型自动变为复数型
- `flat` 属性将返回一个 `numpy.flatiter` 对象，这是获得 `flatiter` 对象的唯一方式——我们无法访问 `flatiter` 的构造函数。这个所谓的“扁平迭代器”可以让我们像遍历一维数组一样去遍历任意的多维数组。可以用`flatiter` 对象直接获取一个数组元素或者获取多个元素。`flat` 属性是一个可赋值的属性。对 `flat` 属性赋值将导致整个数组的元素都被覆盖。

![attributes of the ndarray class](./img/attributes%20of%20the%20ndarray%20class.png)

```python
>>> b
array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]])
>>> b.ndim  # ndim 属性，给出数组的维数，或数组轴的个数
2
>>> b.size  # size 属性，给出数组元素的总个数
24
>>> b.itemsize  # itemsize 属性，给出数组中的元素在内存中所占的字节数
4
>>> b.nbytes  # 整个数组所占的存储空间
96
>>> b.size * b.itemsize
96
>>> b.resize(6, 4)
>>> b = np.arange(5)
>>> b
array([0, 1, 2, 3, 4])
>>> b.T  # T 属性的效果和 transpose 函数一样
array([0, 1, 2, 3, 4])
>>> b = np.array([1.0j + 1, 2.0j + 3])  # 复数的虚部是用j表示的
>>> b.real  # real 属性，给出复数数组的实部
array([1., 3.])
>>> b.imag  # imag 属性，给出复数数组的虚部
array([1., 2.])
>>> b.dtype  # 如果数组中包含复数元素，则其数据类型自动变为复数型
dtype('complex128')
>>> b.dtype.str
'<c16'
>>> b = np.arange(4).reshape(2, 2)
>>> b
array([[0, 1],
       [2, 3]])
>>> f = b.flat  # flat 属性将返回一个 numpy.flatiter 对象
>>> f
<numpy.flatiter object at 0x000001FFD955A270>
>>> for item in f:
...     print(item)
...
0
1
2
3
>>>
>>> b.flat[2]  # 用 flatiter 对象直接获取一个数组元
2
>>> b.flat[[1, 3]]  # 或者获取多个元素
array([1, 3])
>>> b.flat = 7  # flaT 属性是一个可赋值的属性。对 flat 属性赋值将导致整个数组的元素都被覆盖
>>> b.flat[[1, 3]] = 1
>>> b
array([[7, 1],
       [7, 1]])
>>>
```

## 数组的转换

可以使用 `tolist` 函数将 NumPy 数组转换成 Python 列表。

```python
>>> b
array([[7, 1],
       [7, 1]])
>>> b.tolist()
[[7, 1], [7, 1]]
>>>
```

`astype` 函数可以在转换数组的数据类型

```python
>>> b.astype(float)
array([[7., 1.],
       [7., 1.]])
>>>
```
