import streamlit as st
from ui.components.base_search_bar import BaseSearchBar

class SearchPageSearchBar(BaseSearchBar):
    def __init__(self, initial_query: str):
        super().__init__(
            placeholder="Search for title, author, ISBN, DOI, publisher, md5...",
            initial_value=initial_query
        )

    def on_change(self, value: str):
        if value and value != self.initial_value:
            st.switch_page(
                "pages/search.py",
                query_params={"query": value}
            )
