import streamlit as st
from ui.components.base import BaseComponent

class BookGrid(BaseComponent):
    def __init__(self, books, card_cls, cols_per_row=5, **card_kwargs):
        self.books = books
        self.card_cls = card_cls
        self.cols_per_row = cols_per_row
        self.card_kwargs = card_kwargs

    def render(self):
        if not self.books:
            st.info("📭 No books found.")
            return

        rows = [
            self.books[i:i + self.cols_per_row]
            for i in range(0, len(self.books), self.cols_per_row)
        ]

        for row in rows:
            cols = st.columns(self.cols_per_row)
            for col, book in zip(cols, row):
                with col:
                    self.card_cls(book, **self.card_kwargs).render()
