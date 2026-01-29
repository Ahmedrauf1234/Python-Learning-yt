import streamlit as st

st.title("Hello Streamlit 👋")
st.write("Streamlit successfully install ho gaya!")

select = st.selectbox("whats your name?" , ["Ahmed" , "talha" , "hammad"])
st.success(f"Hey {select}")
