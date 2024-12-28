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
import numpy as np

g = np.random.default_rng(0)
df = pd.DataFrame(g.integers(0, 100, [36, 3]), columns=list("ABC"))
df["year"] = [2018] * 12 + [2019] * 12 + [2020] * 12
df["month"] = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split() * 3

df = df.set_index("year")

df.loc[
    [
        (2018, "Jun"),
        (2018, "Jul"),
        (2018, "Aug"),
        (2019, "Jun"),
        (2019, "Jul"),
        (2019, "Aug"),
        (2020, "Jun"),
        (2020, "Jul"),
        (2020, "Aug"),
    ]
]

df.loc[([2018, 2019, 2020], ["Jun", "Jul", "Aug"]), ["A", "B", "C"]]

df.loc[([2018, 2019, 2020], ["Jun", "Jul", "Aug"]), "A":"C"]

df.loc[(slice(None), ["Jun", "Jul", "Aug"]), "A":"C"]
