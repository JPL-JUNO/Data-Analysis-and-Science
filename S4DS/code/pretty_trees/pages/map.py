"""
@File         : map.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-04 13:35:23
@Email        : cuixuanstephen@gmail.com
@Description  : 多页面应用的案例
"""

import pandas as pd
import streamlit as st

st.title("Ch06 Multi-page apps: SF Trees Map")
st.write(
    """
    运行的路径仍然是相对于上一级问价，而不是当前的文件
    
    ```python
    trees_df = pd.read_csv("../trees.csv")
    ```
    """
)
trees_df = pd.read_csv("trees.csv")
trees_df = trees_df.dropna(subset=["longitude", "latitude"])
trees_df = trees_df.sample(n=1_000, replace=True)
st.map(trees_df)
