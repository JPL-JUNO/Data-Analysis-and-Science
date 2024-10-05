"""
@File         : exercise_21_parking_tickets.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-10-05 20:59:02
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import pandas as pd

df = pd.read_csv(
    "../../DATA/nyc-parking-violations-2020.csv",
    usecols=[
        "Date First Observed",
        "Registration State",
        "Plate ID",
        "Issue Date",
        "Vehicle Make",
        "Street Name",
        "Vehicle Color",
    ],
)
