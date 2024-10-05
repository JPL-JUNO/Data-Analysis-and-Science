import pandas as pd
import numpy as np

df = pd.read_csv(
    "../../DATA/nyc_taxi_2020-01.csv",
    usecols=["passenger_count", "total_amount", "payment_type"],
    dtype={
        "passenger_count": np.float32,
        "total_amount": np.float32,
        "payment_type": np.float32,
    },
)


df = df.dropna().copy()
df["passenger_count"] = df["passenger_count"].astype(np.int8)
df["payment_type"] = df["payment_type"].astype(np.int8)

df = pd.read_csv(
    "../../DATA/nyc_taxi_2020-01.csv",
    usecols=["VendorID", "trip_distance", "tip_amount", "total_amount"],
    dtype={
        "VendorID": np.float32,
        "trip_distance": np.float32,
        "tip_amount": np.float32,
        "total_amount": np.float32,
    },
)
df = df.dropna().copy()
df.loc["VenderID"] = df["VenderId"].astype(np.int8)
