import streamlit as st
from ui.components.base import BaseComponent

class BookMetadata(BaseComponent):
    def __init__(self, book, borrowed: bool):
        self.book = book
        self.borrowed = borrowed

    def render(self):
        borrowed_text = "Yes" if self.borrowed else "No"

        st.markdown(
            f"""
            <h1 style="margin-bottom:10px;">{self.book.book_name}</h1>
            <h3 style="margin-top:0; font-style:italic;">
                {", ".join(self.book.authors) if self.book.authors else "Unknown author"}
            </h3>

            <div class="custom-divider"></div>

            <p><strong>Publication year:</strong> {self.book.publication_year}</p>
            <p><strong>ISBN:</strong> {self.book.isbn}</p>
            <p><strong>Language:</strong> {self.book.language}</p>
            <p><strong>Borrowed:</strong> {borrowed_text}</p>

            <div class="custom-divider"></div>
            """,
            unsafe_allow_html=True
        )
