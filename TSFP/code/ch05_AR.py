import pandas as pd
import numpy as np

df = pd.read_csv("../data/foot_traffic.csv")
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(df["foot_traffic"])
ax.set_xlabel("Time")
ax.set_ylabel("Average weekly foot traffic")
plt.xticks(np.arange(0, 1000, 104), np.arange(2000, 2020, 2))
fig.autofmt_xdate()
plt.tight_layout()

from statsmodels.tsa.stattools import adfuller

ADF_result = adfuller(df["foot_traffic"])

print(f"ADF Statistics: {ADF_result[0]}")
print(f"p-value: {ADF_result[1]}")

foot_traffic_diff = np.diff(df["foot_traffic"], n=1)
ADF_result = adfuller(foot_traffic_diff)

print(f"ADF Statistics: {ADF_result[0]}")
print(f"p-value: {ADF_result[1]}")

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

fig = plot_acf(foot_traffic_diff, lags=20)
plt.tight_layout()


# PACF
from statsmodels.tsa.arima_process import ArmaProcess

np.random.seed(42)
ma2 = np.array([1, 0, 0])
ar2 = np.array([1, -0.33, -0.5])
AR2_process = ArmaProcess(ar2, ma2).generate_sample(nsample=1_000)

fig = plot_pacf(AR2_process, lags=20)
plt.tight_layout()

fig = plot_pacf(foot_traffic_diff, lags=20)
plt.tight_layout()
