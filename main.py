import config
import streamlit as st
import requests

# title of webiste
st.title(' Astronomy Picture of the Day')

# requesting the website
url = f'https://api.nasa.gov/planetary/apod?api_key={config.api_key}'
response = requests.get(url)
content = response.json()

# streamlit website functions
col1,col2,col3 = st.columns(3)
st.header(f'{content["title"]}')

# setting up a way to center the date
with col1:
    st.write("")
with col2:
    st.write(f'Date: {content["date"]}')
with col3:
    st.write("")

st.image(f'{content["url"]}')
st.write(f'Explanation: {content["explanation"]}')
