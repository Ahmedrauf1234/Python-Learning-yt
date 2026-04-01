import streamlit as st
import requests

st.title("Live Currency Converter")

URL = "https://api.exchangerate-api.com/v4/latest/PKR"
response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    currensies = list(data["rates"].keys())

    amount = st.number_input("Enter amount in PKR:")
    target_currency = st.selectbox("Convert to" , currensies)
    if st.button("Convert"):
        if amount > 0:
            rate = data["rates"][target_currency]
            converted = rate * amount
            st.success(f"{amount} PKR = {converted:.2f} {target_currency}")
        else:
            st.warning("Enter Amount greater then 0")
else:
    st.error("Failed to fetch conversion rate")

    


