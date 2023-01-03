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
