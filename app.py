import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Datos de kilometraje de vehiculos')

# search_button = st.button('Histogram')

# if search_button:
#     st.write("Creating Car Mileage Histogram")

#     fig = px.histogram(car_data, x='odometer')
#     st.plotly_chart(fig, use_container_width=True)

# scatter_button = st.button('Scattered Data')

# if scatter_button:
#     st.write("Creating Car Mileage Scattered Diagram")

#     fig = px.scatter(car_data, x="odometer", y="price")
#     st.plotly_chart(fig)

build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un diagrama de dispersión')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)
elif build_scatter:
    st.write('Construir un diagrama de dispersión de precios y kilometraje')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig)