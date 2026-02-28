import streamlit as st
import random
import pandas as pd
import numpy as np

st.header('Lanzar una moneda: Simulador Avanzado')

# 1. Widget de entrada: Control deslizante
number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 100)

# 2. Widget de botón
start_button = st.button('Ejecutar experimento')

if start_button:
    st.write(f'Iniciando experimento con {number_of_trials} intentos...')
    
    # --- Lógica de negocio ---
    # Generar resultados (0 = Cara, 1 = Cruz)
    results = [random.choice([0, 1]) for _ in range(number_of_trials)]
    
    # Crear un DataFrame para los resultados
    df = pd.DataFrame(results, columns=['Resultado'])
    df['Intento'] = range(1, number_of_trials + 1)
    
    # Calcular promedio acumulado
    df['Promedio Acumulado'] = df['Resultado'].cumsum() / df['Intento']
    
    # --- Visualización ---
    
    # 3. Gráfico de líneas (Progreso)
    st.subheader('Progreso del experimento')
    st.line_chart(df['Promedio Acumulado'])
    
    # 4. Tabla de resultados (Dataframe)
    st.subheader('Tabla de resultados')
    st.write(df)

st.write('---')
st.write('Desarrollado con Streamlit.')