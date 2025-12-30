import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from assets.styles import apply_global_styles
from ui.components.header import Header
from ui.components.browse_search_bar import BrowseSearchBar
from ui.components.book_card_clickable import ClickableBookCard
from ui.components.book_grid import BookGrid
from services.frontend.books_service import BooksService

apply_global_styles()

Header().render()

# Local search
search_bar = BrowseSearchBar()
search_bar.render()
query = search_bar.value

# Fetch all books
with st.spinner("Loading books..."):
    try:
        books = BooksService.get_all_books()
    except Exception as e:
        st.error(f"Failed to load books: {e}")
        st.stop()

# Client-side filtering
if query:
    q = query.lower()
    books = [
        b for b in books
        if q in b.book_name.lower()
        or any(q in a.lower() for a in b.authors)
    ]

st.markdown("<div style='margin-top:40px'></div>", unsafe_allow_html=True)
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

BookGrid(
    books,
    card_cls=ClickableBookCard,
    key_prefix="browse"
).render()
