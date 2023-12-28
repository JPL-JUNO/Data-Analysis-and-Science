"""
@Title        : 
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2023-12-28 20:40:22
@Description  : 
"""

import openai
import streamlit as st

st.title('OpenAI Version')
analyze_button = st.button('Analyze Text')
openai.api_key = st.secrets['OPENAI_API_KEY']
text = st.text_input("Enter text to analyze")

if analyze_button:
    messages = [
        {"role": "system", "content": """You are a helpful sentiment analysis assistant. You always respond with the sentiment of the text you are
         given and the confidence of your sentiment analysis with a number between
         0 and 1"""},
        {"role": "user",
         "content": f"Sentiment analysis of the following text: {text}"}
    ]
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
    )
    sentiment = response.choices[0].messages['content'].strip()

    st.write(sentiment)

system_message_default = """You are a helpful sentiment analysis
assistant. You always respond with the sentiment of the text you are given
and the confidence of your sentiment analysis with a number between 0 and
1"""

system_message = st.text_area(
    "Enter a System Message to instruct OpenAI", system_message_default
)

analyze_button = st.button('Analyze Text')
if analyze_button:
    messages = [
        {
            'role': 'system',
            'content': f'{system_message}',
        },
        {
            'role': 'user',
            "content": f"Sentiment analysis of the following text: {text}",
        }
    ]
