import streamlit as st
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
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
st.markdown("<div style='margin-top:40px'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    search_query = st.text_input(
        "",
        placeholder="Search for title, author, ISBN, DOI, publisher, md5..."
    )

    if search_query:
        st.switch_page("pages/search.py",
                       query_params={"query": search_query})

st.markdown("<div style='margin-top:30px'></div>", unsafe_allow_html=True)

st.markdown(
    """
    <style>
        .home-cta .stButton > button {
            background-color: #BCCCDC !important;
            color: #000000 !important;
            border: 1px solid #4b5563 !important;
            border-radius: 4px;
            font-size: 18px;
            padding: 18px 30px;
            width: 25em;
            margin-left: 30px;
            font-weight: 800;
            letter-spacing: 0.9px;
        }

        .home-cta .stButton > button:hover {
            background-color: #AEBFD4 !important;
        }

        .stButton > button {
            font-family: inherit;
            background-color: #BCCCDC;
            color: #000000;
            border: 1px solid #4b5563;
            border-radius: 4px;
            font-size: 18px;
            padding: 18px 30px;
            width: 25em;
            margin-left: 30px;
            font-weight: 800;
            letter-spacing: 0.9px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="home-cta">', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    btn_col1, btn_col2 = st.columns(2)

    with btn_col1:
        browse_clicked = st.button("📚 Browse Books")
        if browse_clicked:
            st.switch_page("pages/browse.py")

    with btn_col2:
        room_clicked = st.button("🏫 Room Reservation")
        if room_clicked:
            st.switch_page("pages/room.py")

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- Featured Books ----------------
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
        books = []

if not books:
    st.info("📭 No books available yet.")
else:
    cols_per_row = 5
    rows = [books[i:i + cols_per_row] for i in range(0, len(books), cols_per_row)]

    for row in rows:
        cols = st.columns(cols_per_row)
        for col, book in zip(cols, row):
            with col:
                if book.cover:
                    st.image(book.cover, use_container_width=True)
                else:
                    st.image(
                        Path(__file__).resolve().parents[1]
                        / "assets" / "covers" / "1.jpg",
                        use_container_width=True
                    )
