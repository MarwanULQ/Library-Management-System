import streamlit as st
from ui.components.base import BaseComponent

class BookGrid(BaseComponent):
    def __init__(self, books, cols_per_row=5, clickable=False, key_prefix="book"):
        self.books = books
        self.cols_per_row = cols_per_row
        self.clickable = clickable
        self.key_prefix = key_prefix

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
                    if book.cover:
                        st.image(book.cover, use_container_width=True)

                    if self.clickable:
                        if st.button(
                            book.book_name,
                            key=f"{self.key_prefix}_{book.book_id}",
                            use_container_width=True
                        ):
                            st.switch_page(
                                "pages/book.py",
                                query_params={"id": book.book_id}
                            )

                        if book.authors:
                            st.caption(", ".join(book.authors))
                        else:
                            st.caption("Unknown author")
