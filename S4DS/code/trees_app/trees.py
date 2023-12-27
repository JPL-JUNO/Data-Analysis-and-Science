"""
@Title        : 
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2023-12-26 22:41:36
@Description  : 
"""

import altair as alt
from bokeh.plotting import figure
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
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

st.markdown('### Matplotlib and Seaborn')
trees_df['age'] = (pd.to_datetime('today') -
                   pd.to_datetime(trees_df['date'])).dt.days

st.markdown('#### Seaborn Chart')
fig_sb, ax_sb = plt.subplots()
ax_sb = sns.histplot(trees_df['age'])
plt.xlabel('Aga (Days)')
st.pyplot(fig_sb)

st.markdown('#### Matplotlib Chart')
fig_mpl, ax_mpl = plt.subplots()
ax_mpl = plt.hist(trees_df['age'])
plt.xlabel('Aga (Days)')
st.pyplot(fig_mpl)

st.markdown('### Bokeh')

scatterplot = figure(title='Bokeh Scatterplot')
scatterplot.scatter(trees_df['dbh'], trees_df['site_order'])
scatterplot.yaxis.axis_label = 'site_order'
scatterplot.xaxis.axis_label = 'dbh'
st.bokeh_chart(scatterplot)

st.markdown('### Bokeh')
df_caretaker = trees_df.groupby(['caretaker']).count()['tree_id'].reset_index()
df_caretaker.columns = ['caretaker', 'tree_count']

fig = alt.Chart(df_caretaker).mark_bar().encode(x='caretaker', y='tree_count')
st.altair_chart(fig)

st.write('Altair also allows us to summarize our data directly within the y value of mark_bar():')
fig = alt.Chart(trees_df).mark_bar().encode(x='caretaker', y='count(*):Q')
st.altair_chart(fig)

st.markdown('### PyDeck')
st.write('跳过对地图的绘制')
