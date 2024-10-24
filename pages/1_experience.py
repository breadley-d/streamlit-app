import streamlit as st
import os
from constant import *


st.set_page_config(page_title="Experience", page_icon="📚", layout="wide",initial_sidebar_state="collapsed")
margin_r,body,margin_l = st.columns([0.4, 3, 0.4])


with body:
    menu()

    st.header("📚 Experience",divider='orange')
    st.write("")