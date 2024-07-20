import pandas as pd
import numpy as np

bball_16 = pd.read_csv("../data/baseball16.csv")
assert bball_16.shape == (16, 22)

data_dict = bball_16.iloc[0].to_dict()
data_dict

new_data_dict = {k: "" if isinstance(v, str) else np.nan for k, v in data_dict.items()}
new_data_dict
