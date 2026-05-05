import streamlit as st
from utils.db import get_session

st.title("My Snowflake Streamlit App 🚀")

session = get_session()

query = "SELECT CURRENT_DATE() AS TODAY"
df = session.sql(query).to_pandas()

st.dataframe(df)
