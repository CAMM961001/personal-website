import json
import utils
import streamlit as st

settings = utils.Settings()

class Portfolio:
    def __init__(self):
        self.page_title = 'Portfolio'
        self.contets = './portfolio/projects.json'