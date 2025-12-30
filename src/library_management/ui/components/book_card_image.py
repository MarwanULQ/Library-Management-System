
import streamlit as st
from ui.components.base_book_card import BaseBookCard

class ImageOnlyBookCard(BaseBookCard):
    def render(self):
        if self.book.cover:
            st.image(self.book.cover, use_container_width=True)
