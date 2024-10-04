import pandas as pd
import numpy as np

s = pd.read_csv("../DATA/nyc-temps.txt").squeeze()
df = pd.DataFrame({"temp": s, "hour": [i for i in range(0, 24, 3)] * 91})

df[df.temp < 0]["temp"] = 0
