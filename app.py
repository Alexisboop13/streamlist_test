import scipy.stats
import streamlit as st
import time

st.header('Lanzar una moneda')

# Inicializamos el gráfico con un valor base de 0.5
chart = st.line_chart([0.5])

# Función que emula el lanzamiento de una moneda n veces
def toss_coin(n):
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)
    
    mean = None
    outcome_no = 0
    outcome_1_count = 0
    
    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        
        # Calcula la media acumulada
        mean = outcome_1_count / outcome_no
        
        # Añade la nueva media al gráfico en tiempo real
        chart.add_rows([mean])
        
        # Pausa para visualizar el progreso (0.05 segundos)
        time.sleep(0.05)
        
    return mean

# Widgets de entrada
number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
start_button = st.button('Ejecutar')

# Lógica al pulsar el botón
if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')
    # Llamamos a la función y guardamos el resultado final
    mean = toss_coin(number_of_trials) 
    st.write(f'La media final es: {mean}')