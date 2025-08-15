import joblib 
import streamlit as st

model = joblib.load("knn_model")

st.header("IBM Classification based on Weight and Height")
st.subheader("This ML Model is Accomplished using Knn Classifier Algorighm")

Weight =st.number_input("Enter the weight (in kg)",min_value=45,max_value=95,value=65,step=1) 
Height =st.number_input("Enter the Height (in cm)",min_value=140,max_value=175,value=160,step=1)

if st.button("PREDICT"):
    op=model.predict([[Weight,Height]])
    st.subheader(f"The person having weight as {Weight} and height as {Height} is catagorized as  {op[0]}")
