import streamlit as st

def apply_global_styles():
    st.set_page_config(
        page_title="YLibrary",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    st.markdown(
        """
        <style>
            /* ---------- Global ---------- */
            .stApp {
                background-color: #F8FAFC;
                color: #000000;
                font-family: "Georgia", "Times New Roman", serif;
            }

            h1, h2, h3, p, span, label {
                font-family: inherit;
                color: #000000;
            }

            /* ---------- Titles ---------- */
            .page-title {
                text-align: center;
                font-size: 96px;
                font-weight: 800;
                margin-top: 20px;
                margin-bottom: 0;
                text-shadow: 0px 4px 12px rgba(0,0,0,0.4);
            }

            .page-subtitle {
                text-align: center;
                font-size: 20px;
                font-style: italic;
                color: #555;
                margin-top: 10px;
                margin-bottom: 20px;
            }

            /* ---------- Accent ---------- */
            .accent {
                color: #2ecc71;
                text-shadow: 0px 4px 16px rgba(0,0,0,0.3);
            }

            /* ---------- Inputs ---------- */
            .stTextInput > div > div > input {
                background-color: #9AA6B2;
                color: #000000;
                border: 1px solid #000000;
                border-radius: 0px;
                padding: 14px 16px;
                font-size: 15px;
            }

            .stTextInput > div > div > input::placeholder {
                color: #eeeeef;
                font-size: 16px;
            }

            /* ---------- Buttons (default) ---------- */
            .stButton > button {
                font-family: inherit;
                background-color: #BCCCDC;
                color: #000000;
                border: 1px solid #4b5563;
                border-radius: 4px;
                font-size: 16px;
                padding: 12px 18px;
                font-weight: 800;
                letter-spacing: 0.8px;
            }

            .stButton > button:hover {
                background-color: #AEBFD4;
            }

            /* ---------- Dividers ---------- */
            .custom-divider {
                width: 100%;
                height: 2px;
                background-color: #1f2937;
                opacity: 0.5;
                margin: 12px 0;
            }

            .custom-divider-center {
                width: 40%;
                height: 2px;
                background-color: #1f2937;
                opacity: 0.5;
                margin: 10px auto;
            }

            /* ---------- Cards (optional use) ---------- */
            .card {
                background-color: #E5EAF0;
                border: 1px solid #4b5563;
                padding: 20px;
                border-radius: 6px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.15);
            }

        </style>
        """,
        unsafe_allow_html=True
    )
