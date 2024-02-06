"""
@File         : penguin_animated.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-04 21:57:38
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import streamlit as st
import pandas as pd
import plotly.express as px

from streamlit_plotly_events import plotly_events
import requests
from streamlit_lottie import st_lottie


def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


st.set_page_config(layout="wide")

lottie_penguin = load_lottie_url(
    "https://assets9.lottiefiles.com/private_files/lf30_lntyk83o.json"
)
st_lottie(lottie_penguin, height=150, speed=2)


st.title("Streamlit Plotly Events + Lottie Example: Penguins")
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
