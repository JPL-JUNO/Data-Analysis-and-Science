"""
@File         : streamlit_app.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-07 00:48:00
@Email        : cuixuanstephen@gmail.com
@Description  :
"""

import snowflake.connector
import streamlit as st

st.title("Connecting to Snowflake with Streamlit")
st.write(
    """
    ```python
    session = snowflake.connector.connect(
        **st.secrets["snowflake"], client_session_keep_alive=True
    )

    sql_query = "select 1"
    st.write("Snowflake Query Result")
    df = session.cursor().execute(sql_query).fetch_pandas_all()
    st.write(df)
    ```
    """
)
session = snowflake.connector.connect(
    **st.secrets["snowflake"], client_session_keep_alive=True
)
sql_query = "select 1"
st.write("Snowflake Query Result")
df = session.cursor().execute(sql_query).fetch_pandas_all()
st.write(df)

st.write(
    """
    Every time we run this app it will reconnect to Snowflake. This isn’t a great user experience, as
    it will make our app slower. In the past we would have cached this by wrapping it in a function
    and caching it with `st.cache_data`, but that will actually not work here as the connection is not
    data. Instead, we should cache it with `st.cache_resource`.
    """
)


@st.cache_resource
def initialize_snowflake_connection():
    session = snowflake.connector.connect(
        **st.secrets["snowflake"], client_session_keep_alive=True
    )
    return session


session = initialize_snowflake_connection()
# sql_query = "select 1;"
sql_query = """
    select
    l_returnflag,
    sum(l_quantity) as sum_qty,
    sum(l_extendedprice) as sum_base_price
    from
    snowflake_sample_data.tpch_sf1.lineitem
    where
    l_shipdate <= dateadd(day, -90, to_date('1998-12-01'))
    group by 1;
"""


@st.cache_data
def run_query(_session, sql_query):
    # 这里不能加缓存，因为 sql_query 不能 hash
    # 如果不能 hash，添加下划线
    df = _session.cursor().execute(sql_query).fetch_pandas_all()
    return df


df = run_query(session, sql_query)
# df = session.cursor().execute(sql_query).fetch_pandas_all()
st.write(df)
