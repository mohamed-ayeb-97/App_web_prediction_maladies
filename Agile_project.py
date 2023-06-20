import streamlit as st
from page0 import page0
from page1 import page1
from page2 import page2
from page3 import page3
from page4 import page4

def ml():

    #st.set_page_config(page_title="E-Healthcare", layout="wide")

    page = st.sidebar.selectbox('Select a Disease', (
    "Paga d'Acceuil", 'Défaillance Cardiaque', 'Diabète', 'Maladie de Foie', 'Cancer de Sein'))

    if page == """Paga d'Acceuil""":
        page0()
    elif page == 'Défaillance Cardiaque':
        page1()
    elif page == 'Diabète':
        page2()
    elif page == 'Maladie de Foie':
        page3()
    elif page == 'Cancer de Sein':
        page4()

