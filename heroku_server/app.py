import streamlit as st
import streamlit.components.v1 as components
from project_zero.processing import calc_sum
import numpy as np
import requests

#Documentation 

fontc='Roboto'

hvar= """   <script>
                var elements = window.parent.document.querySelectorAll('.streamlit-sliderLabel');
                elements[0].style.fontWeight = 'bold';
                elements[0].style.fontFamily = 'Didot';
                elements[0].style.fontSize = 'x-large';
            </script>"""

components.html(hvar, height=0, width=0)

st.sidebar.markdown(f"<h1 style='text-align: center; color: black; font: fontc'> Choose Your Galaxies</h1>", unsafe_allow_html=True)

st.sidebar.markdown(f"<h2 style='text-align: left; color: black; font: fontc'> Option 1</h2>", unsafe_allow_html=True)
opt = st.sidebar.selectbox('Answer',('options_1','options_2'),format_func=lambda x: x.replace('-',' ').capitalize())
d = st.sidebar.slider(label='Posterior Mean',value=[.0, 1.])
e = st.sidebar.slider('How old are you?', 0, 130, 25)

st.sidebar.markdown(f"<h2 style='text-align: left; color: black; font: fontc'> Option 2</h2>", unsafe_allow_html=True)
a = st.sidebar.number_input('number a', min_value=None, max_value=None, value=0.0, step=None,format=None)
b = st.sidebar.number_input('number b', min_value=None, max_value=None, value=0.0, step=None,format=None)

#Main title
st.markdown(f"<h1 style='text-align: center; color: black; font: Roboto'> Test API</h1>", unsafe_allow_html=True)

st.write('')
st.write('')
st.write('')
st.write('')
st.write('')

c = calc_sum(a,b)

#Display the error
st.markdown(f"<h4 style='text-align: center; color: green; font: Roboto'> a + b = {round(c,2)} </h4>", unsafe_allow_html=True)
st.markdown(f"<h4 style='text-align: center; color: green; font: Roboto'> d1= {d[0]}, d2= {d[1]} </h4>", unsafe_allow_html=True)
st.markdown(f"<h4 style='text-align: center; color: green; font: Roboto'> e = {round(e,2)} </h4>", unsafe_allow_html=True)
st.markdown(f"<h4 style='text-align: center; color: green; font: Roboto'> opt = {opt}, type={type(opt)} </h4>", unsafe_allow_html=True)

word1 = st.text_input('word1', 'xxx')
word2 = st.text_input('word2', 'xxx')

url = f'https://project-zero-service-cis7jmkfja-ew.a.run.app/send?word1={word1}&word2={word2}'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    st.markdown(f"<h4 style='text-align: center; color: green; font: Roboto'> data = {data} </h4>", unsafe_allow_html=True)