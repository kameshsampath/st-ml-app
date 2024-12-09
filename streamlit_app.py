# import pandas to read the our data file
import pandas as pd
import streamlit as st

st.title("🤖 Machine Learning App")

st.write("Welcome to world of Machine Learning with Streamlit.")

with st.expander("Data", expanded=True):
    st.write("**Raw Data**")
    # read the csv file
    df = pd.read_csv("data/penguins_cleaned.csv")
    df
