import pandas as pd

df_2019_jul = pd.read_csv(
    "../../DATA/nyc_taxi_2019-07.csv",
    usecols=["passenger_count", "total_amount", "payment_type"],
)
df_2019_jul["year"] = 2019

df_2020_jul = pd.read_csv(
    "../../DATA/nyc_taxi_2020-07.csv",
    usecols=["passenger_count", "total_amount", "payment_type"],
)
df_2020_jul["year"] = 2020

df = pd.concat([df_2019_jul, df_2020_jul])

(
    df.loc[df["year"] == 2019, "total_amount"].count()
    - df.loc[df["year"] == 2020, "total_amount"].count()
)

df.loc[
    (df["year"] == 2019) & (df.passenger_count > 1), "passenger_count"
].count() / df.loc[df["year"] == 2019, "passenger_count"].count()
