"""
@File         : exercise_19_bitcoin_values.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-10-05 15:23:59
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import pandas as pd

df = pd.read_csv(
    "https://api.blockchain.info/charts/market-price?format=csv",
    header=None,
    names=["date", "value"],
)

import requests
from io import StringIO

r = requests.get("https://data_for_you.com/data.csv")
s = StringIO(r.content.decode())
df = pd.read_csv(s)

df.loc[df["value"] == df["value"].max()]
df.loc[df["value"] == df["value"].min()]
