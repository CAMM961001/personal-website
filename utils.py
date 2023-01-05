import requests
import streamlit as st

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None    
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def social_media_buttons(align='center'):
    social_media = f"""
            <div style="text-align: {align}"><p></p>
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
                </div>
            """
    st.markdown(social_media, unsafe_allow_html=True)

def render_button(url, align='center'):
    button = f"""
            <div style="text-align: {align}"><p></p>
                <a href="{url}">
                    <button type="button" class="btn btn-outline-danger">
                        View site
                    </button>
                </a>
            </div>
            """
    st.markdown(button, unsafe_allow_html=True)

class Settings:
    def __init__(self):
        self.page_title = "Miguel Castaneda"
        self.layout = "wide"
        self.pages = ['Home', 'Resume', 'Portfolio', 'Contact Me']
        self.menu_icons = ['house', 'book', 'folder2-open', 'envelope']
        self.fontsize = 20

        #URL for other websites
        self.site_repo = '''<a href="https://github.com/CAMM961001/personal-website" style="color: #F63366; text-decoration:none;">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-git" viewBox="0 0 16 16">
            <path d="M15.698 7.287 8.712.302a1.03 1.03 0 0 0-1.457 0l-1.45 1.45 1.84 1.84a1.223 1.223 0 0 1 1.55 1.56l1.773 1.774a1.224 1.224 0 0 1 1.267 2.025 1.226 1.226 0 0 1-2.002-1.334L8.58 5.963v4.353a1.226 1.226 0 1 1-1.008-.036V5.887a1.226 1.226 0 0 1-.666-1.608L5.093 2.465l-4.79 4.79a1.03 1.03 0 0 0 0 1.457l6.986 6.986a1.03 1.03 0 0 0 1.457 0l6.953-6.953a1.031 1.031 0 0 0 0-1.457"/>
        </svg></a>'''
        self.streamlit_url = '<a href="https://streamlit.io/" style="color: #F63366; text-decoration:none;">Streamlit</a>'
        self.itam_url = '<a href="https://mcdatos.itam.mx/es" style="color: #F63366; text-decoration:none;">ITAM</a>'
        self.inai_url = '<a href="https://home.inai.org.mx/" style="color: #F63366; text-decoration:none;">INAI</a>'
        self.cdas_url = '<a href="https://www.facebook.com/dataalgosocitam/" style="color: #F63366; text-decoration:none;">CDAS</a>'
        self.pross_url = '<a href="https://ppross.mx/" style="color: #F63366; text-decoration:none;">Procesos PROSS</a>'
        self.bilstein_url = '<a href="https://bilstein.com/en-us/about-us/" style="color: #F63366; text-decoration:none;">Bilstein Shock Absorbers</a>'
        self.fsae_url = '<a href="https://www.fsaeonline.com/" style="color: #F63366; text-decoration:none;">FSAE</a>'
        self.unam_url = '<a href="http://www.fi-a.unam.mx/" style="color: #F63366; text-decoration:none;">UNAM School of Engineering</a>'
        self.unammotorsports = '<a href="https://unam.pro/" style="color: #F63366; text-decoration:none;">UNAM Motorsports</a>'

    def site_footer(self):
        footer = f'''
        <p style="text-align: center; font-size: 15px">
            <br>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-c-circle" viewBox="0 0 16 16">
                <path d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8Zm15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0ZM8.146 4.992c-1.212 0-1.927.92-1.927 2.502v1.06c0 1.571.703 2.462 1.927 2.462.979 0 1.641-.586 1.729-1.418h1.295v.093c-.1 1.448-1.354 2.467-3.03 2.467-2.091 0-3.269-1.336-3.269-3.603V7.482c0-2.261 1.201-3.638 3.27-3.638 1.681 0 2.935 1.054 3.029 2.572v.088H9.875c-.088-.879-.768-1.512-1.729-1.512Z"/>
            </svg> Miguel Castaneda 2023</br>
            Made with {self.site_repo} and {self.streamlit_url}</br>
        </p>'''
        
        st.markdown(footer, unsafe_allow_html=True)