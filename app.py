import streamlit as st
import scipy.stats
import time

st.header('Lanzar una moneda')

# Inicializamos el gráfico con un valor base de 0.5
chart = st.line_chart([0.5])

# Función para emular lanzamientos y actualizar gráfico
def toss_coin(n): 
    # Genera n lanzamientos (0 o 1) con 50% de probabilidad
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)
    
    mean = None
    outcome_no = 0
    outcome_1_count = 0
    
    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        
        # Calcula el promedio acumulado hasta el momento
        mean = outcome_1_count / outcome_no
        
        # --- AQUÍ ESTÁ LA MAGIA ---
        # Añade la nueva media al gráfico
        chart.add_rows([mean])
        
        # Pausa pequeña para visualizar el efecto
        time.sleep(0.05)
        
    return mean

# --- Widgets ---
number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
start_button = st.button('Ejecutar')

# --- Lógica al presionar el botón ---
if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')
    toss_coin(number_of_trials)
    st.write('¡Experimento finalizado!')