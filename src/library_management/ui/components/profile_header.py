import streamlit as st
from ui.components.header import Header

class ProfileHeader(Header):
    def render(self):
        st.markdown(
            """
            <div class="page-title">
                <span class="accent">P</span>rofile
            </div>
            <div class="page-subtitle">
                Manage your account and activity
            </div>
            <div class="custom-divider-center"></div>
            """,
            unsafe_allow_html=True
        )
