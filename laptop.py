
import streamlit as st
import pickle
import numpy as np

df= pickle.load(open('df.pkl','rb'))
pipe= pickle.load(open('pipe.pkl','rb'))

st.title("Prediction model for Laptop Price")

company = st.selectbox("Brand",df['Company'].unique(),index = 3)
type = st.selectbox("Type of Laptop",df['TypeName'].unique(),index = 1)
cpu = st.selectbox("Cpu Name",df['Cpu'].unique(), index=0)
ram = st.selectbox("RAM",np.array([2,4,6,8,12,16,24,32,64,128]),index = 3)
memory =  st.selectbox("Memory Storage",df['Memory'].unique(),index = 4)
hdd = st.selectbox("HDD Storage",np.array([0,128,500,1000,2000]), index = 2)
ssd= st.selectbox("SSD Storage",np.array([0,8,16,32,64,128,180,240,256,512,768,1000,1024]),index = 9)
hybrid = st.selectbox("Hybrid",np.array([0,508,1000]),index = 2)
flash_storage =  st.selectbox("Flash Storage",np.array([0,16,32,64,128,256,512]),index = 5)
gpu =  st.selectbox("GPU",df['Gpu'].unique(),index = 0)
opsys = st.selectbox("Operating System",df['OpSys'].unique(),index = 1)
weight = st.number_input("weight of the laptop(in kg)",min_value=0.6,max_value= 4.7,value=2.0 ,step =0.1 )
