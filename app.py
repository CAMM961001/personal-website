import utils
import streamlit as st
import streamlit.components.v1 as components

from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

from about_me import AboutMe
from resume import Resume
from contact import Contact

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
    orientation='horizontal')

# --- ABOUT ME ---
if selected == settings.pages[0]:
    about_me = AboutMe()

    st.title(about_me.page_title)
    content, personl_info = st.columns((2.5, 1), gap='large')
    with st.container():
        with content:
            about_me.main_content()
        with personl_info:
            about_me.personal_info()
    
    st.write("---")

# --- RESUME ---
elif selected == settings.pages[1]:
    resume = Resume()

    st.title(resume.page_title)
    resume.header_section()
    st.write('---')
    resume.education_section()
    st.write('---')
    resume.job_section()
    st.write('---')
    resume.skills_section()
    st.write('---')

# --- PORTFOLIO ---
elif selected == settings.pages[2]:
    with st.container():
        st.title("Portfolio")

        HtmlFile = open("./assets/test2.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        print(source_code)
        components.html(source_code, height=600, scrolling=True)

# --- CONTACT ---
elif selected == settings.pages[3]:
    contact = Contact()
    st.title(contact.page_title)
    utils.social_media_buttons(align='left')

    with st.container():
        email_animation = utils.load_lottie_url("https://assets3.lottiefiles.com/packages/lf20_v7gj8hb1.json")
        
        left_column, right_column = st.columns((2,1))
        with left_column:
            st.write("##")
            contact.render_contact_form()
        with right_column:
            st_lottie(email_animation, height=350, key="data science")

    st.write('---')

settings.site_footer()