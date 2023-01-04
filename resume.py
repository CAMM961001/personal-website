import json
import utils
import streamlit as st

settings = utils.Settings()

class Resume:
    def __init__(self):
        self.page_title = 'Resume'
        self.resume_file = './assets/resume.pdf'
        self.resume_contets = './assets/resume_contents.json'
        self.resume_description = f'''
        <p style="font-size: {settings.fontsize}px">
        Data Scientist & Masters candidate, <br>
        assisting enterprises towards data driven decisions.
        </p>
        '''
        

    def header_section(self):
        st.markdown(self.resume_description, unsafe_allow_html=True)
        
        with open(self.resume_file, 'rb') as f:
            resume_pdf = f.read()
            st.download_button(
                label='Download Resume',
                data=resume_pdf,
                file_name='Resume.pdf',
                mime='application/octet-stream')
        f.close()

    def education_section(self):
        st.title("Education")
        with open(self.resume_contets) as f:
            data = json.load(f)['education']
            
            for idx in reversed(range(len(data))):
                with st.container():
                    date, content = st.columns((1, 2), gap='medium')
                    with date:
                        date_content = f'''
                        <div style="text-align: right">
                            <p style="font-size: {settings.fontsize}px">{data[idx]['date']}</p>
                        </div>
                        '''
                        st.markdown(date_content, unsafe_allow_html=True)

                    with content:
                        content = f'''
                        <div style="text-align: left">
                            <h4>{data[idx]['univ']}</h4>
                            <p style="font-size: {settings.fontsize}px">
                                {data[idx]['degree']}
                            </p>
                        </div>
                        '''
                        st.markdown(content, unsafe_allow_html=True)
                st.write('##')
        f.close()


        