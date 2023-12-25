"""
@Title        : 展示中心极限定理
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2023-12-25 21:04:10
@Description  : 
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('Illustrating the Central Limit Theorem with Streamlit')
st.subheader('An app by Stephen CUI')
st.write(('This app simulates a thousand coin clips using the chance of heads input below, '
          'and then samples with replacement from that population and plots the histogram of the'
          ' means of the samples in order to illustrate the central limit theorem!'))

perc_heads = st.number_input(label='Chance of Coins Landing on Heads',
                             min_value=.0, max_value=1.0, value=.5)

graph_title = st.text_input(label='Graph Title')

binom_dist = np.random.binomial(1, perc_heads, 1_000)
list_of_means = []
for i in range(0, 1_000):
    list_of_means.append(np.random.choice(
        binom_dist, 100, replace=True).mean())

fig, ax = plt.subplots()
plt.hist(list_of_means, range=[0, 1])
plt.title(graph_title)
st.pyplot(fig)

#  简写，不推荐，已经被弃用
# plt.hist(list_of_means)
# st.pyplot()
# plt.hist([1, 1, 1, 1])
# st.pyplot()
