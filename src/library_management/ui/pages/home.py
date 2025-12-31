import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from assets.styles import apply_global_styles
from ui.components.header import Header
from ui.components.search_bar import SearchBar
from ui.components.cta_buttons import CTAButtons
from ui.components.featured_books import FeaturedBooks
import streamlit as st


if st.session_state.logged_in:  
    apply_global_styles()

    Header().render()
    SearchBar().render()
    CTAButtons().render()
    FeaturedBooks().render()
else:
    st.error("You Should Log in to Continue")