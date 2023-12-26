"""
@Title        : 使用数据缓存
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2023-12-26 21:59:56
@Description  : 
"""

import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns
import time
st.title("Palmer's Penguins")
st.markdown(
    'Use this Streamlit app to make your own scatter plot about penguins!')

penguin_file = st.file_uploader(
    'Select your Local Penguins CSV (default provided)')


@st.cache_data
def load_file(penguin_file):
    time.sleep(3)  # 估计减速以测试代码是否运行的更快
    if penguin_file is not None:
        df = pd.read_csv(penguin_file)
    else:
        df = pd.read_csv('../../data/penguins.csv')

    return df


penguins_df = load_file(penguin_file)


# selected_species = st.selectbox('What species would you like to visualize?',
#                                 ['Adelie', 'Gentoo', 'Chinstrap'])

selected_x_var = st.selectbox('What do you want the x variable to be?',
                              ['bill_length_mm', 'bill_depth_mm',
                               'flipper_length_mm', 'body_mass_g'])
selected_y_var = st.selectbox('What about the y?',
                              ['bill_length_mm', 'bill_depth_mm',
                               'flipper_length_mm', 'body_mass_g'])

selected_gender = st.selectbox('What gender do you want to filter for?',
                               ['all penguins', 'male penguins', 'female penguins'])

if selected_gender == 'male penguins':
    penguins_df = penguins_df[penguins_df['sex'] == 'male']
elif selected_gender == 'female penguins':
    penguins_df = penguins_df[penguins_df['sex'] == 'female']
else:
    pass

# penguins_df = penguins_df[penguins_df['species'] == selected_species]

sns.set_style('darkgrid')
markers = {'Adelie': 'X', "Gentoo": 's', 'Chinstrap': 'o'}

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
