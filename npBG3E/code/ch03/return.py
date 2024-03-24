import numpy as np

c = np.loadtxt("../data/AAPL.csv", delimiter=",", usecols=(6,), unpack=True)
returns = np.diff(c) / c[:-1]

print("Standard deviation =", np.std(returns))
logreturns = np.diff(np.log(c))

posretindices = np.where(returns > 0)
print("Indices with positive returns", posretindices)

annual_volatility = np.std(logreturns) / np.mean(logreturns)
annual_volatility = annual_volatility / np.sqrt(1.0 / 252.0)
print("Annual volatility", annual_volatility)
print("Monthly volatility", annual_volatility * np.sqrt(1.0 / 12.0))
