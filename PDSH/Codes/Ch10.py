import numpy as np

rng = np.random.default_rng(seed=1701)

x = rng.integers(100, size=10)
print(x)

[x[3], x[7], x[2]]

idx = [3, 7, 4]
x[idx]

idx = np.array([[3, 7],
                [4, 5]])

x[idx]

X = np.arange(12).reshape((3, 4))
row = np.array([0, 1, 2])
col = np.array([2, 1, 3])
X[row, col]
