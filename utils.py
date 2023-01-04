import requests
import streamlit as st

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None    
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

class Settings:
    def __init__(self):
        self.page_title = "Miguel Castaneda"
        self.layout = "wide"
        self.pages = ['Home', 'Resume', 'Portfolio', 'Contact Me']
        self.menu_icons = ['house', 'book', 'folder2-open', 'envelope']
        self.fontsize = 20

        #URL for other websites
        self.itam_url = '<a href="https://mcdatos.itam.mx/es" style="color: #F63366; text-decoration:none;">ITAM</a>'
        self.inai_url = '<a href="https://home.inai.org.mx/" style="color: #F63366; text-decoration:none;">INAI</a>'
        self.cdas_url = '<a href="https://www.facebook.com/dataalgosocitam/" style="color: #F63366; text-decoration:none;">CDAS</a>'
        self.pross_url = '<a href="https://ppross.mx/" style="color: #F63366; text-decoration:none;">Procesos PROSS</a>'
        self.bilstein_url = '<a href="https://bilstein.com/en-us/about-us/" style="color: #F63366; text-decoration:none;">Bilstein Shock Absorbers</a>'
        self.fsae_url = '<a href="https://www.fsaeonline.com/" style="color: #F63366; text-decoration:none;">FSAE</a>'
        self.unam_url = '<a href="http://www.fi-a.unam.mx/" style="color: #F63366; text-decoration:none;">UNAM School of Engineering</a>'
        self.unammotorsports = '<a href="https://unam.pro/" style="color: #F63366; text-decoration:none;">UNAM Motorsports</a>'