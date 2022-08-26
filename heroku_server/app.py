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

a=4
b=5

c = calc_sum(a,b)

#Display the error
st.markdown(f"<h4 style='text-align: center; color: green; font: Roboto'> a + b = {round(c,2)} </h4>", unsafe_allow_html=True)