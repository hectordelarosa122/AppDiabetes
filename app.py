import streamlit as st
import pandas as pd
import joblib

# Title
st.header("Predictor de Diabetes")

# Input bar 1
height = st.number_input("Ingrese su altura")

# Input bar 2
weight = st.number_input("Ingrese su peso")

# Dropdown input
eyes = st.selectbox("Seleccione el color de los ojos", ("Blue", "Brown"))

# If button is pressed
if st.button("Submit"):
    
    # Unpickle classifier
    clf = joblib.load("clf.pkl")
    
    # Store inputs into dataframe
    X = pd.DataFrame([[height, weight, eyes]], 
                     columns = ["Height", "Weight", "Eyes"])
    X = X.replace(["Brown", "Blue"], [1, 0])
    
    # Get prediction
    prediction = clf.predict(X)[0]
    
    # Output prediction
    st.text(f"This instance is a {prediction}")