import pandas as pd
import plotly.express as px
import streamlit as st

# Header(Title) of the app
st.header("Car Sales Advertisements")

# Load the data from the CSV file - Advertisements
car_data = pd.read_csv('vehicles_us.csv')

# Checkboxes to toggle histogram and scatter plot
show_histogram = st.checkbox("Show Histogram")
show_scatter = st.checkbox("Show Scatter Plot")

# If the histogram checkbox is checked
if show_histogram:
    st.write(
        "Creación de un histograma para el conjunto de datos de anuncios de venta de coches")

    # Create and display histogram
    fig_histogram = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_histogram, use_container_width=True)

# If the scatter plot checkbox is checked
if show_scatter:
    st.write(
        "Creación de un gráfico de dispersión distancia recorrida vs precio de los coches")

    # Create and display scatter plot
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)
