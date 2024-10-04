import pandas as pd

df = pd.read_csv(
    "../../DATA/nyc_taxi_2019-01.csv",
    usecols=["passenger_count", "trip_distance", "total_amount", "payment_type"],
)

df.loc[df.passenger_count > 8, "passenger_count"].count()

df.loc[df.passenger_count == 0, "passenger_count"].count()

df.loc[(df.payment_type == 2) & (df.total_amount > 1000), "passenger_count"].count()

df.loc[df.total_amount < 0, "total_amount"].count()

df.loc[
    (df.trip_distance < df.trip_distance.mean())
    & (df.total_amount > df.total_amount.mean()),
    "trip_distance",
].count()

df.query("passenger_count > 8")["passenger_count"].count()
df.query("passenger_count == 0")["passenger_count"].count()
df.query("payment_type == 2 & total_amount > 1000")["payment_type"].count()
df.query("total_amount < 0")["total_amount"].count()
df.query("trip_distance < trip_distance.mean() & total_amount > total_amount.mean()")[
    "trip_distance"
].count()

df.loc[
    (df.total_amount < 0) & ((df.payment_type == 4) | (df.payment_type == 6)),
    "total_amount",
].count()

df.payment_type.value_counts(normalize=True)[[1, 2]]
