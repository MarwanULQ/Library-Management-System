import streamlit as st
from ui.components.base import BaseComponent

class SearchBar(BaseComponent):
    def render(self):
        st.markdown("<div style='margin-top:40px'></div>", unsafe_allow_html=True)

        _, col2, _ = st.columns([1, 3, 1])
        with col2:
            query = st.text_input(
                "",
                placeholder="Search for title, author, ISBN, DOI, publisher, md5..."
            )

            if query:
                st.switch_page(
                    "pages/search.py",
                    query_params={"query": query}
                )
