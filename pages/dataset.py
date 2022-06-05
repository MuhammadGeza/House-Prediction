import streamlit as st
from pages.other_function import *

def app(): 
    df = load_df("data/boston.csv")   

    st.write(f"""
    # About Dataset
    The number of rows in the dataset is {df.shape[0]} and the number of columns in the dataset is {df.shape[1]}""")

    st.write('### Display the first five data')
    st.write(df.head())

    _, _, col3, _, _= st.columns(5)
    with col3:
        checkbox = st.checkbox("Show More")

    if checkbox:
        st.write("### Descriptive Statistics")
        df_describe = describe_df(df)
        st.write(df_describe)

        st.write('### Correlation between each column')
        df_corr = show_corr(df)
        st.write(df_corr)

        col1, col2 = st.columns(2)
        with col1:
            st.write('### Unique number in each column')
            du = pd.DataFrame([df[i].nunique() for i in df.columns], index=df.columns, columns=['unique number'])
            st.write(du)
            
        with col2:
            st.write('### The percentage of missing values in the dataset')
            df_col2 = show_percentage_msvalue(df)
            st.write(df_col2)
            
        st.write("### View the distribution of data for each column")
        distplot(df)