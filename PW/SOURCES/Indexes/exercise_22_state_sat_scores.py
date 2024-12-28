"""
@File         : exercise_22_state_sat_scores.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-10-27 17:18:36
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import pandas as pd

filename = "../../DATA/sat-scores.csv"

df = pd.read_csv(
    filename,
    usecols=["Year", "State.Code", "Total.Math", "Total.Test-takers", "Total.Verbal"],
)

df = df.set_index(["Year", "State.Code"])

df.loc[(2010, ["NY", "NJ", "MA", "IL"]), "Total.Math"].mean()

df.loc[([2012, 2013, 2014, 2015], ["AZ", "CA", "TX"]), "Total.Math"].mean()
