#References: https://www.youtube.com/watch?v=VqgUkExPvLY&t=14s
import utils
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Miguel Castaneda", page_icon=":tada:", layout="wide")

#Website assets
aboutme_animation = utils.load_lottie_url("https://assets7.lottiefiles.com/packages/lf20_x17ybolp.json")

#Header section
with st.container():
    st.subheader("Hi, I am Miguel :wave:")
    st.title("A Data Scientist from Mexico")
    st.write("This is my personal website")
    st.write("[LinkedIn](https://www.linkedin.com/in/miguel-angel-castaneda-martinez-b0a566142/)")

#About me
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("ABout me")
        st.write("##")
        st.write("""
        Write here 'about me' section
        """)
    with right_column:
        st_lottie(aboutme_animation, height=200, key="data science")


