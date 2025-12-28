import streamlit as st
from assets.styles import apply_global_styles


class LoginPage:
    def __init__(self):
        self._init_session_state()

    # ---------- Public API ----------
    def render(self):
        apply_global_styles()
        self._render_header()
        self._render_choice_buttons()
        self._render_forms()

    # ---------- Session State ----------
    def _init_session_state(self):
        defaults = {
            "choicef": False,
            "new": False,
            "logged_in": False,
        }
        for key, value in defaults.items():
            if key not in st.session_state:
                st.session_state[key] = value

    # ---------- Header ----------
    def _render_header(self):
        st.markdown(
            """
            <div class="page-title">
                <span class="accent">Y</span>Library 📚
            </div>
            <div class="page-subtitle" style="color:#94a3b8;">
                Secure access to knowledge and services
            </div>
            <div class="custom-divider-center"></div>
            """,
            unsafe_allow_html=True
        )

    # ---------- Choice Buttons ----------
    def _render_choice_buttons(self):
        col1, col2 = st.columns(2)

        with col1:
            if st.button("Login", key="choose_login", use_container_width=True):
                st.session_state.choicef = True
                st.session_state.new = False

        with col2:
            if st.button("Sign Up", key="choose_signup", use_container_width=True):
                st.session_state.choicef = True
                st.session_state.new = True

    # ---------- Forms ----------
    def _render_forms(self):
        if not st.session_state.choicef:
            return

        st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

        username = st.text_input("Username")

        email = None
        if st.session_state.new:
            email = st.text_input("Email")

        password = st.text_input("Password", type="password")

        action = "Sign Up" if st.session_state.new else "Login"

        if st.button(
            action,
            key="submit_signup" if st.session_state.new else "submit_login",
            use_container_width=True
        ):
            self._handle_submit(username, email, password)

    # ---------- Auth Logic ----------
    def _handle_submit(self, username, email, password):
        if not username or not password:
            st.error("Please fill all fields correctly")
            return

        if st.session_state.new:
            if not email or "@ejust.edu.eg" not in email:
                st.error(
                    "Don't have access to the Uni Library. "
                    "You should have an E-JUST Email."
                )
                return

        st.session_state.logged_in = True
        st.switch_page("pages/home.py")


page = LoginPage()
page.render()