import streamlit as st

st.set_page_config(page_title="Library System")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    st.switch_page("pages/home.py")
else:
    st.switch_page("pages/login.py")
