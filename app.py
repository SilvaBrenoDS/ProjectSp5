import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv("vehicles.csv")

st.header("Análise de anúncios de veículos nos EUA")

hist_button = st.button("Criar histograma")

if hist_button:
    st.write("Criando um histograma para a coluna odometer.")
    fig = px.histogram(
        car_data,
        x="odometer",
        title="Distribuição da quilometragem dos veículos"
    )
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button("Criar gráfico de dispersão")

if scatter_button:
    st.write("Criando um gráfico de dispersão entre preço e quilometragem.")
    fig = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Relação entre quilometragem e preço"
    )
    st.plotly_chart(fig, use_container_width=True)