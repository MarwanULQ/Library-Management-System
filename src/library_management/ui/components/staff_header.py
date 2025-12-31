import streamlit as st
from ui.components.header import Header

class StaffHeader(Header):
    def render(self):
        st.markdown(
            """
            <div class="page-title">
                <span class="accent">S</span>taff Dashboard
            </div>
            <div class="custom-divider-center"></div>
            """,
            unsafe_allow_html=True
        )
