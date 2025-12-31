import streamlit as st
from ui.components.header import Header

class RoomHeader(Header):
    def render(self):
        st.markdown(
            """
            <div class="page-title">
                <span class="accent">R</span>oom Reservation
            </div>
            <div class="custom-divider-center"></div>
            """,
            unsafe_allow_html=True
        )
