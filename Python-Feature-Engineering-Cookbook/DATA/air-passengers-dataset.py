"""
@File         : air-passengers-dataset.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2025-01-25 14:58:43
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import numpy as np
import pandas as pd

url = "https://raw.githubusercontent.com/facebook/prophet/main/examples/example_air_passengers.csv"
df = pd.read_csv(url)
df.loc[10:11, "y"] = np.nan
df.loc[25:28, "y"] = np.nan
df.loc[40:45, "y"] = np.nan
df.loc[70:94, "y"] = np.nan
df.to_csv("DATA/air_passengers.csv", index=False)
