import json
import utils
import streamlit as st

settings = utils.Settings()

class Portfolio:
    def __init__(self):
        self.page_title = 'Portfolio'
        self.contets = './portfolio/projects.json'
        with open(self.contets) as f:
            self.data = json.load(f)['projects']
        f.close()


    def first_row(self):
        with st.container():
            col1, col2, col3 = st.columns(3, gap='large')
            with col1:
                st.caption(self.data[0]['contributors'])
                description = ""
                for line in self.data[0]['description']:
                    description += line
                
                description = f'''<p style="text-align: justify; font-size: 18px">{description}</p>'''
                st.markdown(description, unsafe_allow_html=True)
                utils.render_button(url='https://camm961001.quarto.pub/un-enfoque-bayesiano/')