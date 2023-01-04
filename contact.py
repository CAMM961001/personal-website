import utils
import streamlit as st

settings = utils.Settings()

class Contact:
    def __init__(self):
        self.page_title = 'Contact Me'

    def render_contact_form(self):
        contact_form = """
                <form action="https://formsubmit.co/miguel.castama@outlook.com" method="POST">
                    <input type="hidden" name="_captcha" value="false">
                    <input type="text" name="name" placeholder="Name" required>
                    <input type="email" name="email" placeholder="Email" required>
                    <textarea name="message" placeholder="Leave a message" required></textarea>
                    <button type="submit">Send</button>
                </form>
                """
        st.markdown(contact_form, unsafe_allow_html=True)