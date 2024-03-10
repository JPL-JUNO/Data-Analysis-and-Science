"""
@File         : pretty_trees.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-03 12:47:29
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import streamlit as st

st.set_page_config(layout="wide")
st.title("Ch06 Beautifying Streamlit Apps: ST Trees")
st.write(
    """
    This app analyses trees in San Francisco using a dataset kindly provided by SD DPW.
    """
)
st.write(
    """
    Streamlit allows us to format our app into dynamic columns using the `st.columns()` feature.
    
    We can divide our Streamlit app into multiple columns of different lengths and then treat each
    column as its own unique space (called a **container**) in our app to include text, graphs, images,
    or anything else we would like.
    """
)
st.write(
    """
    The easiest way to think about the with notation in Streamlit columns is that
    they are self-contained blocks of code that tell Streamlit exactly where to place items in our apps.
    ```python
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Column 1")
    with col2:
        st.write("Column 2")
    with col3:
        st.write("Column 3")
    ```
    """
)
col1, col2, col3 = st.columns(3)
with col1:
    st.write("Column 1")
with col2:
    st.write("Column 2")
with col3:
    st.write("Column 3")

st.write(
    """
    As we can see, `st.columns()` defines three columns of equal length, and we can use the 
    `with` notation to print some text in each. We can also call the `st.write()` function (or any other Streamlit
    function that writes content to our Streamlit app).
    
    ```python
    col1, col2, col3 = st.columns(3)
    col1.write("Column 1")
    col2.write("Column 2")
    col3.write("Column 3")
    ```
    """
)

st.write(
    """
    在 Streamlit 中，列宽是相对于其他定义的列的大小而言的。 因此，如果我们将每列的宽度放大到 10 而不是 1，我们的应用程序将根本不会改变。 此外，我们还可以将单个数字传递给 `st.beta_columns()`，它将返回相同宽度的列数。
    
    ```python
    col1, col2, col3 = st.columns((1, 1, 1))
    col1, col2, col3 = st.columns((10, 10, 10))
    col1, col2, col3 = st.columns(3)
    ```
    """
)
import pandas as pd

trees_df = pd.read_csv("./trees.csv")
df_dbh_grouped = pd.DataFrame(trees_df.groupby("dbh").count()["tree_id"])
df_dbh_grouped.columns = ["tree_count"]

# col1, col2, col3 = st.columns(3)
# col1, col2, col3 = st.columns(3, gap="large")
with col1:
    st.line_chart(df_dbh_grouped)

with col2:
    st.bar_chart(df_dbh_grouped)
with col3:
    st.area_chart(df_dbh_grouped)

st.markdown("### Exploring page configuration")
st.write(
    """
    The default for Streamlit apps is to have a centered page layout, which is why there is copious white space on the edges of our apps.
    
    ```python
    st.set_page_config(layout='wide')
    ```
    """
)

st.write(
    """
    关于 Streamlit 列，我们还需要了解两点信息。 第一个是我们还可以编辑我们创建的列容器之间的间隙，第二个是我们还可以确保图形保留在其列内并且不会渗透到其他列中。 对于间隙部分，默认是在列之间留一个小间隙，但我们可以将其更改为中等或大间隙。
    
    ```python
    col1, col2, col3 = st.columns(3, gap="large")
    ```
    
    ```python
    with col1:
        st.line_chart(df_dbh_grouped, use_container_width=False)
    ```
    """
)

st.markdown("## Using Streamlit tabs")
st.write(
    """
    还有第二种组织 Streamlit 应用程序布局的方法，它与 Streamlit 列非常相似，称为选项卡。 当您的内容太宽而无法分成列（即使在宽模式下）时，选项卡很有用；当您想通过一次只显示一项内容来集中注意力时，选项卡也很有用。
    
    `st.tabs` works very similarly to `st.columns`, but instead of telling Streamlit the number of tabs we want, we instead pass along the names of the tabs and then use now-familiar `with` statements to place content into the tab. 
    """
)

tab1, tab2, tab3 = st.tabs(["Line Chart", "Bar Chart", "Area Chart"])
with tab1:
    st.line_chart(df_dbh_grouped)
with tab2:
    st.bar_chart(df_dbh_grouped)
with tab3:
    st.area_chart(df_dbh_grouped)

st.markdown("## Using the Streamlit sidebar")

# owners = st.sidebar.multiselect("Tree Owner Filter", trees_df["caretaker"].unique())

# if owners:
#     trees_df = trees_df[trees_df["caretaker"].isin(owners)]
# df_dbh_grouped = pd.DataFrame(trees_df.groupby(["dbh"]).count()["tree_id"])
# df_dbh_grouped.columns = ["tree_count"]
# st.line_chart(df_dbh_grouped)

# trees_df = trees_df.dropna(subset=["longitude", "latitude"])
# trees_df = trees_df.sample(n=1000, replace=True)
# st.map(trees_df)

import plotly.express as px

today = pd.to_datetime("today")
trees_df["date"] = pd.to_datetime(trees_df["date"])
trees_df["age"] = (today - trees_df["date"]).dt.days
unique_caretakers = trees_df["caretaker"].unique()
owners = st.sidebar.multiselect("Tree Owner Filter", unique_caretakers)
if owners:
    trees_df = trees_df[trees_df["caretaker"].isin(owners)]
df_dbh_grouped = pd.DataFrame(trees_df.groupby(["dbh"]).count()["tree_id"])
df_dbh_grouped.columns = ["tree_count"]

col1, col2 = st.columns(2)
with col1:
    fig = px.histogram(trees_df, x=trees_df["dbh"], title="Tree Width")
    st.plotly_chart(fig)
with col2:
    fig = px.histogram(trees_df, x=trees_df["age"], title="Tree Age")
    st.plotly_chart(fig)
st.write("Trees by Location")
trees_df = trees_df.dropna(subset=["longitude", "latitude"])
trees_df = trees_df.sample(n=1000, replace=True)
st.map(trees_df)

st.markdown("## Picking colors with a color picker")
st.write(
    """
    Streamlit’s approach to this problem is `st.color_picker()`,
    which lets the user pick a color as a part of their user input, and returns that color in a hex string
    (which is a unique string that defines very specific color shades used by most graphing libraries
    as input).
    """
)
graph_color = st.sidebar.color_picker("Graph Colors")
if owners:
    trees_df = trees_df[trees_df["caretaker"].isin(owners)]
col1, col2 = st.columns(2)
with col1:
    fig = px.histogram(
        trees_df,
        x=trees_df["dbh"],
        title="Tree Width",
        color_discrete_sequence=[graph_color],
    )
    fig.update_xaxes(title_text="Width")
    st.plotly_chart(fig, use_container_width=True)
with col2:
    fig = px.histogram(
        trees_df,
        x=trees_df["dbh"],
        title="Tree Age",
        color_discrete_sequence=[graph_color],
    )
    st.plotly_chart(fig, use_container_width=True)
st.write("Trees by Location")
trees_df = trees_df.dropna(subset=["longitude", "latitude"])
trees_df = trees_df.sample(n=1000, replace=True)
st.map(trees_df)
st.markdown("## Multi-page apps")
st.write(
    """
    Streamlit 创建多页面应用程序的方式是在与我们的 Streamlit 应用程序相同的目录中查找名为 `pages` 的文件夹，然后将 `pages` 文件夹内的每个Python 文件作为其自己的 Streamlit 应用程序运行。
    """
)
