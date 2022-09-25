import streamlit as st
import pandas as pd
import joblib

# Title
st.header("Predictor de Diabetes")

# Input bar 1
#Genero = st.number_input("Género")
Genero = st.radio('1. Seleccione su género', ['Femenino', 'Masculino'])


# Input bar 2
#weight = st.number_input("Ingrese su peso")
R_Edad = st.slider('2. Seleccione su edad', 0, 100)


# Input bar 3
Estatura = st.slider('3. Seleccione su estatura', 0.0, 2.3)


# Input bar 4
Peso = st.slider('4. Seleccione su peso', 0.0, 150.0)


# Input bar 5
Sistolica = st.slider('5. Ingrese su presión "Sistólica"', 0.0, 500.0)


# Input bar 6
Diastolica = st.slider('6. Ingrese su presión "Diastólica"', 0.0, 100.0)


# Input bar 7
Obesidad_ = st.radio('7. ¿Algún médico le ha diagnosticado obesidad?', ['Sí', 'No'])



# Input bar 8
Antecedentes_de_Diabetes = st.radio('8. ¿Alguno de sus familiares ha sido diagnosticado con diabetes?', ['Sí', 'No'])


# Input bar 9
Nivel_de_Glucosa = st.slider('9. Ingrese su Nivel de Glucosa', 0.0, 1000.0)


# Dropdown input
eyes = st.selectbox("Seleccione el color de los ojos", ("Blue", "Brown"))

# If button is pressed
if st.button("Submit"):
    
    # Unpickle classifier
    clf = joblib.load("clf.pkl")
    
    # Store inputs into dataframe
    X = pd.DataFrame([[Genero, R_Edad, Estatura, Peso, Sistolica, Diastolica, Obesidad_, Antecedentes_de_Diabetes,
                    Nivel_de_Glucosa, eyes]], 
                     columns = ["Género", "R_Edad", "Estatura", "Peso", "Sistólica", "Diastolica",
                     "Obesidad_", "Antecedentes de Diabetes", "Nivel de Glucosa", "Eyes"])
    
    X = X.replace(["Brown", "Blue"], [1, 0])
    
    # Get prediction
    prediction = clf.predict(X)[0]
    
    # Output prediction
    st.text(f"This instance is a {prediction}")