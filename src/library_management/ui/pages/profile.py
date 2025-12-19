import streamlit as st

def show_profile_page(user_data):
    st.set_page_config(page_title="Profile", layout="wide")

    # ---------- Custom CSS ----------
    st.markdown("""
        <style>
                
        .profile-title {
            font-size: 26px;
            font-weight: 700;
            margin-bottom: 6px;
        }

        .profile-sub {
            color: #a6a6a6;
            font-size: 15px;
            margin-bottom: 12px;
        }

        .profile-field {
            font-size: 16px;
            margin-bottom: 6px;
        }

        .stTabs [data-baseweb="tab"] {
            font-size: 15px;
            padding: 10px 16px;
        }

        .stButton > button {
            width: 100%;
            border-radius: 8px;
            font-weight: 600;
        }
        </style>
    """, unsafe_allow_html=True)

    # ---------- Page Title ----------
    st.markdown("## 👤 User Profile")

    _, col = st.columns([1, 2])

    with col:

        st.markdown(
            f'<div class="profile-title">{user_data.get("name", "N/A")}</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="profile-sub">Member since {user_data.get("join_date", "N/A")}</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="profile-field"><b>Email:</b> {user_data.get("email", "N/A")}</div>',
            unsafe_allow_html=True
        )

        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    # ---------- Tabs ----------
    tab1, tab2, tab3 = st.tabs(["📚 Borrowed Books", "⚙️ Account Settings", "📊 Activity"])

    with tab1:
        st.subheader("Currently Borrowed")
        borrowed = user_data.get('borrowed_books', [])

        if borrowed:
            for book in borrowed:
                st.markdown(
                    f"- **{book['title']}**  \n  _Due:_ `{book['due_date']}`"
                )
        else:
            st.info("No books borrowed")

    with tab2:
        st.subheader("Account Settings")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔐 Change Password", key="change_password"):
                st.session_state.show_password_form = True

        with col2:
            if st.button("✏️ Update Profile", key="update_profile"):
                st.session_state.show_profile_form = True

    with tab3:
        st.subheader("Activity History")
        st.caption("Recent activities will appear here")


# ---------- Sample Data ----------
sample_user = {
    'name': 'John Doe',
    'email': 'john@example.com',
    'member_id': '12345',
    'join_date': '2023-01-15',
    'borrowed_books': []
}

show_profile_page(sample_user)
