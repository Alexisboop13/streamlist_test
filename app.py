import streamlit as st
import random

st.header('Lanzar una moneda')

# Botón para lanzar la moneda
if st.button('Lanzar moneda'):
    resultado = random.choice(['Cara', 'Cruz'])
    st.write(f'Resultado: **{resultado}**')