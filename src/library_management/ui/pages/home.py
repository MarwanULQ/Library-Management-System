import streamlit as st

st.title("Home")

st.write("Welcome to the Library Management System")

st.markdown("---")

st.write("This is the home page placeholder")

if st.button("Logout"):
    st.session_state.logged_in = False
    st.switch_page("pages/login.py")
