import streamlit as st
from ui.components.base import BaseComponent
from ui.components.auth_controller import AuthController

class AuthForm(BaseComponent):
    def render(self):
        if st.session_state.auth_mode is None:
            return

        st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        action = "Sign Up" if st.session_state.auth_mode == "signup" else "Login"

        if st.button(
            action,
            key=f"auth_submit_{st.session_state.auth_mode}",
            use_container_width=True
        ):
            AuthController.submit(email, password)
