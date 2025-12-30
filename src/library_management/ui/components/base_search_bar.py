import streamlit as st
from ui.components.base import BaseComponent
from abc import ABC, abstractmethod

class BaseSearchBar(BaseComponent, ABC):
    def __init__(self, placeholder: str, initial_value: str = ""):
        self.placeholder = placeholder
        self.initial_value = initial_value

    def render(self):
        st.markdown("<div style='margin-top:10px'></div>", unsafe_allow_html=True)

        _, col2, _ = st.columns([1, 3, 1])
        with col2:
            value = st.text_input(
                "",
                value=self.initial_value,
                placeholder=self.placeholder
            )

            self.on_change(value)

    @abstractmethod
    def on_change(self, value: str):
        pass
