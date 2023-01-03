import utils
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

#Site settings
settings = utils.Settings()
st.set_page_config(page_title=f"{settings.page_title} - Home", layout=settings.layout)

#Site assets
profile_pict = Image.open("./images/Profile.jpg")

#Horizontal menu
selected = option_menu(
    menu_title=None,
    options=['Home', 'Resume', 'Portfolio', 'Contact Me'],
    icons=['house', 'book', 'folder2-open', 'envelope'],
    menu_icon='cast',
    default_index=0,
    orientation='horizontal'
)

#Pages
if selected == 'Home':
    with st.container():
        st.title("About Me")
        content, contact_info = st.columns((2, 1))

        with contact_info:
            st.image(profile_pict)
            st.header("Miguel Castañeda")
            st.subheader("A Data Scientist from Mexico")
            st.write("Contact information")
            st.write(f"""
            <a target="_self" href="https://github.com/CAMM961001">
                <button>GitHub</button></a>""", unsafe_allow_html=True)

elif selected == "Resume":
    with st.container():
        st.title("Resume")

elif selected == "Portfolio":
    with st.container():
        st.title("Portfolio")

elif selected == "Contact Me":
    with st.container():
        utils.local_css("./style/style.css")
        aboutme_animation = utils.load_lottie_url("https://assets3.lottiefiles.com/packages/lf20_v7gj8hb1.json")
        
        st.title("Contact Me")
        left_column, right_column = st.columns((2,1))
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
            st_lottie(aboutme_animation, height=350, key="data science")
        