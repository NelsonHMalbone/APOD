import config
import streamlit as st
import requests

st.title(' Astronomy Picture of the Day')

url = f'https://api.nasa.gov/planetary/apod?api_key={config.api_key}'
response = requests.get(url)
content = response.json()

st.write(f'Date: {content["title"]}')
st.write(f'Date: {content["date"]}')
