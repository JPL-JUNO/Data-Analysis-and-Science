"""
@File         : penguin_profiled.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-04 22:25:41
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import pandas as pd
import plotly.express as px
import requests
import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_lottie import st_lottie
from streamlit_pandas_profiling import st_profile_report
from streamlit_plotly_events import plotly_events

st.set_page_config(layout="wide")
df = pd.read_csv("../../data/penguins.csv")
fig = px.scatter(df, x="bill_length_mm", y="bill_depth_mm", color="species")
selected_point = plotly_events(fig, click_event=True)
st.subheader("Pandas Profiling of Penguin Dataset")
penguin_profile = ProfileReport(df, explorative=True)
st_profile_report(penguin_profile)
