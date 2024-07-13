import streamlit as st
import pandas as pd
import plotly_express as px

st.set_page_config(page_title="Excel Plotter")
st.title('Excel Plotter 📈')
st.subheader('Feed me with your Excel file')

# Uploade excel file
uploaded_file = st.file_uploader('Choose a XLSX file', type='xlsx')
# Check to see if xlsx file has been uploaded
if uploaded_file:
    st.markdown('---')
    df = pd.read_excel(uploaded_file, engine='openpyxl')
    st.dataframe(df)
    groupby_column = st.selectbox(
        'WHat would you like to analyse?',
        ('Ship Mode', 'Segment', )
    )