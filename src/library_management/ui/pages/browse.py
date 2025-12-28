import streamlit as st
import random
from assets.styles import apply_global_styles

apply_global_styles()

# ---------------- Header ----------------
st.markdown(
    """
    <div class="page-title">
        <span class="accent">Y</span>Library 📚
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

# ---------------- Mock book data (temporary) ----------------
# This will be replaced by backend logic later
mock_books = [
    {"title": "Clean Code", "author": "Robert C. Martin"},
    {"title": "The Pragmatic Programmer", "author": "Andrew Hunt"},
    {"title": "Introduction to Algorithms", "author": "CLRS"},
    {"title": "Design Patterns", "author": "Gamma et al."},
    {"title": "Structure and Interpretation of Computer Programs", "author": "Sussman"},
    {"title": "Operating Systems: Three Easy Pieces", "author": "Remzi Arpaci-Dusseau"},
    {"title": "Computer Networks", "author": "Andrew Tanenbaum"},
]

# Randomize order every load
books = random.sample(mock_books, k=len(mock_books))

# Optional client-side filtering
if search_query:
    q = search_query.lower()
    books = [
        b for b in books
        if q in b["title"].lower() or q in b["author"].lower()
    ]

# ---------------- Book listing ----------------
st.markdown("<div style='margin-top:40px'></div>", unsafe_allow_html=True)

if books:
    cols_per_row = 3
    rows = [books[i:i + cols_per_row] for i in range(0, len(books), cols_per_row)]

    for row in rows:
        cols = st.columns(cols_per_row)
        for col, book in zip(cols, row):
            with col:
                st.markdown(
                    f"""
                    <div class="card">
                        <strong>{book['title']}</strong><br>
                        <em>{book['author']}</em>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
else:
    st.markdown(
        """
        <div class="card">
            No books found.
        </div>
        """,
        unsafe_allow_html=True
    )
