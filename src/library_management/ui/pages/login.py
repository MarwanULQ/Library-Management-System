import streamlit as st

# ---------------- Page config ----------------
st.set_page_config(
    page_title="YLibrary | Login",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------- Dark Styling ----------------
st.markdown(
    """
    <style>
        .stApp {
            background-color: #0f172a; /* dark slate */
            color: #e5e7eb;
            font-family: "Georgia", "Times New Roman", serif;
        }

        h1, h2, h3, p {
            font-family: inherit;
            color: #e5e7eb;
        }

        .stTextInput > div > div > input {
            background-color: #1e293b;
            color: #e5e7eb;
            border: 1px solid #334155;
        }

        .stTextInput > div > div > input::placeholder {
            color: #94a3b8;
        }

        .stButton > button {
            background-color: #1e293b;
            color: #e5e7eb;
            border: 1px solid #334155;
            font-weight: 700;
        }

        .stButton > button:hover {
            background-color: #334155;
        }

        hr {
            border: 1px solid #334155;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- Session state ----------------
if "choicef" not in st.session_state:
    st.session_state.choicef = False
if "new" not in st.session_state:
    st.session_state.new = False
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- Header ----------------
st.markdown(
    """
    <h1 style="text-align:center;">
        <span style="color:#2ecc71;">Y</span>Library 📚
    </h1>
    <p style="text-align:center; font-style:italic; color:#94a3b8;">
        Secure access to knowledge and services
    </p>
    """,
    unsafe_allow_html=True
)

# ---------------- Login / Signup choice ----------------
col1, col2 = st.columns(2)

with col1:
    if st.button("Login", key="choose_login", use_container_width=True):
        st.session_state.choicef = True
        st.session_state.new = False

with col2:
    if st.button("Sign Up", key="choose_signup", use_container_width=True):
        st.session_state.choicef = True
        st.session_state.new = True

st.markdown("---")

# ---------------- Forms ----------------
if st.session_state.choicef:

    username = st.text_input("Username")

    if st.session_state.new:
        email = st.text_input("Email")

    password = st.text_input("Password", type="password")

    action = "Sign Up" if st.session_state.new else "Login"

    if st.button(
        action,
        key="submit_signup" if st.session_state.new else "submit_login",
        use_container_width=True
    ):
        if username and password and (not st.session_state.new or "@ejust.edu.eg" in email):
            st.session_state.logged_in = True
            st.switch_page("pages/home.py")
        else:
            if "@ejust.edu.eg" not in email:
                st.error("Don't have access to the Uni Library. You should have an E-JUST Email.")
            else:
                st.error("Please fill all fields correctly")