import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Análisis de los anuncios de venta de coches')

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
scat_button = st.button('Construir gráfico de dispersión') # crear un botón 
bar_button = st.button('Construir gráfico de barra') # crear un botón


if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Frecuencia modelos de coches publicados')
            
    # crear un histograma
    fig = px.histogram(car_data, x="model")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


if scat_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Gráfico de dispersión según el tipo de combustible')
            
    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="model", y=["type", "transmission", "fuel"])
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if bar_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Precios según modelos de coche')
            

    # crear un gráfico de barra
    fig = px.bar(car_data, x=["model","model_year"], y="price")
        

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)