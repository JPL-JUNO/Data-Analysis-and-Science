L = [2, 1, 4, 1, 5, 9, 2, 6]
sorted(L)

print(L)

L.sort()
print(L)


sorted('python')


import numpy as np

x = np.array([2, 1, 4, 3, 5])
np.sort(x)

x.sort()


x = np.array([2, 1, 4, 3, 5])
i = np.argsort(x)
print(i)

x[i]

rng = np.random.default_rng(seed=42)
X = rng.integers(0, 10, size=(4, 6))
print(X)

np.sort(X, axis=0)

np.sort(X, axis=1)


x = np.array([7, 2, 3, 1, 6, 4, 5])
np.partition(x, 3)

np.partition(X, 2, axis=1)
