# importing the libraries 
import pandas as pd
import joblib
import streamlit as st
import numpy as np

# Load the trained model
model = joblib.load("model.pkl")

# stream lit logic is using st. 
st.title("")
st.write("")


# Input fields  #define the values as of self according to the data


 



 #define the values as of self according to the data syntax
column_name = st.number_input("column_name (hPa)", min_value='', max_value='', value='')
column_name = st.number_input("column_name (hPa)", min_value='', max_value='', value='')
column_name = st.number_input("column_name (hPa)", min_value='', max_value='', value='')
column_name = st.number_input("column_name (hPa)", min_value='', max_value='', value='')
column_name = st.number_input("column_name (hPa)", min_value='', max_value='', value='')
column_name = st.number_input("column_name (hPa)", min_value='', max_value='', value='')
column_name = st.number_input("column_name (hPa)", min_value='', max_value='', value='')


# Input fields examples
pressure = st.number_input("Pressure (hPa)", min_value=800.0, max_value=1100.0, value=1013.0)
dewpoint = st.number_input("Dew Point (°C)", min_value=-20.0, max_value=40.0, value=12.0)
humidity = st.slider("Humidity (%)", 0, 100, 70)
cloud = st.slider("Cloud Cover (%)", 0, 100, 50)
sunshine = st.number_input("Sunshine (hours)", min_value=0.0, max_value=12.0, value=6.0)
winddirection = st.slider("Wind Direction (°)", 0, 360, 180)
windspeed = st.number_input("Wind Speed (km/h)", min_value=0.0, max_value=100.0, value=10.0)



    