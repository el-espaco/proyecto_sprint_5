import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Vehicles Data')

search_button = st.button('Search')

if search_button:
    st.write("Creating Car Mileage Histogram")

    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)