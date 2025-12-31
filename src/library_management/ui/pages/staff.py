from assets.styles import apply_global_styles
from ui.components.staff_header import StaffHeader
from ui.components.staff_tabs import StaffTabs
import streamlit as st


apply_global_styles()
StaffHeader().render()
StaffTabs().render()