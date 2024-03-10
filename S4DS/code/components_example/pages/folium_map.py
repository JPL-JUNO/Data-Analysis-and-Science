"""
@File         : folium_map.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-06 12:06:39
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import folium
import pandas as pd
from streamlit_folium import st_folium
import streamlit as st

st.title("Interactive maps with st-folium")
trees_df = pd.read_csv("../../data/trees.csv")
trees_df = trees_df.dropna(subset=["longitude", "latitude"])
trees_df = trees_df.iloc[:100]
lat_avg = trees_df["latitude"].mean()
lon_avg = trees_df["longitude"].mean()
m = folium.Map(location=[lat_avg, lon_avg], zoom_start=12)
# st_folium(m)
for _, row in trees_df.iterrows():
    folium.Marker([row["latitude"], row["longitude"]]).add_to(m)
events = st_folium(m)
st.write(events)
