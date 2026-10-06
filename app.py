import streamlit as st
import joblib


# Load the trained machine learning model
model = joblib.load("model/salary_prediction_model.pkl")


# Title of the app
st.title("💼 Salary Prediction App")


# Description
st.write(
    "Enter your years of experience to predict your salary."
)


# Take input from the user
experience = st.number_input(
    "Years of Experience",
    min_value=0.0,
    max_value=50.0,
    value=1.0,
    step=0.1
)


# Create prediction button
if st.button("Predict Salary"):

    # Make prediction using our trained model
    prediction = model.predict([[experience]])

    # Display prediction
    st.success(
        f"Predicted Salary: ${prediction[0]:,.2f}"
    )