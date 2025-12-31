import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from assets.styles import apply_global_styles
from services.frontend.books_service import BooksService
from services.frontend.loan_service import LoanService
from ui.components.header import Header
from ui.components.book_cover import BookCover
from ui.components.book_metadata import BookMetadata
from ui.components.borrow_button import BorrowButton

if st.session_state.logged_in:
    apply_global_styles()

    # ---------------- Auth guard ----------------
    if "student_id" not in st.session_state:
        st.error("You must be logged in to borrow books.")
        st.stop()

    student_id = st.session_state["student_id"]

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

    # ---------------- Fetch loans ----------------
    with st.spinner("Checking loan status..."):
        try:
            loans = LoanService.get_loans()
        except Exception as e:
            st.error(f"Failed to fetch loans: {e}")
            st.stop()

    # ---------------- Determine borrowed state ----------------
    borrowed = any(
        loan.book_id == book.book_id and loan.student_id == student_id
        for loan in loans
    )

    # ---------------- Header ----------------
    Header().render()

    # ---------------- Layout ----------------
    st.markdown("<div style='margin-top:40px'></div>", unsafe_allow_html=True)

    left, right = st.columns([1, 2], gap="large")

    with left:
        BookCover(book).render()

    with right:
        BookMetadata(book, borrowed).render()
        BorrowButton(
            can_borrow=not borrowed,
            student_id=student_id,
            book_id=book.book_id
        ).render()
else:
    st.error("You should Log in to view book")
