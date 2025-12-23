import streamlit as st #to create web app
import pandas as pd #to handle dataframes
import requests #to make api calls

st.title("Tip Prediction App")
st.write("Please enter details to get  the tip amount")

#imput data

total_bill = st.number_input("Total Bill Amount",min_value=0.0)
sex = st.selectbox("Sex",options=['Male','Female'])
smoker = st.selectbox("Smoker",options=['Yes','No'])
day = st.selectbox("day",options=['Thur','Fri','Sat','Sun'])
time = st.selectbox("time",options=['Lunch','Dinner'])
size = st.number_input("Size of party",min_value=1,max_value=10)

if st.button("Predict"):
    #prepare the data to  send to the abckend
    input_data = {
        'total_bill' : total_bill,
        'sex' : sex,
        'smoker' : smoker,
        'day' : day,
        'time' : time,
        'size' : size
    }

    response = requests.post("http://127.0.0.1:5000/predict", json = input_data) #make the api
    if response.status_code == 200:
        prediction = response.json().get('predicted_tip') #get the predicted tip amount 
        st.write('The tip value is:',prediction)#display the predicted amount
    else:
        st.write("Error in prediction")


