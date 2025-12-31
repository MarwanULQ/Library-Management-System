import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

import streamlit as st
from assets.styles import apply_global_styles
from ui.components.header import Header
from ui.components.book_card_clickable import ClickableBookCard
from ui.components.search_page_search_bar import SearchPageSearchBar
from ui.components.book_grid import BookGrid
from services.frontend.books_service import BooksService


if st.session_state.logged_in:
    apply_global_styles()

    # Read query from URL
    query = st.query_params.get("query", "")

    Header().render()
    SearchPageSearchBar(query).render()

    st.markdown("<div style='margin-top:40px'></div>", unsafe_allow_html=True)

    if not query:
        st.markdown(
            """
            <div class="card">
                No search query provided.
            </div>
            """,
            unsafe_allow_html=True
        )
        st.stop()

    st.markdown(
        f"""
        <h2>Results for: <em>{query}</em></h2>
        <div class="custom-divider"></div>
        """,
        unsafe_allow_html=True
    )

    with st.spinner("Searching books..."):
        try:
            books = BooksService.search_books(query)
        except Exception as e:
            st.error(f"Search failed: {e}")
            st.stop()

    BookGrid(
        books,
        card_cls=ClickableBookCard,
        key_prefix="search"
    ).render()
else:
    st.error("You must sign in to search books")
