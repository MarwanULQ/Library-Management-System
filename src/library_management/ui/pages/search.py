import streamlit as st
from assets.styles import apply_global_styles
from services.frontend.books_service import BooksService

apply_global_styles()

# ---------------- Read query from Home ----------------
query = st.query_params.get("query", "")

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
st.markdown("<div style='margin-top:5px'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    search_query = st.text_input(
        "",
        value=query,
        placeholder="Search for title, author, ISBN, DOI, publisher, md5..."
    )

    if search_query and search_query != query:
        st.switch_page(
            "pages/search.py",
            query_params={"query": search_query}
        )

# ---------------- Results ----------------
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
                key=f"search_title_{book.book_id}",
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
