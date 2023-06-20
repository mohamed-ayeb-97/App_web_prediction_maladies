
import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
import requests

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_uuxhjual.json")

#Header Section :

def page0():

    with st.container():
        st.title("Welcome to the E-Healthcare ML Web App!")
        st.subheader("How can I help you today ?")

    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)

        with left_column:
            st.header("What I do")
            st.write("##")
            st.write("""
            Machine learning in healthcare is becoming more widely used and
            is helping patients and clinicians by overcoming industry challenges 
            and creating a more unified system to improve work processes.
            I'm Here to Help you predict many diseases and remove any uncertainties 
            you may have through the power of Machine Learning   
            I have been trained on big datasets and by the best Models
            Here's the Diseases i can help you predict with their respective Accuracy:
        
            """
                     )
            df = pd.DataFrame({'The Disease': ["Défaillance Cardiaque", "Diabète", "Maladie de Foie", "Cancer de Sein"],
                               'Accuracy': ["85.21%", "79.95%", "84.65%", "95.80%"]})
        st.dataframe(df, height=400)

        with right_column:
            st_lottie(lottie_coding, key="ML", height= 350)

    #Disease_Name = st.sidebar.selectbox('Select a Disease', ("""Paga d'Acceuil""", 'Défaillance Cardiaque', 'Diabète', 'Maladie de Rein', 'Disease 4'))

