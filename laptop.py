
import streamlit as st
import pickle
import numpy as np
import pandas as pd

df= pickle.load(open('df.pkl','rb'))
pipe= pickle.load(open('pipe.pkl','rb'))

st.title("Prediction model for Laptop Price")

company = st.selectbox("Brand",df['Company'].unique(),index = 3)
type = st.selectbox("Type of Laptop",df['TypeName'].unique(),index = 1)
cpu = st.selectbox("Cpu Name",df['Cpu'].unique(), index=0)
ram = st.selectbox("RAM",np.array([2,4,6,8,12,16,24,32,64,128]),index = 3)
hdd = st.selectbox("HDD Storage",np.array([0,128,500,1000,2000]), index = 2)
ssd= st.selectbox("SSD Storage",np.array([0,8,16,32,64,128,180,240,256,512,768,1000,1024]),index = 9)
hybrid = st.selectbox("Hybrid",np.array([0,508,1000]),index = 2)
flash_storage =  st.selectbox("Flash Storage",np.array([0,16,32,64,128,256,512]),index = 5)
gpu =  st.selectbox("GPU",df['Gpu'].unique(),index = 0)
opsys = st.selectbox("Operating System",df['OpSys'].unique(),index = 1)
weight = st.number_input("weight of the laptop(in kg)",min_value=0.6,max_value= 4.7,value=2.0 ,step =0.1 )
touchscreen = st.selectbox("Touchscreen",["Yes","No"],index = 0)
ips = st.selectbox("IPS",["Yes","No"],index = 0)
screen_size = st.number_input("Screen Size(in Inches, calculated diagonally)",min_value = 10.0,max_value=18.5,step= 0.1,value = 15.6)
screen_resolution = st.selectbox("Screen Resolution",["2560x1600","1440x900","1920x1080","2880x1800",
"1366x768","2304x1440","3200x1800","1920x1200","2256x1504","3840x2160","2160x1440","2560x1440",
"1600x900","2736x1824","2400x1600"],index =2)

if st.button("PREDICT PRICE"):
    # Convert Yes/No to binary
    touchscreen = 1 if touchscreen == "Yes" else 0
    ips = 1 if ips == "Yes" else 0

    # Calculate PPI
    X_res = int(screen_resolution.split('x')[0])
    Y_res = int(screen_resolution.split('x')[1])
    PPI = ((X_res**2) + (Y_res**2))**0.5 / screen_size

    # Build query as DataFrame with SAME column names as training data
    query_df = pd.DataFrame([[company, type, cpu, ram, hdd, ssd, hybrid, 
                              flash_storage, gpu, opsys, weight, touchscreen, ips, PPI]],
                            columns=['Company','TypeName','Cpu','Ram','Memory','HDD',
                                     'SSD','Hybrid','Flash_Storage','Gpu','OpSys',
                                     'Weight','Touchscreen','IPS','PPI'])

    # Predict
    op = np.exp(pipe.predict(query_df))
    st.subheader(f"The Predicted Price of the Laptop with above configuration is ₹{str(round(op[0]))}")
