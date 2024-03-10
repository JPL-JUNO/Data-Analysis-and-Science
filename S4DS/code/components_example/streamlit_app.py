"""
@File         : streamlit_app.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-04 20:17:19
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import streamlit as st

st.set_page_config(layout="wide")
st.title("Ch07 Exploring Streamlit Components: Streamlit Components Examples")
st.write(
    """
    `streamlit-aggrid` essentially creates a
    beautiful, interactive, and editable version of st.dataframe, and is built on top of a JavaScript
    product called [AgGrid](https://www.ag-grid.com/).
    """
)
st.markdown("## Adding editable DataFrames with streamlit-aggrid")
st.write(
    """
    Within `aggrid.py`, we can pull in the penguins data, and use the central function in `streamlit-aggrid` 
    called `AgGrid` to display the data in our Streamlit app.
    """
)
st.write(
    """
    你可能会注意到的一件事是，它默认显示整个 DataFrame。我发现这对于 Streamlit 应用程序来说有点不和谐，但幸运的是，streamlit-aggrid 中有一个 `height` 参数可以强制 DataFrame 适应特定的高度。
    """
)
st.write(
    """
    我们已经讨论过但尚未展示的最后一个功能是在 AgGrid 中编辑 DataFrame 的能力。 同样，这就像向 AgGrid 函数添加参数一样简单。 该函数返回编辑后的 DataFrame，我们可以在应用程序的其余部分使用它。 这意味着该组件是双向的，就像我们已经使用过的所有 Streamlit 输入小部件一样。
    """
)

st.markdown("## Creating drill-down graphs with streamlit-plotly-events")
st.write(
    """
    `streamlit-plotly-events` turns the unidirectional `st.plotly_chart` function into a bidirectional one, 
    where we can receive events like clicks or hovers back into our Streamlit app.
    """
)
st.write(
    """
    The `plotly_events` function takes an argument called `click_event`, which, if we set it to `True`, will return all the click events back to Streamlit as a variable. 
    """
)

st.write(
    """
    The streamlit-plotly-events library has two other events (`select_event` and `hover_event`), which can be useful as well and are returned in the same fashion.
    """
)

st.markdown("## Using Streamlit Components – streamlit-lottie")
st.write(
    """
    `streamlit-lottie` also allows us to change the animation speed, width, and height through the `speed`, `width`, and `height` parameters, respectively. If the animation goes too slowly for your taste, increase the speed to a number such as 1.5 or 2, which will increase the speed by 50% or 100%. The `height` and `width` parameters, however, are the pixel height/width of the animation and default to the native size of the animation.
    """
)
st.markdown("## Using Streamlit Components – streamlit-pandas-profiling")
st.write(
    """
    `pandas-profiling` is a very powerful Python library that automates some of the EDA, which is often the first step in any data analysis, modeling, or even data engineering task. 
    """
)
st.markdown("## Interactive maps with st-folium")
st.write(
    """
    `st-folim` is very similar to `streamlit-plotly-events`, but for geospatial maps.
    
    The interesting part comes when we realize that the `st_folium` function returns the click 
    events made on the map by default!
    """
)
st.markdown("## Helpful mini-functions with streamlit-extras")
st.write(
    """
    For example, we had a problem where users of our apps would accidentally just select one date
    in a date range, and then the entire app would not run correctly. In response to this, we built
    a mandatory date range picker that will not run the app until two dates are selected! It can be
    used like this:
    
    ```python
    from streamlit_extras.mandatory_date_range import date_range_picker

    result = date_range_picker("Select a date range")
    st.write("Result:", result)
    ```
    """
)

from streamlit_extras.mandatory_date_range import date_range_picker

result = date_range_picker("Select a date range")
st.write("Result:", result)
st.write(
    """
    Or for another example, we wanted to have an input that looked like the toggles in our favorite
    document management software, Notion. So we built a small one! It can be used like so:
    
    ```python
    from streamlit_extras.stoggle import stoggle

    stoggle("Click me!", "Surprise! Here's some additional content")
    ```
    """
)
from streamlit_extras.stoggle import stoggle

stoggle("Click me!", """😜Surprise! Here's some additional content""")
st.markdown("## Finding more Components")
st.write(
    """
    The best place to find new and interesting Components is on either
    the [Streamlit website](https://streamlit.io/gallery?type=components&category=featured) or the [discussion forums](https://discuss.streamlit.io/c/streamlit-components/18).
    """
)
