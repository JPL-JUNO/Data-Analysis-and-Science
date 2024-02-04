"""
@File         : data_quality.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-04 16:19:31
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import streamlit as st
import pandas as pd

st.title("Editable DataFrames")
st.write(
    """
     Streamlit released `st.data_editor`, 
     a way to give users edit ability on top of an `st.dataframe-style` interface.
    """
)
trees_df = pd.read_csv("./trees.csv")
trees_df = trees_df.dropna(subset=["longitude", "latitude"])
trees_df_filtered = trees_df[trees_df["legal_status"] == "Private"]
st.dataframe(trees_df)
st.write(
    """
    To make this data editable, we only need to change `st.dataframe` to `st.data_editor`, 
    and then pass the result back to a new DataFrame:
    """
)

edited_df = st.data_editor(trees_df_filtered)
st.write(
    """
    整个 `DataFrame` 由数据编辑器传回，因此我们的最后一步是编辑原始的、未过滤的 `DataFrame`，
    然后覆盖 `CSV` 文件。 我们希望确保用户确定他们的更改，因此我们可以添加一个按钮，将结果写回原始 `CSV` 文件：
    """
)

trees_df.loc[edited_df.index] = edited_df
if st.button("Save data and overwrite:"):
    trees_df.to_csv("trees.csv", index=False)
    st.write("Saved!")
