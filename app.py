import streamlit as st
import pickle

kkn=pickle.load(open('knn.pkl', 'rb'))

st.title('Weather Prediction Model')

percep=st.number_input('Enter Precipitation:')
min_temp=st.number_input('Enter Minimum Temprature:')
max_temp=st.number_input('Enter Maximum Temprature:')
wind=st.number_input('Enter Wind Speed:')

prediction =kkn.predict([[percep, min_temp, max_temp, wind]])

if st.button('Prediction'):
    if (prediction[0] == 0):
        st.header("Drizzle")
    elif (prediction[0] == 1):
        st.header("Fog")
    elif (prediction[0] == 2):
        st.header("Rain")
    elif (prediction[0] == 3):
        st.header("snow")
    else:
        st.header("Sun")
