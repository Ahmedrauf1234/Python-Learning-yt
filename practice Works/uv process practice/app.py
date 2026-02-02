import streamlit as st

st.title("Hello Streamlit 👋")
st.write("Mera pehla Streamlit app")

name = st.text_input("Apna naam likho")

if name:
    st.success(f"Welcome {name} 😊")
