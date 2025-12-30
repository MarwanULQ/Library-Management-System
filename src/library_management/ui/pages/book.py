import streamlit as st
from assets.styles import apply_global_styles
from services.frontend.books_service import BooksService

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

# ---------------- Borrow state (mock for now) ----------------
borrow_key = f"borrowed_{book.book_id}"
if borrow_key not in st.session_state:
    st.session_state[borrow_key] = False

borrowed_text = "Yes" if st.session_state[borrow_key] else "No"

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

# ---------------- Layout ----------------
st.markdown("<div style='margin-top:40px'></div>", unsafe_allow_html=True)

left, right = st.columns([1, 2], gap="large")

# ---- Cover (left) ----
with left:
    if isinstance(book.cover, str) and (
        book.cover.startswith("http://") or book.cover.startswith("https://")
    ):
        st.image(book.cover, use_container_width=True)
    else:
        st.markdown(
            """
            <div class="card" style="text-align:center;">
                No cover available
            </div>
            """,
            unsafe_allow_html=True
        )

# ---- Metadata (right) ----
with right:
    st.markdown(
        f"""
        <h1 style="margin-bottom:10px;">{book.book_name}</h1>
        <h3 style="margin-top:0; font-style:italic;">
            {", ".join(book.authors) if book.authors else "Unknown author"}
        </h3>

        <div class="custom-divider"></div>

        <p><strong>Publication year:</strong> {book.publication_year}</p>
        <p><strong>ISBN:</strong> {book.isbn}</p>
        <p><strong>Language:</strong> {book.language}</p>
        <p><strong>Borrowed:</strong> {borrowed_text}</p>

        <div class="custom-divider"></div>
        """,
        unsafe_allow_html=True
    )

    # ---- Borrow button (still mock state) ----
    if not st.session_state[borrow_key]:
        if st.button("📥 Borrow Book"):
            st.session_state[borrow_key] = True
            st.rerun()
    else:
        st.button("✅ Already Borrowed", disabled=True)
