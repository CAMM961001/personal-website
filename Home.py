#References: https://www.youtube.com/watch?v=VqgUkExPvLY&t=14s
import utils
import streamlit as st
from PIL import Image

#Site settings
settings = utils.Settings()
st.set_page_config(page_title=f"{settings.page_title} - Home", layout=settings.layout)
st.title("About Me")
st.sidebar.empty()

#Site assets
profile_pict = Image.open("./images/Profile.jpg")

#About me section
with st.container():
    
    content, contact_info = st.columns((2, 1))

    with contact_info:
        st.image(profile_pict)
        st.header("Miguel Castañeda")
        st.subheader("A Data Scientist from Mexico")
        st.write("Contact information")
        st.write("""[LinkedIn](https://www.linkedin.com/in/miguel-angel-castaneda-martinez-b0a566142/)
        [GitHub](https://github.com/CAMM961001)""")
