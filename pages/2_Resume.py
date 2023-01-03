import utils
import streamlit as st

settings = utils.Settings()
st.set_page_config(page_title=f"{settings.page_title} - Resume", layout=settings.layout)

st.title('Resume')