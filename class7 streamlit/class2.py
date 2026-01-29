import streamlit as st

st.title("chai maker App")
if st.button("Make Chai"):
    st.success("your chai is ready")
add_mazala = st.checkbox("Add Masala")
if add_mazala :
    st.write("Masala added to chai")
tea_type = st.radio("Pick your chai base" , ["water" , "milk" ])

if tea_type == "water":
    st.write(f"Added Water")
else:
    st.write("make normal coffe with milk")

sugar = st.slider("sugar level" , 0, 50 , 8)
cups = st.number_input("cups ?" , min_value=1 ,max_value=12 , step=1)
name = st.text_input("enter name")
if name :
    st.write("chai on the way")

Parcel = st.success("coffee is ready")

