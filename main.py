from config import api_key
import streamlit as st
import requests

# title of webiste
st.title(' Astronomy Picture of the Day')

# requesting the website
url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'
response = requests.get(url)
content = response.json()

# streamlit website functions

st.header(f'{content["title"]}')


# setting up a way to center the date

st.image(f'{content["url"]}', caption=f"{content['date']}", width=400)


st.write(f'Explanation: {content["explanation"]}')
