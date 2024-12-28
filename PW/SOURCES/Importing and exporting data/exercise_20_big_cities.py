import pandas as pd

df = pd.read_json("../../DATA/cities.json")
df["population"].describe()[["mean", "50%"]]


pd.cut(
    df.growth_from_2000_to_2013,
    bins=[df.growth_from_2000_to_2013.min(), 0, df.growth_from_2000_to_2013.max()],
    include_lowest=True,
    labels=["-", "+"],
).value_counts()


df.loc[
    (df.latitude > df.latitude.mean() + 2 * df.latitude.std())
    | (df.latitude < df.latitude.mean() - 2 * df.latitude.std())
]
