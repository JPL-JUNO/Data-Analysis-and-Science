"""
@File         : ch09_grouping_for_aggregation_filtration_and_transformation.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-03-27 19:53:20
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import pandas as pd
import numpy as np

flights = pd.read_csv("../data/flights.csv")

flights.groupby("AIRLINE").agg({"ARR_DELAY": "mean"})

flights.groupby("AIRLINE")["ARR_DELAY"].agg("mean")

flights.groupby("AIRLINE")["ARR_DELAY"].agg(np.mean)

flights.groupby("AIRLINE")["ARR_DELAY"].mean()

grouped = flights.groupby("AIRLINE")
type(grouped)


flights.groupby("AIRLINE")["ARR_DELAY"].agg(np.sqrt)

flights.groupby(["AIRLINE", "WEEKDAY"])["CANCELLED"].agg("sum")

flights.groupby(["AIRLINE", "WEEKDAY"])[["CANCELLED", "DIVERTED"]].agg(["sum", "mean"])

flights.groupby(["ORG_AIR", "DEST_AIR"]).agg(
    {"CANCELLED": ["sum", "mean", "size"], "AIR_TIME": ["mean", "var"]}
)

flights.groupby(["ORG_AIR", "DEST_AIR"]).agg(
    sum_cancelled=pd.NamedAgg(column="CANCELLED", aggfunc="sum"),
    mean_cancelled=pd.NamedAgg(column="CANCELLED", aggfunc="mean"),
    size_cancelled=pd.NamedAgg(column="CANCELLED", aggfunc="size"),
    mean_air_time=pd.NamedAgg(column="AIR_TIME", aggfunc="mean"),
    var_air_time=pd.NamedAgg(column="AIR_TIME", aggfunc="var"),
)

res = flights.groupby(["ORG_AIR", "DEST_AIR"]).agg(
    {"CANCELLED": ["sum", "mean", "size"], "AIR_TIME": ["mean", "var"]}
)
res.columns = ["_".join(x) for x in res.columns.to_flat_index()]
res.head()


def flatten_cols(df):
    df.columns = ["_".join(x) for x in df.columns.to_flat_index()]
    return df


res = (
    flights.groupby(["ORG_AIR", "DEST_AIR"])
    .agg({"CANCELLED": ["sum", "mean", "size"], "AIR_TIME": ["mean", "var"]})
    .pipe(flatten_cols)
)

res = (
    flights.assign(ORG_AIR=flights.ORG_AIR.astype("category"))
    .groupby(["ORG_AIR", "DEST_AIR"])
    .agg({"CANCELLED": ["sum", "mean", "size"], "AIR_TIME": ["mean", "var"]})
)
res.shape

res = (
    flights.assign(ORG_AIR=flights.ORG_AIR.astype("category"))
    .groupby(["ORG_AIR", "DEST_AIR"], observed=True)
    .agg({"CANCELLED": ["sum", "mean", "size"], "AIR_TIME": ["mean", "var"]})
)
res.shape

airline_info = (
    flights.groupby(["AIRLINE", "WEEKDAY"])
    .agg({"DIST": ["sum", "mean"], "ARR_DELAY": ["min", "max"]})
    .astype(int)
)
airline_info

airline_info.columns.get_level_values(0)
airline_info.columns.get_level_values(1)
airline_info.columns.to_flat_index()

airline_info.columns = ["_".join(x) for x in airline_info.columns.to_flat_index()]

airline_info.reset_index()

flights.groupby(["AIRLINE"], as_index=False)["DIST"].agg("mean").round(0)
flights.groupby(["AIRLINE"], as_index=False, sort=False)["DIST"].agg("mean").round(0)

college = pd.read_csv("../data/college.csv")
college.groupby("STABBR")["UGDS"].agg(["mean", "std"]).round(0)


def max_deviation(s):
    std_score = s - s.mean() / s.std()
    return std_score.abs().max()


college.groupby("STABBR")["UGDS"].agg(max_deviation).round(1)
college.groupby("STABBR")[["UGDS", "SATVRMID", "SATMTMID"]].agg(max_deviation).round(1)
college.groupby("STABBR")[["UGDS", "SATVRMID", "SATMTMID"]].agg(
    [max_deviation, "mean", "std"]
).round(1)

max_deviation.__name__
max_deviation.__name__ = "Max Deviation"
college.groupby("STABBR")[["UGDS", "SATVRMID", "SATMTMID"]].agg(
    [max_deviation, "mean", "std"]
).round(1)
