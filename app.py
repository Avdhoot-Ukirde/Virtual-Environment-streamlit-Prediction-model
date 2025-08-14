
import streamlit as st
import joblib

# Title and description
st.header("This is a Salary Prediction Model Based on Years of Experience")
st.caption("This ML model was designed with a sample dataset obtained from Kaggle. Linear Regression was the algorithm used to make the model.")

# Load saved model
model = joblib.load('lr_model')  # Make sure you saved it earlier using joblib.dump(model, 'lr_model.pkl')

# User input
years = st.slider("Enter the number of years of experience", min_value=0.0, max_value=20.0, value=5.0, step=0.1)

# Prediction
if st.button("PREDICT"):
    op = model.predict([[years]])  # Predict using model
    st.header(f"The estimated salary for a person with {years} years of experience is ₹ {round(op[0], 2)}")
