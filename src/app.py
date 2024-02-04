# Importar las librerias 
import streamlit as st
import pandas as pd
import joblib

# Cargar el modelo preentrenado
clf = joblib.load("model/laptop_model.pkl")

# Añadir un título
st.title("Estimate Laptop")

# Añadir una imágen
st.image('comment-choisir-un-ordinateur-portable.webp')

# Sección para seleccionar la cantidad de RAM
ram_gb = st.selectbox(
    'Select RAM Size (GB)',
    ('4 GB', '8 GB', '16 GB', '32 GB')
)

# Sección para seleccionar el sistema operativo
os = st.selectbox(
    'Select Operating System',
    ('Windows', 'DOS', 'Mac')
)

# Sección para seleccionar la arquitectura de bits
os_bit = st.selectbox(
    'Select Bits',
    ('64-bit', '32-bit')
)

# Línea divisoria para mejorar la presentación
st.divider()

# Botón para realizar la estimación cuando se hace clic
if st.button("Find out"):
    # Crear un DataFrame con las selecciones del usuario
    X = pd.DataFrame([[ram_gb, os, os_bit]],
                             columns=['RAM Size (GB)', 'Operating System', 'Bits'])
    
    # Renombrar columnas para mayor claridad
    X = X.rename(columns={'RAM Size (GB)': 'ram_gb', 'Operating System': 'os', 'Bits': 'os_bit'})
    X = X[['ram_gb', 'os', 'os_bit']]

    # Convertir variables categóricas a valores numéricos si es necesario
    X = X.replace(['Windows','DOS', 'Mac', '4 GB', '8 GB', '16 GB', '32 GB', '64-bit', '32-bit'],[1, 2, 3, 4, 8, 16, 32, 64, 32])

    # Realizar predicciones utilizando el modelo cargado
    prediction = clf.predict(X)[0]

    # Mostrar el resultado al usuario
    st.text(f"This instance is a {prediction}")