import pandas as pd

bball_16 = pd.read_csv("../data/baseball16.csv")
assert bball_16.shape == (16, 22)

data_dict = bball_16.iloc[0].to_dict()
data_dict
