import streamlit as st
import os
from constant import *


st.set_page_config(page_title="Contacts", page_icon="🌏", layout="wide",initial_sidebar_state="collapsed")
margin_r,body,margin_l = st.columns([0.4, 3, 0.4])


with body:
    menu()
    st.header("🌏 Contacts",divider='orange')
    st.subheader(f"✉️ Email: {email}")


    with st.container():
        col1, col2 = st.columns([0.1, 3])
        with col1:
            st.write(linkedin_logo, unsafe_allow_html=True)
        with col2:
            st.subheader(f"LinkedIn: ")
    with st.container():
        col1, col2 = st.columns([0.1, 3])
        with col1:
            st.write(github_logo, unsafe_allow_html=True)
        with col2:
            st.subheader(f" Github: {github}")
            



