import streamlit as st
col1 , col2 = st.columns(2)
with col1:
    st.header("Masala Chai")
    vote1 = st.button("Vote masala chai")
    st.image("https://i.pinimg.com/736x/13/00/ce/1300ce79ee5fc7781be417b118e44c0d.jpg", width=200)
with col2:
    st.header("Adrak Chai")
    vote2 = st.button("Vote adrak chai")
    st.image("https://i.pinimg.com/736x/69/27/2d/69272dd561bb47ae63992587b5ce8c99.jpg", width=200)

if vote1 :
    st.success("thanks for voting")
   
elif vote2 :
    st.success("thanks adrak chai")

name = st.sidebar.text_input("Enter your name:")
tea = st.sidebar.selectbox("choose your chai" , ["Masala" , "elaichi" , "Adrak"])
st.write(f"welcome {name} and your chai is {tea}")

with st.expander("Show chai making instructions"):
    st.write("""
    1. boil water
    2. water base    
""")
st.markdown('### welcome chai App')
