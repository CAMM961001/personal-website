import utils
import streamlit as st
from PIL import Image

settings = utils.Settings()

class AboutMe:
    def __init__(self):
        self.page_title = 'About Me'
        self.profile_pict = Image.open('./assets/Profile.png')

    def main_content(self):
        content = f'''
        <p style="text-align: justify; font-size: {settings.fontsize}px">
            <br>
            I am a data scientist with expierence in manufacturing processes for automotive industry, and
            automation services for financial sector. I am currently studying a full time MSc. in Data 
            Science at {settings.itam_url}, where I additionally volunteer as Data Scientist with {settings.inai_url}
            (Mexico's National Institue for Information Accessibility) through {settings.cdas_url}, which is ITAM's
            extracurricular organization responsible for tackling diverse social topics powered by data
            analytics. In here, I employ web scrapping and NLP technics to leverage INAI's capabilities
            to foresee public domain trending topics.
            </br>
            <br>
            Prior to this, I worked at {settings.pross_url} initially as Compliance Analyst and then as Project
            Manager for a year and a half. Before that, I perfomed an engineering role with the Manufacturing
            Proces Plann Team at {settings.bilstein_url}. In addition, during my Bachelor in Mechanical Engineering
            at {settings.unam_url}, I participated during four years in the {settings.fsae_url} design series with
            {settings.unammotorsports} which is UNAM's representative team in the category. In here, I played
            the role of Design Engineer in seasons 2016 - 2017, D&M Engineering Principal in season 2018,
            and Team Principal in season 2019.
            </br>
            <br>
            Finally, 
            </br>
        </p>'''
        
        st.markdown(content, unsafe_allow_html=True)

    def personal_info(self):
        content = f'''
        <div style="text-align: center">
            <h2>Miguel Ángel Castañeda Martínez</h2>
            <h4>Data Scientist from Mexico</h3>
            <p style="font-size: {settings.fontsize}px">
            </p>
        </div>'''
        
        st.image(self.profile_pict)
        st.markdown(content, unsafe_allow_html=True)
        
        #Github and Linkedin buttons
        utils.social_media_buttons()