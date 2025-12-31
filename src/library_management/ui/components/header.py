import streamlit as st
from ui.components.base import BaseComponent

class Header(BaseComponent):
    def render(self):
        st.markdown(
            """
            <div class="page-title">
                <span class="accent">Y</span>Library 📚
            </div>
            <div class="page-subtitle">
                Your gateway to knowledge and culture. Accessible for everyone.
            </div>
            <div class="custom-divider-center"></div>
            """,
            unsafe_allow_html=True
        )
