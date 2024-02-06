"""
@File         : plotly_events.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-04 21:27:56
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import streamlit as st
import pandas as pd
import plotly.express as px

from streamlit_plotly_events import plotly_events

st.set_page_config(layout="wide")
st.title("Streamlit Plotly Events Example: Penguins")
df = pd.read_csv("../../data/penguins.csv")
fig = px.scatter(df, x="bill_length_mm", y="bill_depth_mm", color="species")
# st.plotly_chart(fig)
# 颜色不起作用
selected_point = plotly_events(fig, click_event=True)
if len(selected_point) == 0:
    st.stop()
selected_x_value = selected_point[0]["x"]
selected_y_value = selected_point[0]["y"]
df_selected = df[
    (df["bill_length_mm"] == selected_x_value)
    & (df["bill_depth_mm"] == selected_y_value)
]
st.write("Selected point:")
st.write(df_selected)

from pandas.errors import DataError
