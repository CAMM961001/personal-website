import utils
import streamlit as st
from streamlit_lottie import st_lottie

settings = utils.Settings()
st.set_page_config(page_title=f"{settings.page_title} - Contact", layout=settings.layout)

#Aassets
aboutme_animation = utils.load_lottie_url("https://assets7.lottiefiles.com/packages/lf20_x17ybolp.json")

#About me
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Contact me")
        st.write("##")
        st.write("""
        Write here 'contact me' section
        """)
    with right_column:
        st_lottie(aboutme_animation, height=200, key="data science")