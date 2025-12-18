import streamlit as st
from pathlib import Path

if "menu_open" not in st.session_state:
    st.session_state.menu_open = False

st.set_page_config(
    page_title="YLibrary",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <style>
        .stApp {
            background-color: #F8FAFC;
            font-family: "Georgia", "Times New Roman", serif;
        }

        .title {
            font-family: inherit;
            text-align: center;
            font-size: 96px;
            font-weight: 800;
            margin-top: 50px;
            margin-bottom: 0;
            font-spacing: 1.2px;
            text-shadow: 0px 4px 12px rgba(0, 0, 0, 0.40);
        }

        .subtitle {
            font-family: inherit;
            text-align: center;
            font-size: 20px;
            font-style: italic;
            color: #555;
            margin-top: 10px;
            margin-bottom: 20px;
            margin-left: -10px;
        }

        .stTextInput > div > div > input {
            background-color: #9AA6B2;
            color: #000000;
            border: 1px solid #000000;
            border-radius: 0px;
            padding: 14px 16px;
            font-size: 15px;
        }

        .stTextInput > div > div > input::placeholder {
            font-family: inherit;
            color: #eeeeef;
            padding: 18px 18px;
            font-size: 16px;
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
        .custom-divider {
            width: 100%;
            height: 2px;
            background-color: #1f2937;
            margin-bottom: 10px;
            margin-top: -10px;
            opacity: 0.5;
        }

        .custom2-divider {
            width: 40%;
            height: 2px;
            background-color: #1f2937;
            margin-left: 500px;
            margin-bottom: 10px;
            margin-top: -10px;
            opacity: 0.5;
        }

        .top-icons {
            display: flex;
            justify-content: flex-end;
            gap: 18px;
            margin-top: 25px;
        }

        .top-icons img {
            width: 34px;
            height: 34px;
            cursor: pointer;
        }

        .modal-overlay {
            position: fixed;
            inset: 0;
            background-color: rgba(0,0,0,0.55);
            z-index: 9998;
        }

        .modal-box {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: #F8FAFC;
            padding: 30px;
            width: 420px;
            border-radius: 6px;
            z-index: 9999;
            box-shadow: 0 20px 50px rgba(0,0,0,0.4);
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="title">
        <span style="
            color:#2ecc71;
            text-shadow: 0px 4px 16px rgba(0, 0, 0, 0.30);
        ">Y</span>Library 📚
    </div>
    <div class="subtitle">
         Your gateway to knowledge and culture. Accessible for everyone. 
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown('<div class="custom2-divider"></div>', unsafe_allow_html=True)

st.markdown("<div style='margin-top:40px'></div>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    search_query = st.text_input(
        "",
        placeholder="Search for title, author, ISBN, DOI, publisher, md5..."
    )

st.markdown("<div style='margin-top:30px'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    btn_col1, btn_col2 = st.columns(2)

    with btn_col1:
        browse_clicked = st.button("📚 Browse Books")

    with btn_col2:
        room_clicked = st.button("🏫 Room Reservation")


COVERS_DIR = Path(__file__).resolve().parents[1] / "assets" / "covers"
st.markdown(
    "<h2 style='text-align:left; color:#000000 ; font-family: inherit;'>Featured Books: </h2>",
    unsafe_allow_html=True
)

st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
covers = sorted(COVERS_DIR.glob("*.jpg"), reverse=True)

cols_per_row = 5
rows = [covers[i:i + cols_per_row] for i in range(0, len(covers), cols_per_row)]

for row in rows:
    cols = st.columns(cols_per_row)
    for col, cover in zip(cols, row):
        with col:
            st.image(cover, use_container_width=True)
