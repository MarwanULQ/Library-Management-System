import streamlit as st
from ui.components.base import BaseComponent
from ui.components.room_card import RoomCard

class RoomGrid(BaseComponent):
    def __init__(self, manager):
        self.manager = manager

    def render(self):
        cols = st.columns(2)
        col_idx = 0

        for room in self.manager.get_all_rooms().values():
            with cols[col_idx % 2]:
                RoomCard(room).render()
            col_idx += 1
