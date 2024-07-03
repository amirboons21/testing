import streamlit as st
import pandas as pd

st.write("""
# My first app
Hello *world!*
""")

df = pd.read_csv("msci_world_price_ts.csv")
st.line_chart(df)