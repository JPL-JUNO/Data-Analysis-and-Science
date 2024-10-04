"""
@File         : exercise_12_finding_outliers.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-10-03 22:54:25
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import pandas as pd
import numpy as np

trip_distance = pd.read_csv("../DATA/taxi-distance.csv", header=None).squeeze()
passenger_count = pd.read_csv("../DATA/taxi-passenger-count.csv", header=None).squeeze()


df = pd.DataFrame({"trip_distance": trip_distance, "passenger_count": passenger_count})
