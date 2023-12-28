"""
@Title        : 
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2023-12-28 20:27:13
@Description  : 
"""

import streamlit as st
from transformers import pipeline

st.title('Hugging Face Demo')
text = st.text_input('Enter text to analyze')


@st.cache_resource
def get_model():
    return pipeline('sentiment-analysis')


model = get_model()

if text:
    result = model(text)
    st.write('Sentiment:', result[0]['label'])
    st.write('Confidence:', result[0]['score'])
