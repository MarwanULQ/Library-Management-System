import streamlit as st
from ui.components.base import BaseComponent

class AuthChoiceButtons(BaseComponent):
    def render(self):
        if "auth_mode" not in st.session_state:
            st.session_state.auth_mode = None  # "login" | "signup"

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Login", use_container_width=True):
                st.session_state.auth_mode = "login"

        with col2:
            if st.button("Sign Up", use_container_width=True):
                st.session_state.auth_mode = "signup"