"""
@Title        : 
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2023-12-26 22:14:43
@Description  : 
"""

import streamlit as st

st.title('My To-Do List Center')

if 'my_todo_list' not in st.session_state:
    st.session_state.my_todo_list = [
        'Buy groceries', 'Learn Streamlit', 'Learn Python']


# st.write('My current To-Do list is:', my_todo_list)

new_todo = st.text_input('What do you need to do?')
if st.button('Add the new To-Do item'):
    st.write('Adding a new item to the list')
    # 这里的问题在于每次运行都会覆盖之前添加的值
    st.session_state.my_todo_list.append(new_todo)
    # 这样的话会记住我们每次的添加，直到我们离开 App 或者刷新页面

st.write('My new To-Do list is:', st.session_state.my_todo_list)
