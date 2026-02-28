import pandas as pd
import scipy.stats
import streamlit as st
import time

# 1. Inicialización de la Memoria (Session State)
if 'experiment_no' not in st.session_state:
    st.session_state['experiment_no'] = 0

if 'df_experiment_results' not in st.session_state:
    st.session_state['df_experiment_results'] = pd.DataFrame(columns=['no', 'iteraciones', 'media'])

st.header('Lanzar una moneda')

# 2. Gráfico inicial
chart = st.line_chart([0.5])

# 3. Función de simulación
def toss_coin(n):
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)
    mean = 0
    outcome_no = 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])
        time.sleep(0.05)

    return mean

# 4. Interfaz de usuario
number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
start_button = st.button('Ejecutar')

if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')
    
    # Aumentar el contador de experimentos
    st.session_state['experiment_no'] += 1
    
    # Ejecutar simulación
    mean = toss_coin(number_of_trials)
    
    # Guardar resultados en el DataFrame de la sesión
    new_data = pd.DataFrame(data=[[st.session_state['experiment_no'],
                                   number_of_trials,
                                   mean]],
                            columns=['no', 'iteraciones', 'media'])
    
    st.session_state['df_experiment_results'] = pd.concat([
        st.session_state['df_experiment_results'],
        new_data
    ], axis=0).reset_index(drop=True)

# 5. Mostrar la tabla de historial siempre al final
st.write("### Historial de experimentos")
st.write(st.session_state['df_experiment_results'])