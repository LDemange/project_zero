import streamlit as st
from project_zero.processing import calc_sum

#Documentation 

#Main title
st.markdown(f"<h1 style='text-align: center; color: black; font: Roboto'> Test API</h1>", unsafe_allow_html=True)

st.write('')
st.write('')
st.write('')
st.write('')
st.write('')

#a = st.number_input('number a', min_value=None, max_value=None, value=0.0, step=None,
#                format=None)
b = st.number_input('number b', min_value=None, max_value=None, value=0.0, step=None,
                format=None)

col1, col2= st.columns(2)

with col1:
    st.header('a =')

with col2:
    a = st.number_input(min_value=None, max_value=None, value=0.0, step=None,
                format=None)

c = calc_sum(a,b)

#Display the error
st.markdown(f"<h4 style='text-align: center; color: green; font: Roboto'> a + b = {round(c,2)} </h4>", unsafe_allow_html=True)