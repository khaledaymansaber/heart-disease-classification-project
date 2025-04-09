import streamlit as st
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler  # Or your scaler of choice

# Load the trained model
model = joblib.load('model.pkl')


# Streamlit UI for input
st.title("Heart Disease Prediction")

# Accept input for each column in the dataset
bmi = st.number_input("BMI", min_value=12.9, max_value=43.1, value=25.0)
smoking = st.selectbox("Smoking (1 = Yes, 0 = No)", options=[1, 0])
alcohol_drinking = st.selectbox("Alcohol Drinking (1 = Yes, 0 = No)", options=[1, 0])
stroke = st.selectbox("Stroke (1 = Yes, 0 = No)", options=[1, 0])
physical_health = st.number_input("Physical Health (Days)", min_value=0, max_value=30, value=0)
mental_health = st.number_input("Mental Health (Days)", min_value=0, max_value=30, value=0)
diff_walking = st.selectbox("Difficulty Walking (1 = Yes, 0 = No)", options=[1, 0])
sex = st.selectbox("Sex (1 = Male, 0 = Female)", options=[1, 0])
age_category = st.selectbox("Age Category", options=[1, 2, 3, 4, 5])  # Adjust options based on actual categories
race = st.selectbox("Race (1, 2, 3, ...)", options=[1, 2, 3, 4])  # Adjust based on race categories
diabetic = st.selectbox("Diabetic (1 = Yes, 0 = No)", options=[1, 0])
physical_activity = st.selectbox("Physical Activity (1 = Yes, 0 = No)", options=[1, 0])
gen_health = st.selectbox("General Health (1 = Excellent, 5 = Poor)", options=[1, 2, 3, 4, 5])
sleep_time = st.number_input("Sleep Time (Hours)", min_value=3, max_value=11, value=7)
asthma = st.selectbox("Asthma (1 = Yes, 0 = No)", options=[1, 0])
kidney_disease = st.selectbox("Kidney Disease (1 = Yes, 0 = No)", options=[1, 0])
skin_cancer = st.selectbox("Skin Cancer (1 = Yes, 0 = No)", options=[1, 0])
# Prepare the input features for prediction
features = np.array([[bmi, smoking, alcohol_drinking, stroke, physical_health, mental_health, 
                      diff_walking, sex, age_category, race, diabetic, physical_activity, 
                      gen_health, sleep_time, asthma, kidney_disease, skin_cancer]])


# Prediction
if st.button("Predict"):
    prediction = model.predict(features)
    if prediction[0] == 1:
        st.write("Prediction: Heart Disease")
    else:
        st.write("Prediction: No Heart Disease")
