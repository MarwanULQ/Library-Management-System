import streamlit as st
from ui.components.base import BaseComponent

class BookCover(BaseComponent):
    def __init__(self, book):
        self.book = book

    def render(self):
        if isinstance(self.book.cover, str):
            st.image(self.book.cover, use_container_width=True)
        else:
            st.markdown(
                """
                <div class="card" style="text-align:center;">
                    No cover available
                </div>
                """,
                unsafe_allow_html=True
            )
