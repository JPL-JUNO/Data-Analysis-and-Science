import pandas as pd
import numpy as np

# 创建示例数据
data = {
    "group": ["A", "A", "B", "B", "B"],
    "value": [10, 20, 30, 40, 50],
    "weight": [1, 2, 3, 4, 5],
}

df = pd.DataFrame(data)

# df.groupby("group").agg(avg=pd.NamedAgg("value", aggfunc=np.average))

# df.groupby("group").agg(
#     avg=("value", lambda g: np.average(g, weights=df.loc[g.index, "weight"]))
# )
df.groupby("group").agg(
    {"value": lambda g: np.average(g, weights=df.loc[g.index, "weight"])}
)
