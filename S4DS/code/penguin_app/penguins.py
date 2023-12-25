"""
@Title        : 
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2023-12-25 22:11:16
@Description  : 
"""

import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns
st.title("Palmer's Penguins")

penguin_file = st.file_uploader(
    'Select your Local Penguins CSV (default provided)')
if penguin_file is not None:
    penguins_df = pd.read_csv(penguin_file)
else:
    penguins_df = pd.read_csv('../../data/penguins.csv')
# st.write(penguins_df.head())
st.markdown(
    'Use this Streamlit app to make your own scatter plot about penguins!')

# selected_species = st.selectbox('What species would you like to visualize?',
#                                 ['Adelie', 'Gentoo', 'Chinstrap'])

selected_x_var = st.selectbox('What do you want the x variable to be?',
                              ['bill_length_mm', 'bill_depth_mm',
                               'flipper_length_mm', 'body_mass_g'])
selected_y_var = st.selectbox('What about the y?',
                              ['bill_length_mm', 'bill_depth_mm',
                               'flipper_length_mm', 'body_mass_g'])

# penguins_df = penguins_df[penguins_df['species'] == selected_species]

alt_chart = (
    alt.Chart(penguins_df,
              # title=f'Scatterplot of {selected_species} Penguins'
              )
    .mark_circle().encode(x=selected_x_var,
                          y=selected_y_var,
                          color='species')
    .interactive()  # 设置为交互性的
)
# 使用整个容器的宽度
st.altair_chart(alt_chart, use_container_width=True)
