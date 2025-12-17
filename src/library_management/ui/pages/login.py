import streamlit as st

st.title("Library Management System")
st.subheader("Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username and password:
        st.session_state.logged_in = True
        st.switch_page("pages/home.py")
    else:
        st.error("Please enter username and password")
