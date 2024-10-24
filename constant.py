import streamlit as st


def menu():
    bar0, bar1, bar2, bar3, bar4= st.columns([0.1,1,1,1,1])
    bar1.page_link("homepage.py", label="Introduction", icon="🏠")
    bar2.page_link("pages/1_experience.py", label= "Experience", icon="📚")
    bar3.page_link("pages/2_portfolio.py", label="Portofolio", icon="📁")
    bar4.page_link("pages/3_contacts.py", label="Contacts", icon="🌏")
    st.write("")



info = {
        'brief' : """I found my passion for computer science 
        in high school after several great experiences 
        with a fantastic teacher. I am now pursuing my 
        Bachelors Degree in CS at Messiah University. I am 
        eager to dive deeper into my education and find an 
        area of specificity within the broad realm of Computer Science.""",
        'name' : 'Brad Kreider',
        'institution' : 'Messiah University',
        'location' : 'Mechanicsburg, PA',
        'interest' : 'Computer Science',
    }