import streamlit as st
from ui.components.header import Header

class LoginHeader(Header):
    def render(self):
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
