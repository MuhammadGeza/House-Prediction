import base64
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis

@st.cache()
def decode_img(dir_img):
    with open(dir_img, "rb") as image_file:
        byt = base64.b64encode(image_file.read())
    return byt.decode()

@st.cache(allow_output_mutation=True)
def load_df(dir):
    return pd.read_csv(dir)

@st.cache(allow_output_mutation=True)
def show_percentage_msvalue(df):
    return df.isna().mean().rename('Percentage')

@st.cache(allow_output_mutation=True)
def show_corr(df):
    return df.corr()

@st.cache(allow_output_mutation=True)
def describe_df(df):
    return df.describe()

def distplot(df):
    choice = st.selectbox('Select column', df.columns)
    # fig = ff.create_distplot(hist_data=[df[choice].values.tolist()], group_labels=[f'{choice}'])
    # st.plotly_chart(fig, use_container_width=True)
    fig = plt.figure(figsize=(10, 4))
    sns.distplot(df[choice])
    st.pyplot(fig)
    st.write(f"""
    * **Skewness** column {choice}: {skew(df[choice])}
    * **Kurtosis** column {choice}: {kurtosis(df[choice])}
    """)
