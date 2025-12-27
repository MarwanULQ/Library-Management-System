import streamlit as st
from pathlib import Path
from assets.styles import apply_global_styles

apply_global_styles()

# ---------------- Mock book data ----------------
book = {
    "title": "Berserk, Vol. 1",
    "author": "Kentaro Miura",
    "year": 1990,
    "publisher": "Hakusensha",
    "isbn": "9784592134010",
    "language": "Japanese",
    "pages": 224,
    "description": (
        "Berserk is a dark fantasy manga that follows Guts, a lone mercenary, "
        "as he struggles against fate, demons, and his own inner darkness. "
        "Renowned for its detailed artwork, brutal themes, and philosophical depth."
    ),
    "cover": "5.jpg",
}

# ---------------- Borrow state (mock) ----------------
if "borrowed" not in st.session_state:
    st.session_state.borrowed = False

# ---------------- Resolve cover path ----------------
COVERS_DIR = Path(__file__).resolve().parents[1] / "assets" / "covers"
cover_path = COVERS_DIR / book["cover"]

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
    if cover_path.exists():
        st.image(cover_path, use_container_width=True)
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
    borrowed_text = "Yes" if st.session_state.borrowed else "No"

    st.markdown(
        f"""
        <h1 style="margin-bottom:10px;">{book['title']}</h1>
        <h3 style="margin-top:0; font-style:italic;">{book['author']}</h3>

        <div class="custom-divider"></div>

        <p><strong>Year:</strong> {book['year']}</p>
        <p><strong>Publisher:</strong> {book['publisher']}</p>
        <p><strong>ISBN:</strong> {book['isbn']}</p>
        <p><strong>Language:</strong> {book['language']}</p>
        <p><strong>Pages:</strong> {book['pages']}</p>
        <p><strong>Borrowed:</strong> {borrowed_text}</p>

        <div class="custom-divider"></div>

        <p>{book['description']}</p>
        """,
        unsafe_allow_html=True
    )

    # ---- Borrow button ----
    if not st.session_state.borrowed:
        if st.button("📥 Borrow Book"):
            st.session_state.borrowed = True
            st.rerun()
    else:
        st.button("✅ Already Borrowed", disabled=True)
