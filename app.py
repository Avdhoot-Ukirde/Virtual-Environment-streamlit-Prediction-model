st.title("This a Salary Prediction Model Based on Years of Experience")
st.caption("This ML model was desighned with a sample data obtained from kaggle. Linear Regression was the algorith used to make the model")
st.model.jobilb.load('lr_model')
years = st.slider("Enter the number of years of Experience", min_value=0.0,max_value=20,value=5,step=0.1)

