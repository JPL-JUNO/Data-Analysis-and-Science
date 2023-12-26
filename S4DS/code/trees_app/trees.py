"""
@Title        : 
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2023-12-26 22:41:36
@Description  : 
"""

import plotly.express as px
import numpy as np
import streamlit as st
import pandas as pd

st.title('SF Trees')
st.subheader('Author: Stephen CUI')
st.write("""
         This app analyzes trees in San Francisco using a
         dataset kindly provided by SF DPW
         """)

trees_df = pd.read_csv('./trees.csv')
df_dbh_grouped = trees_df.groupby(by=['dbh'])['tree_id'].count().to_frame()

df_dbh_grouped.columns = ['tree_count']

st.line_chart(df_dbh_grouped)
# st.bar_chart(df_dbh_grouped)
# st.area_chart(df_dbh_grouped)
df_dbh_grouped['new_col'] = np.random.randn(len(df_dbh_grouped)) * 500

st.line_chart(df_dbh_grouped)
# st.write(df_dbh_grouped)

# df_dbh_grouped = trees_df.groupby(
#     by=['dbh'])['tree_id'].count().to_frame().reset_index()

# df_dbh_grouped.columns = ['dbh', 'tree_count']
# 显式指明 x-axis 和 y-axis
# st.line_chart(df_dbh_grouped, x='dbh', y='tree_count')
st.markdown('### 绘制地图')
trees_df = trees_df.dropna(subset=['longitude', 'latitude'])
trees_df = trees_df.sample(n=1_000)
st.map(trees_df)
st.markdown('## Streamlit’s built-in visualization options')
st.markdown('### Plotly')

fig = px.histogram(trees_df['dbh'])
st.plotly_chart(fig)
