import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("readmission_model.pkl","rb"))

st.title("Patient Readmission Risk Prediction")

st.write("Enter patient information to predict readmission risk.")

# Patient inputs
season = st.selectbox("Season", [0,1,2,3])
age = st.number_input("Age", 18,95)
gender = st.selectbox("Gender", [0,1])
region = st.selectbox("Region", [0,1,2,3,4])
primary_diagnosis = st.selectbox("Primary Diagnosis", list(range(11)))
comorbidities_count = st.slider("Comorbidities Count",0,10)
length_of_stay = st.slider("Length of Stay",1,30)
treatment_type = st.selectbox("Treatment Type",[0,1,2,3])
medications_count = st.slider("Medications Count",0,20)
followup_visits_last_year = st.slider("Followup Visits Last Year",0,20)
prev_readmissions = st.slider("Previous Readmissions",0,10)
insurance_type = st.selectbox("Insurance Type",[0,1,2,3])
discharge_disposition = st.selectbox("Discharge Disposition",[0,1,2,3])

# Prediction button
if st.button("Predict Readmission Risk"):

    input_data = np.array([[

        season,
        age,
        gender,
        region,
        primary_diagnosis,
        comorbidities_count,
        length_of_stay,
        treatment_type,
        medications_count,
        followup_visits_last_year,
        prev_readmissions,
        insurance_type,
        discharge_disposition

    ]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("High Risk of Readmission")
    else:
        st.success("Low Risk of Readmission")