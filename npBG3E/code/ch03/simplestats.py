import numpy as np

c = np.loadtxt("../data/AAPL.csv", delimiter=",", usecols=(6,), unpack=True)
print("median =", np.median(c))

sorted = np.msort(c)
print("sorted =", sorted)

N = len(c)
print("middle =", sorted[int(N / 2)])
print("average middle =", (sorted[int(N / 2)] + sorted[int(N / 2 - 1)]) / 2)

print("variance =", np.var(c))
print("variance from definition =", np.mean((c - c.mean()) ** 2))
