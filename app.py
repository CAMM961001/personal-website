import utils
import streamlit as st

from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

from about_me import AboutMe
from resume import Resume

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
    content, personl_info = st.columns((2, 1), gap='large')

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
    resume.work_section()
    st.write('---')
    resume.skills_section()
    st.write('---')

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

        #Contact form
        left_column, right_column = st.columns((2,1))
        contact_form = """
            <form action="https://formsubmit.co/miguel.castama@outlook.com" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Name" required>
                <input type="email" name="email" placeholder="Email" required>
                <textarea name="message" placeholder="Leave a message" required></textarea>
                <button type="submit">Send</button>
            </form>
            <div style="text-align: left"><p></p>
                <p>
                    <a href="https://github.com/CAMM961001">
                        <button type="button" class="btn btn-success">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-github" viewBox="0 0 16 16">
                                <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
                            </svg>
                            GitHub
                        </button>
                    </a>
                    <a href="https://www.linkedin.com/in/miguel-angel-castaneda-martinez-b0a566142/">
                        <button type="button" class="btn btn-success">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-linkedin" viewBox="0 0 16 16">
                                <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
                            </svg>
                            LinkedIn
                        </button>
                    </a>
                </p>
            </div>"""
        with left_column:
            st.write("##")
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st_lottie(aboutme_animation, height=350, key="data science")