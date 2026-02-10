import streamlit as st
import pandas as pd

st.title("chai sales dashboard")

file = st.file_uploader("upload your csv file" , type=["csv"])

if file :
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)

if file :
    st.subheader("Summary Stats")
    st.write(df.describe())

if file:
    cities = df["city"].unique()
    select_cities = st.selectbox("filter cities" , cities)
    filter_data = df[df["city"] == select_cities]
    st.dataframe(filter_data) #this is pandas part

