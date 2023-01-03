import streamlit as st
from PIL import Image

class AboutMe:
    def __init__(self):
        self.page_title = "About Me"
        self.profile_pict = Image.open("./images/Profile.jpg")

    def personal_info(self):
        st.image(self.profile_pict)
        st.header("Miguel Castañeda")
        st.subheader("A Data Scientist from Mexico")
        st.write("Contact information")
        st.write(f"""
        <a target="_self" href="https://github.com/CAMM961001">
            <button>GitHub</button></a>""", unsafe_allow_html=True)