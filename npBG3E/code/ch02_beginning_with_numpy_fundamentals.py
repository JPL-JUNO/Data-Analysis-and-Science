"""
@File         : ch02_beginning_with_numpy_fundamentals.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-03-23 15:21:16
@Email        : cuixuanstephen@gmail.com
@Description  : NumPy 基础
"""

import numpy as np

a = np.arange(5)
a.dtype
a
a.shape

m = np.array([np.arange(2), np.arange(2)])
m
m.shape

a = np.array([[1, 2], [3, 4]])
a
a[0, 0]
a[0, 1]
a[1, 0]
a[1, 1]

np.finfo(np.float32)

np.float64(42)
np.int8(42.0)
np.bool_(42)
np.bool_(0)
np.bool_(42.0)
np.float64(True)
np.float64(False)

np.arange(7, dtype=np.uint8)

np.int16(42.0 + 1.0j)

np.complex64(1.0)

a.dtype.itemsize

np.arange(7, dtype="f")
np.arange(7, dtype="D")

np.dtype(float)  # Use the general Python float
np.dtype("f")  # Specify a single precision float with a character code
np.dtype("d")  # Use a double precision float character code
np.dtype("f8")

np.sctypeDict.keys()

t = np.dtype("float64")
t.char
t.type

t.str

t = np.dtype([("name", np.str_, 40), ("num_items", np.int32), ("price", np.float32)])
t
itemz = np.array([("Meaning of life DVD", 42, 3.14), ("Butter", 13, 2.72)], dtype=t)
itemz

a = np.arange(9)
a[3:7]
a[:7:2]
a[::-1]

b = np.arange(24).reshape(2, 3, 4)
b.shape
b
b[0, 0, 0]
b[:, 0, 0]
b[0]
b[0, :, :]
b[0, ...]

b[::-1]

b
b.ravel()
b.flatten()

b.shape = (6, 4)
b
b.transpose()

b.resize((2, 12))

a = np.arange(9).reshape(3, 3)
b = 2 * a
np.hstack((a, b))

np.concatenate((a, b), axis=1)

np.vstack((a, b))
np.concatenate((a, b), axis=0)

np.dstack((a, b))

oned = np.arange(2)
oned
twice_oned = 2 * oned
np.column_stack((oned, twice_oned))

np.column_stack((a, b))
np.column_stack((a, b)) == np.hstack((a, b))

np.row_stack((oned, twice_oned))
np.row_stack((a, b))
np.row_stack((a, b)) == np.vstack((a, b))

np.hsplit(a, 3)

np.split(a, 3, axis=1)

np.vsplit(a, 3)
np.split(a, 3, axis=0)

c = np.arange(27).reshape(3, 3, 3)
c
np.dsplit(c, 3)

b = np.arange(24).reshape(2, 12)
b
b.ndim  # ndim 属性，给出数组的维数，或数组轴的个数
b.size  # size 属性，给出数组元素的总个数
b.itemsize  # itemsize 属性，给出数组中的元素在内存中所占的字节数
b.nbytes  # 整个数组所占的存储空间
b.size * b.itemsize
b.resize(6, 4)
b = np.arange(5)
b
b.T  # T 属性的效果和 transpose 函数一样
b = np.array([1.0j + 1, 2.0j + 3])  # 复数的虚部是用j表示的
b.real  # real 属性，给出复数数组的实部
b.imag  # imag 属性，给出复数数组的虚部
b.dtype  # 如果数组中包含复数元素，则其数据类型自动变为复数型
b.dtype.str
b = np.arange(4).reshape(2, 2)
b
f = b.flat  # flat 属性将返回一个 numpy.flatiter 对象
f
for item in f:
    print(item)


b.flat[2]  # 用 flatiter 对象直接获取一个数组元
b.flat[[1, 3]]  # 或者获取多个元素
b.flat = 7  # flaT 属性是一个可赋值的属性。对 flat 属性赋值将导致整个数组的元素都被覆盖
b.flat[[1, 3]] = 1

b
b.tolist()
b.astype(float)
