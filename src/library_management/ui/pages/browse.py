import streamlit as st
from assets.styles import apply_global_styles
from services.frontend.books_service import BooksService

apply_global_styles()

# ---------------- Header ----------------
st.markdown(
    """
    <div class="page-title">
        <span class="accent">Y</span>Library 📚
    </div>
    <div class="page-subtitle">
        Your gateway to knowledge and culture. Accessible for everyone.
    </div>
    <div class="custom-divider-center"></div>
    """,
    unsafe_allow_html=True
)

# ---------------- Search bar ----------------
st.markdown("<div style='margin-top:10px'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    search_query = st.text_input(
        "",
        placeholder="Search within books..."
    )

# ---------------- Fetch books ----------------
with st.spinner("Loading books..."):
    try:
        books = BooksService.get_all_books()
    except Exception as e:
        st.error(f"Failed to load books: {e}")
        st.stop()

# ---------------- Client-side filtering ----------------
if search_query:
    q = search_query.lower()
    books = [
        b for b in books
        if q in b.book_name.lower()
        or any(q in a.lower() for a in b.authors)
    ]

# ---------------- Book listing ----------------
st.markdown("<div style='margin-top:40px'></div>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="custom-divider"></div>
    """,
    unsafe_allow_html=True
)

if not books:
    st.markdown(
        """
        <div class="card">
            No books found.
        </div>
        """,
        unsafe_allow_html=True
    )
    st.stop()

cols_per_row = 5
rows = [books[i:i + cols_per_row] for i in range(0, len(books), cols_per_row)]

for row in rows:
    cols = st.columns(cols_per_row)
    for col, book in zip(cols, row):
        with col:
            if book.cover:
                st.image(book.cover, use_container_width=True)

            if st.button(
                book.book_name,
                key=f"browse_title_{book.book_id}",
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
