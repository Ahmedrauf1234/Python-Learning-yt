import streamlit as st

st.title("Hello Streamlit 👋")
st.write("Streamlit successfully install ho gaya!")
st.text("Ahmed")
select = st.selectbox("your fav language", ["javascript" , "python" , "C language"])
st.write(f"you choose {select} best choice")
st.success("language is good")

