# JRPMHS_SP7_P
Jorge Ponce-Sprint 7 Data Scientist-Project

# Name of the APP in RENDER
JRPMHS_SP7_P
# URL Render application
https://jrpmhs-sp7-p.onrender.com



# Car Sales Advertisements App

## Overview
This Streamlit web application provides interactive visualizations of a dataset containing car sales advertisements. Users can explore the data through:
- A **Histogram** showing the distribution of odometer readings.
- A **Scatter Plot** comparing odometer readings and car prices.

## File Structure

### 1. `requirements.txt`
Contains the list of required libraries for the application. This file is used by Render to install dependencies before deploying the app.
```
pandas
streamlit
plotly-express
```

### 2. `vehicles_us.csv`
A dataset containing car sales advertisement data, imported into a DataFrame for visualization.

### 3. `.streamlit/config.toml`
Configuration file for Streamlit, ensuring the app runs properly in a cloud environment.
```
[server]
headless = true
port = 10000

[browser]
serverAddress = "0.0.0.0"
serverPort = 10000
```

### 4. `app.py`
The main script of the application. It provides:

- **Two Checkboxes:**
  - **Show Histogram**: Displays a histogram of odometer readings.
  - **Show Scatter Plot**: Displays a scatter plot comparing odometer readings with car prices.

## How to Run Locally
1. **Clone the repository:**
   ```sh
   git clone https://github.com/JorgeRPMHS/JRPMHS_SP7_P.git
   cd car-sales-app
   ```

## Deployment on Render
- Ensure that `requirements.txt` and `.streamlit/config.toml` are correctly configured.
- Deploy the repository on **Render** and configure the **Build Command** as:
  ```sh
  pip install --upgrade pip && pip install -r requirements.txt
  ```
- **Start Command** as:
  ```sh
  streamlit run app.py
  ```

## Author
Jorge Roberto Ponce Martínez - [GitHub](https://github.com/JorgeRPMHS)

