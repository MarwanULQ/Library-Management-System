import streamlit as st
from ui.components.base import BaseComponent

class ProfileButton(BaseComponent):
    def render(self):
        # Top spacing to align with header
        st.markdown("<div style='margin-top:10px'></div>", unsafe_allow_html=True)

        # 3-column layout: push button to far right
        _, _, col = st.columns([8, 1, 1])

        with col:
            if st.button("👤 Profile", use_container_width=True):
                st.switch_page("pages/profile.py")
