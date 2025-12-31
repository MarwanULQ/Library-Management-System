import streamlit as st
from ui.components.base_book_card import BaseBookCard

class ClickableBookCard(BaseBookCard):
    def __init__(self, book, key_prefix="book"):
        super().__init__(book)
        self.key_prefix = key_prefix

    def render(self):
        if self.book.cover:
            st.image(self.book.cover, use_container_width=True)

        if st.button(
            self.book.book_name,
            key=f"{self.key_prefix}_{self.book.book_id}",
            use_container_width=True
        ):
            st.switch_page(
                "pages/book.py",
                query_params={"id": self.book.book_id}
            )

        if self.book.authors:
            st.caption(", ".join(a.full_name for a in self.book.authors))
        else:
            st.caption("Unknown author")
