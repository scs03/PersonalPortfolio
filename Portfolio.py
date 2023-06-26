import streamlit as st
from PIL import Image


st.set_page_config(page_title="Sriram's Portfolio", page_icon=":wave:", layout="wide")

# --- CSS IMPORT ---
# with open('style.css') as f:
#    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# -- PRE-LOADING FILES ---
selfPortrait = Image.open("images/KTPHeadshot_copy.jpeg")
sfBackground = Image.open("images/SF_Sruti.jpeg")
# --- MENU BAR ---

# --- HEADER ---
with st.container():
    st.write("---")
    introduction, photo = st.columns(2)
    with introduction:
        st.subheader("NEUROSCIENCE")
        st.subheader("STUDENT")
        st.write("I am passionate about finding ways to bridge the fields (and my fields of interest) "
                 "neuroscience and computer science together")
        st.write("[LinkedIn](https://www.linkedin.com/in/sriramsendhil)")
    with photo:
        st.image(selfPortrait)

# --- ABOUT ME ---
with st.container():
    st.write("---")
    aboutMe, information = st.columns(2)
    with aboutMe:
        st.title("ABOUT ME")
        # INSERT BACKGROUND IMAGE
    with information:
        st.write("""
        Hi! My name is Sriram Sendhil and I am a third year undergraduate student transitioning to Computer Science 
        from a background Neuroscience (Pre-medical). I am an ambitious and motivated individual now starting a new 
        chapter in computer science from my deep fascination for the intersection of technology and human cognition. 
        I intend to leverage my analytical mindset, problem-solving abilities, and thirst for learning in order to 
        embark and succeed in my new chapter.

        Currently I am making strides to improve my portfolio by completing personal projects, courses, taking part in
         hackathons, and participating in clubs/organizations surrounding aspects of Computer Science. Currently I am 
         strengthening my skills in: C/C++, Python, HTML/CSS/JS and working with developer tools such as: GitHub and 
         VSCode. """)

# --- PROJECTS ---
with st.container():
    st.write("---")
    # Row 1
    st.title("Projects")
    Project1, Project2, Project3 = st.columns(3)
    with Project1:
        st.image(sfBackground)
        st.write("Still in construction :)")
    with Project2:
        st.image(sfBackground)
        st.write("Still in construction :)")
    with Project3:
        st.image(sfBackground)
        st.write("Still in construction :)")
    # Row 2
    Project4, Project5, Resume = st.columns(3)
    with Project4:
        st.image(sfBackground)
        st.write("Still in construction :)")
    with Project5:
        st.image(sfBackground)
        st.write("Still in construction :)")
    with Resume:
        st.write("[Click Here>]")

# --- CONTACTS ---

with st.container():
    st.write("---")
    st.subheader("Contact Me")

