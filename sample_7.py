import streamlit as st
import joblib
import numpy as np

st.title("Obesity Classification")
col1,col2=st.columns(2)

with col1:
    Age=st.text_input("Enter your age:")
    Gender=st.text_input("Enter your gender Male:1,Female:0")
    Height=st.text_input("Enter your height:")
    Weight=st.text_input("Enter your weight:")
    BMI=st.text_input("Enter your BMI:")

    model=joblib.load("obes_99.pkl")

    if st.button("prediction"):
        data=[[Age,Gender,Height,Weight,BMI]]
        data_array=np.array(data).reshape(1,-1)
        pred=model.predict(data_array)
        if pred==0:
            st.write("Normal weight")
        elif pred==1:
            st.write("obese")
        elif pred==2:
            st.write("Over weight")
        elif pred==3:
            st.write("Under Weight")
with col2:
    st.image("F:\obesity.png")
