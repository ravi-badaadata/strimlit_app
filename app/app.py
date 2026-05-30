import streamlit as st
from utils.db import get_session

st.title("My Snowflake Streamlit app badaadata_new_badaa_few1🚀")

session = get_session()

df = session.sql("SELECT CURRENT_USER(), CURRENT_DATABASE()").to_pandas()

st.dataframe(df)
