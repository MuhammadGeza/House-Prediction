import streamlit as st
from pages.other_function import *


def app():
    image = decode_img("img/boston.jpg")

    st.markdown("""
        <h1>
            Random forest to predict house prices
        </h1>""", unsafe_allow_html=True)

    # image
    st.markdown(f"""
        <div class="inner text-center">
            <img src="data:image/jpg;base64,{image}" width="500" height="300" class="">
        </div>
        <a href="https://unsplash.com/photos/sMtKdbJfi_I"><p class="text-center">Image Source</p></a>""", unsafe_allow_html=True)
    #  End Image

    st.write("""
    In this project, we will develop and evaluate the performance and predictive power of a model that was trained and tested on data collected from suburban Boston homes. We use a random forest model

    Once we get a good fit, we'll use this model to predict the monetary value of a house located in the Boston area.

    A model like this will be invaluable for real state agents who can take advantage of the information provided on a daily basis.

    You can find the full project, documentation and dataset on my GitHub page:

    https://github.com/rromanss23/Machine_Leaning_Engineer_Udacity_NanoDegree/tree/master/projects/boston_housing
        """)  