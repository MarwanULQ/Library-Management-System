import streamlit as st
from ui.components.base import BaseComponent
from ui.components.book_grid import BookGrid
from services.frontend.books_service import BooksService

class FeaturedBooks(BaseComponent):
    def render(self):
        st.markdown(
            """
            <h2 style="text-align:left; font-family: inherit;">
                Featured Books:
            </h2>
            <div class="custom-divider"></div>
            """,
            unsafe_allow_html=True
        )

        with st.spinner("Loading books..."):
            try:
                books = BooksService.get_all_books()
            except Exception as e:
                st.error(f"Failed to load books: {e}")
                return

        BookGrid(books).render()
