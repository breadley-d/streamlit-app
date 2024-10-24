import streamlit as st
import os
from constant import *



st.set_page_config(page_title="Main Page", layout="wide", initial_sidebar_state="collapsed", page_icon="🏠")

margin_r,body,margin_l = st.columns([0.4, 3, 0.4])





with body:
    menu()

    with st.sidebar:
        st.success("Select a page above.")

    st.title("Brad Kreider")
    st.subheader(":orange[Aspiring Computer Scientist]", divider="orange")
    col1, col2, col3 = st.columns([1.3 ,0.2, 1])
    

    with col1:
            st.write(info['brief'])
            
            st.markdown(f"###### 👨‍💼 :orange[Name:] {info['name']}")
            st.markdown(f"###### 🏫 :orange[Institution:] {info['institution']}")
            st.markdown(f"###### 📍 :orange[Location:] {info['location']}")
            st.markdown(f"###### 📚 :orange[Interest:] {info['interest']}")
            #st.markdown(f"###### 👀 Linkedin: {linkedin_link}")

            #with open("src/resume.pdf", "rb") as file:
            #pdf_file = file.read()

            #st.download_button(
                #label="Download my :blue[resume]",
                #data=pdf_file,
                #file_name="resume",
                #mime="application/pdf")

    with col3:
        st.image("static/profile_img.jpeg", width=350)

    st.subheader("", divider="orange")


