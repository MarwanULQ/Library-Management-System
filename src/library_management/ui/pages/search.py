import streamlit as st
from assets.styles import apply_global_styles

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

if query:
    st.markdown(
        f"""
        <h2>Results for: <em>{query}</em></h2>
        <div class="custom-divider"></div>
        """,
        unsafe_allow_html=True
    )

    # Placeholder for search results
    st.markdown(
        """
        <div class="card">
            Search results will appear here.
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <div class="card">
            No search query provided.
        </div>
        """,
        unsafe_allow_html=True
    )
