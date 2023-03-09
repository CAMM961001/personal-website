import utils
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

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

    def timeline(self):
        st.header('Timeline')
        st.write('This is my timeline')

        data = (
            pd.read_csv('assets/timeline.csv')
            .assign(fecha = lambda df_: pd.to_datetime(df_.fecha, format='%d/%m/%Y')))
        
        fig = go.Figure()

        for tipo in data['tipo'].unique():
            df_ = data.query(f"tipo=='{tipo}'")
            
            fig.add_trace(
                go.Scatter(
                    x=df_.fecha
                    ,y=df_.empresa
                    ,hovertext=df_.descripcion
                    ,name=df_.tipo.unique()[0]
                    ,text=df_.nombre
                    ,textposition='top center'
            ))

        fig.update_traces(
            line_width=8,
            marker_size=14)
        
        fig.update_layout(
            xaxis=dict(tickfont=dict(size=18))
            ,yaxis=dict(tickfont=dict(size=18))
        )

        st.plotly_chart(
                fig
                ,use_container_width=True
                ,sharing='streamlit'
                ,theme='streamlit')




    def skills_section(self):
        st.header("Skills & Software")
        st.write(f'''
        - Problem solving
        - Team-oriented leadership
        - Cross-functional team management
        - Advanced data analytics
        ''')
        analytics, dev, bi, storage = st.columns(4, gap='medium')
        with st.container():
            with analytics:
                header = '''
                <div style="text-align: center">
                    <h4>Advanced Analytics</h4>
                    <p></p>
                </div>
                '''
                st.markdown(header, unsafe_allow_html=True)
                #Plot
                fig = plt.figure(figsize=(6,6))
                ax = fig.add_subplot(projection='polar')

                packages = ['Numpy', 'Scipy','Pandas','Matplotlib','ScikitLearn','TensorFlow','Tidyverse', 'ggplot2']
                values = [10,8,10,10,8,7,6,7,10]
                
                # Initialise the spider plot by setting figure size and polar projection
                theta = np.linspace(0, 2 * np.pi, len(values))
                
                # Arrange the grid into number of sales equal parts in degrees
                lines, labels = plt.thetagrids(range(0, 360, int(360/len(packages))), (packages), fontsize=16)
                
                # Plot actual sales graph
                ax.plot(theta, values, color='green')
                ax.fill(theta, values, color='green', alpha=0.1)
                ax.set_yticks([5,6,7,8,9,10])
                ax.grid(alpha=0.4)

                #Add plot to streamlit
                st.pyplot(fig=fig)

            with dev:
                header = '''
                <div style="text-align: center">
                    <h4>Development</h4>
                    <p></p>
                </div>
                '''
                st.markdown(header, unsafe_allow_html=True)
                #Plot
                fig = plt.figure(figsize=(6,6))
                ax = fig.add_subplot(projection='polar')

                packages = ['Flask','SQL Connectors','Docker','Git-GitHub']
                values = [8,9,6,9,8]
                
                # Initialise the spider plot by setting figure size and polar projection
                theta = np.linspace(0, 2 * np.pi, len(values))
                
                # Arrange the grid into number of sales equal parts in degrees
                lines, labels = plt.thetagrids(range(0, 360, int(360/len(packages))), (packages), fontsize=16)
                
                # Plot actual sales graph
                ax.plot(theta, values, color='red')
                ax.fill(theta, values, color='red', alpha=0.1)
                ax.set_yticks([5,6,7,8,9,10])
                ax.grid(alpha=0.4)

                #Add plot to streamlit
                st.pyplot(fig=fig)

            with bi:
                header = '''
                <div style="text-align: center">
                    <h4>Bussines Inteligence</h4>
                    <p></p>
                </div>
                '''
                st.markdown(header, unsafe_allow_html=True)
                #Plot
                fig = plt.figure(figsize=(6,6))
                ax = fig.add_subplot(projection='polar')

                packages = ['Excel','Excel VBA','R Shiny', 'Streamlit']
                values = [10,7,7,9,10]
                
                # Initialise the spider plot by setting figure size and polar projection
                theta = np.linspace(0, 2 * np.pi, len(values))
                
                # Arrange the grid into number of sales equal parts in degrees
                lines, labels = plt.thetagrids(range(0, 360, int(360/len(packages))), (packages), fontsize=16)
                
                # Plot actual sales graph
                ax.plot(theta, values, color='blue')
                ax.fill(theta, values, color='blue', alpha=0.1)
                ax.set_yticks([5,6,7,8,9,10])
                ax.grid(alpha=0.4)

                #Add plot to streamlit
                st.pyplot(fig=fig)
            
            with storage:
                header = '''
                <div style="text-align: center">
                    <h4>Data Processing & Storage</h4>
                    <p></p>
                </div>
                '''
                st.markdown(header, unsafe_allow_html=True)
                #Plot
                fig = plt.figure(figsize=(6,6))
                ax = fig.add_subplot(projection='polar')

                packages = ['Postgres','SQLServer','SQLite', 'Bash']
                values = [9,8,7,8,9]
                
                # Initialise the spider plot by setting figure size and polar projection
                theta = np.linspace(0, 2 * np.pi, len(values))
                
                # Arrange the grid into number of sales equal parts in degrees
                lines, labels = plt.thetagrids(range(0, 360, int(360/len(packages))), (packages), fontsize=16)
                
                # Plot actual sales graph
                ax.plot(theta, values, color='purple')
                ax.fill(theta, values, color='purple', alpha=0.1)
                ax.set_yticks([5,6,7,8,9,10])
                ax.grid(alpha=0.4)

                #Add plot to streamlit
                st.pyplot(fig=fig)
        
        st.write("###")
        st.markdown(
            f'''<div style="font-size: 15px; text-align: center">
                    Software mastery scale ranges from 1 as minimum  value to 10 as maximum value
                </div>''', unsafe_allow_html=True)