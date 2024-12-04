import streamlit as st
import pandas as pd
import pickle
from datetime import datetime
import joblib

#Loading my pre-trained linear regression model which was saved earlier
model = joblib.load('lr_nurse_pay.pkl')

# Streamlit App
st.title("Nurse' Hourly Pay Rate Prediction in the US")
st.header("Enter Details to Get Hourly Pay Rate Prediction")

# Input fields
# Inputs for the user to query the data
job_title = st.selectbox("Select Job Title",
                         ['RegisteredNurse_ICU', 'RegisteredNurse_MedSurg', 'RegisteredNurse_Telemetry',
                          'RegisteredNurse_Oncology', 'RegisteredNurse_Pediatric', 'PhysioTherapist',
                          'LabTechnician', 'RegisteredNurse_CriticalCare', 'RegisteredNurse_Cardiology',
                          'RegisteredNurse_Surgery'])

location = st.selectbox("Select Location",
                        ['Dallas, TX', 'Atlanta, GA', 'New York, NY', 'Philadelphia, PA', 'Washington, DC',
                         'San Francisco, CA', 'Los Angeles, CA', 'Seattle, WA', 'Chicago, IL',
                         'San Diego, CA', 'Miami, FL', 'Boston, MA', 'Detroit, MI', 'Phoenix, AZ', 'Houston, TX'])

hospital_name = st.selectbox("Select Hospital Name",['Chicago Govt', 'San Francisco Corporate', 'Dallas Corporate',
       'Chicago NonProfit', 'Chicago Veterans', 'Houston Veterans',
       'Phoenix Community', 'New York Veterans', 'Detroit Community',
       'Miami Community', 'San Francisco Govt', 'Los Angeles Corporate',
       'San Francisco Veterans', 'Phoenix Veterans', 'Miami NonProfit',
       'San Diego Community', 'Los Angeles Govt', 'Houston Govt',
       'Boston Govt', 'Washington Community', 'San Diego NonProfit',
       'Atlanta Veterans', 'Los Angeles Veterans', 'Boston NonProfit',
       'Washington Corporate', 'New York NonProfit', 'Detroit Corporate',
       'San Diego Corporate', 'Phoenix Corporate', 'Houston Corporate',
       'Miami Veterans', 'Boston Community', 'Seattle Community',
       'Philadelphia NonProfit', 'Detroit Govt', 'Atlanta Govt',
       'New York Corporate', 'Houston NonProfit', 'Dallas Govt',
       'Miami Corporate', 'Philadelphia Veterans', 'Washington Veterans',
       'Dallas NonProfit', 'Detroit NonProfit', 'Dallas Community',
       'Dallas Veterans', 'San Francisco Community', 'Seattle Govt',
       'Los Angeles Community', 'Seattle NonProfit',
       'Philadelphia Community', 'San Diego Veterans',
       'Atlanta NonProfit', 'New York Community', 'Boston Corporate',
       'Seattle Veterans', 'Chicago Community', 'Atlanta Community',
       'New York Govt', 'Miami Govt', 'San Francisco NonProfit',
       'Philadelphia Corporate', 'San Diego Govt', 'Washington NonProfit',
       'Philadelphia Govt', 'Chicago Corporate', 'Atlanta Corporate',
       'Phoenix Govt', 'Washington Govt', 'Houston Community',
       'Boston Veterans', 'Seattle Corporate', 'Los Angeles NonProfit',
       'Detroit Veterans', 'Phoenix NonProfit'])
contract_start_date = st.date_input("Contract Start Date")
contract_end_date = st.date_input("Contract End Date")

# Predict button
if st.button("Predict Hourly Pay Rate"):
    # Preprocess input: extract month and day
    start_month = pd.to_datetime(contract_start_date).month
    end_month = pd.to_datetime(contract_end_date).month
    start_date=pd.to_datetime(contract_start_date).day
    end_date=pd.to_datetime(contract_end_date).day

    
    # Create a DataFrame with the necessary format
    input_data = pd.DataFrame({
        'Job Title': [job_title],
        'Location': [location],
        'Hospital Name': [hospital_name],
        'StartMonth': [start_month],
        'EndMonth': [end_month],
	'StartDate': [start_date],
        'EndDate': [end_date]
    })
    
    # Make a prediction using the pre-trained pipeline
    prediction = model.predict(input_data)[0]
    
    # Display result
    st.write(f"Predicted Hourly Pay Rate: ${prediction:.2f}")
