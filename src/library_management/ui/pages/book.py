import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from assets.styles import apply_global_styles
from services.frontend.books_service import BooksService
from ui.components.header import Header
from ui.components.book_cover import BookCover
from ui.components.book_metadata import BookMetadata
from ui.components.borrow_button import BorrowButton

apply_global_styles()

# ---------------- Read book_id ----------------
book_id = st.query_params.get("id")

if not book_id:
    st.error("No book selected.")
    st.stop()

try:
    book_id = int(book_id)
except ValueError:
    st.error("Invalid book ID.")
    st.stop()

# ---------------- Fetch book ----------------
with st.spinner("Loading book..."):
    try:
        book = BooksService.get_book_by_id(book_id)
    except Exception as e:
        st.error(f"Failed to load book: {e}")
        st.stop()

# ---------------- Borrow state ----------------
borrow_key = f"borrowed_{book.book_id}"
if borrow_key not in st.session_state:
    st.session_state[borrow_key] = False

# ---------------- Header ----------------
Header().render()

# ---------------- Layout ----------------
st.markdown("<div style='margin-top:40px'></div>", unsafe_allow_html=True)

left, right = st.columns([1, 2], gap="large")

with left:
    BookCover(book).render()

with right:
    BookMetadata(book, st.session_state[borrow_key]).render()
    BorrowButton(borrow_key).render()
