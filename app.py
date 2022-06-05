import streamlit as st
from streamlit_option_menu import option_menu
from pages import home, dataset, model, predict, me
from PIL import Image
from pages.other_function import *

def app():
    img = Image.open("img/page_icon.png")
    st.set_page_config(page_title="Sales Dashboard",
                       page_icon=img,
                       layout="wide",
                       initial_sidebar_state="auto")

    # Custom CSS
    with open("css/style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Bootstrap CSS
    st.markdown(""" <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous" />""", unsafe_allow_html=True)

    # Bootsrap Javascript
    st.markdown("""<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4" crossorigin="anonymous"></script>""", unsafe_allow_html=True)

    # Google Fonts
    st.markdown("""<link rel="preconnect" href="https://fonts.gstatic.com" />
    <link href="https://fonts.googleapis.com/css2?family=Viga&display=swap" rel="stylesheet" />""", unsafe_allow_html=True)
    
    # Font Awesome Icons
    st.markdown("""<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" />""", unsafe_allow_html=True)

    with st.sidebar:
        selected = option_menu(
            menu_title='Main Menu',
            options=['Home', 'Dataset', 'Model', 'Predict', 'Me'],
            icons=['house', 'table', 'robot', 'graph-up-arrow', 'person-circle'],
            menu_icon='cast',
            default_index=0
        )

    dict_function = {
        "Home": home,
        "Dataset": dataset,
        "Model": model,
        "Predict": predict,
        "Me": me
    }

    dict_function[selected].app()  

app()