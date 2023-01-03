import utils
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from about_me import AboutMe

#Site settings
settings = utils.Settings()
st.set_page_config(page_title=f"{settings.page_title} - Home", layout=settings.layout)

# --- HORIZONTAL MENU ---
selected = option_menu(
    menu_title=None,
    options=settings.pages,
    icons=settings.menu_icons,
    menu_icon='cast',
    default_index=0,
    orientation='horizontal'
)

# --- ABOUT ME ---
if selected == settings.pages[0]:
    about_me = AboutMe()
    st.title(about_me.page_title)
    content, personl_info = st.columns((2, 1), gap='large')

    with st.container():
        with content:
            about_me.main_content()
        with personl_info:
            about_me.personal_info()

# --- RESUME ---
elif selected == settings.pages[1]:
    with st.container():
        st.title("Resume")

# --- PORTFOLIO ---
elif selected == settings.pages[2]:
    with st.container():
        st.title("Portfolio")

# --- CONTACT ---
elif selected == settings.pages[3]:
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