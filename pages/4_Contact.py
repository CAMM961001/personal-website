import utils
import streamlit as st
from streamlit_lottie import st_lottie

settings = utils.Settings()
st.set_page_config(page_title=f"{settings.page_title} - Contact", layout=settings.layout)
utils.local_css("./style/style.css")

#Aassets
aboutme_animation = utils.load_lottie_url("https://assets3.lottiefiles.com/packages/lf20_v7gj8hb1.json")

#About me
with st.container():
    st.title("Contact Me")
    left_column, right_column = st.columns(2)
    contact_form = """
        <form action="https://formsubmit.co/miguel.castama@outlook.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Name" required>
            <input type="email" name="email" placeholder="Email" required>
            <textarea name="message" placeholder="Leave a message" required></textarea>
            <button type="submit">Send</button>
        </form>"""
    with left_column:
        st.write("##")
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st_lottie(aboutme_animation, height=300, key="data science")