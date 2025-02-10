import pandas as pd
import plotly.express as px
import streamlit as st

# Header(Title) of the app
st.header("Car Sales Advertisements")

# Load the data from the CSV file-Advertasements
car_data = pd.read_csv('vehicles_us.csv')

# Button to show the data (As an Histogram)
hist_button = st.button('Build an Histogram')

# If the button 'hist_button' is clicked
if hist_button:
    # Write a text explaining what the histogram is about
    st.write(
        "Creación de un histograma para el conjunto de datos de anuncios de venta de coches")

    # Create a histogram
    fig_histogram = px.histogram(car_data, x="odometer")

    # Show the interactive plot histogram
    st.plotly_chart(fig_histogram, use_container_width=True)


# Button to show the data (In a Scatter Plot)
scatter_button = st.button('Build a Scatter Plot')

# If the button 'scatter_button' is clicked
if scatter_button:
    # Write a text explaining what the scatter plot is about
    st.write(
        "Creación de un gráfico de dispersión distancia recorrida vs precio de los coches")

    # Create a scatter plot
    fig_scatter = px.scatter(car_data, x="odometer", y="price")

    # Show the interactive plot scatter
    st.plotly_chart(fig_scatter, use_container_width=True)
