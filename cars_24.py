import streamlit as st
import pandas as pd
import pickle



st.title("Car Price Prediction App")

# I want to take 4 inputs from the user
# Fuel type, Transmission type, engine power, seats


col1, col2 = st.columns(2)

with col1: 
    # use radio for fuel_type
    fuel_type = st.radio("Fuel Type", ["Petrol", "Diesel", "CNG", "Electric"])

with col2: 
    transmission_type = st.selectbox("Transmission Type", ["Manual", "Automatic"])


col3, col4 = st.columns(2)

with col3:
    engine_power = st.slider("Engine Power", 500, 5000, step=100)

with col4:
    seats = st.selectbox("Seats", [2, 4, 5, 6, 7, 8, 9, 10])