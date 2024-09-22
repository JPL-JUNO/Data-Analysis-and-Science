"""
@File         : 06_data_assembly.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-09-22 20:43:07
@Email        : cuixuanstephen@gmail.com
@Description  : Data Assembly
"""

import pandas as pd

df1 = pd.read_csv("DATA/concat_1.csv")
df2 = pd.read_csv("DATA/concat_2.csv")
df3 = pd.read_csv("DATA/concat_3.csv")

from pathlib import Path

billboard_data_files = Path("./DATA/billboard-by_week/").glob("billboard-*.csv")
list_billboard_df = []

for csv_filename in billboard_data_files:
    df = pd.read_csv(csv_filename)

    list_billboard_df.append(df)

billboard_loop_concat = pd.concat(list_billboard_df)

# 需要重新生成生成器
billboard_data_files = Path("./DATA/billboard-by_week/").glob("billboard-*.csv")
billboard_dfs = [pd.read_csv(data) for data in billboard_data_files]
