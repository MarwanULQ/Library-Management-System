import streamlit as st
from ui.components.base import BaseComponent

class BrowseSearchBar(BaseComponent):
    def render(self):
        st.markdown("<div style='margin-top:10px'></div>", unsafe_allow_html=True)

        _, col2, _ = st.columns([1, 3, 1])
        with col2:
            return st.text_input(
                "",
                placeholder="Search within books..."
            )
