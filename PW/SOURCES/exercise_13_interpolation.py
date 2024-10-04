"""
@File         : exercise_13_interpolation.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-10-04 14:25:36
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import pandas as pd
import numpy as np

s = pd.read_csv("../DATA/nyc-temps.txt").squeeze()
df = pd.DataFrame({"temp": s, "hour": [i for i in range(0, 24, 3)] * 91})
df.loc[df["hour"].isin([3, 6]), "temp"] = np.NAN
df = df.interpolate(method="linear")
df["temp"].describe()
