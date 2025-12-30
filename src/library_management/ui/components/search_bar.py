import streamlit as st
from ui.components.base_search_bar import BaseSearchBar

class SearchBar(BaseSearchBar):
    def __init__(self):
        super().__init__(
            placeholder="Search for title, author, ISBN, DOI, publisher, md5..."
        )

    def on_change(self, value: str):
        if value:
            st.switch_page(
                "pages/search.py",
                query_params={"query": value}
            )
