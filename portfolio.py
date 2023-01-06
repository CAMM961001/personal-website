import json
import utils
import streamlit as st
from PIL import Image

settings = utils.Settings()

class Portfolio:
    def __init__(self):
        self.page_title = 'Portfolio'
        self.contets = './assets/projects.json'
        with open(self.contets) as f:
            self.data = json.load(f)['projects']
        f.close()


    def first_row(self):
        with st.container():
            col1, col2, col3= st.columns(3, gap='large')
            with col1:
                cover = Image.open('./assets/bayesian-approach.png')
                st.subheader(self.data[0]['project_name'])
                st.caption(self.data[0]['contributors'])
                st.image(cover)
                description = ""
                for line in self.data[0]['description']:
                    description += line
                description = f'''<p style="text-align: justify; font-size: 15px">{description}</p>'''
                st.markdown(description, unsafe_allow_html=True)
                utils.render_button(url='https://camm961001.quarto.pub/un-enfoque-bayesiano/')