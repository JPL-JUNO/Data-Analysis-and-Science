import numpy as np

h, l, c = np.loadtxt("../data/AAPL.csv", delimiter=",", usecols=(4, 5, 6), unpack=True)
N = 5
h = h[-N:]
l = l[-N:]

print("len(h)", len(h), "len(l)", len(l))
print("Close", c)
previous_close = c[-N - 1 : -1]

print("len(previous_close)", len(previous_close))
print("Previous close", previous_close)

true_range = np.maximum(h - l, h - previous_close, previous_close - l)
print("True range", true_range)

atr = np.zeros(N)
atr[0] = np.mean(true_range)
for i in range(1, N):
    atr[i] = (N - 1) * atr[i - 1] + true_range[i]
    atr[i] /= N
