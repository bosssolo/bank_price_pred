import streamlit as st 
import joblib 
import pandas as pd 
import numpy as np 

gend_map = {'Female': 0, 'Male': 1}
mar_map = {'No': 0, 'Yes': 1}
edu_map =  {'Graduate': 0, 'Not Graduate': 1}
aply_map = {'No': 0, 'Yes': 1}
prop_map = {'Rural': 0, 'Semiurban': 1, 'Urban': 2}
label = {'No': 0, 'Yes': 1}


model = joblib.load('Model.pkl')



# Page config
st.set_page_config(page_title="Dark Style", layout="centered")

# Actual CSS injection
st.markdown("""
    <style>
        body {
            background-color: #000000;
            color: black;
        }
        h1 {
            color: #00FFAA;
            text-shadow: 2px 2px 5px #00ffaa88;
        }
        .big-text {
            font-size: 20px;
            color: #FFD700;
        }
    </style>
""", unsafe_allow_html=True)

# This works 👇

# st.markdown("<h1>  Bank Loan Origination Predication Model  </h1>", unsafe_allow_html=True)
st.markdown(
    """
    <p style="
        font-size: 40px;
        font-weight: bold;
        color: #000000;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        margin-bottom: 20px;
        text-align: left;">
        Bank Loan Origination Prediction Model
    </p>
    """,
    unsafe_allow_html=True
)
st.markdown('<p style = "color:#e44040;" class="big-text">Please Complete Underwriting Process Of Lender </p>', unsafe_allow_html=True)






gender_list = list(set(gend_map.keys()))
married_list = list(set(mar_map.keys()))
education_list = list(set(edu_map.keys()))
appl_list = list(set(aply_map.keys() ))
prop_list = list(set(prop_map.keys()))










gender =  st.selectbox("Select Gender",gender_list)
married = st.selectbox("Please Put Married Status Yes or No",married_list)
dependent = st.number_input("How Much Number of Dependence you have please put in ",min_value=0)
edu =  st.selectbox("Select Education ",education_list)
self_em = st.selectbox("Are You Self Employed Or Working Please tell Answer in Yes or Not",appl_list)
appl_ln = st.number_input("Please give the Applicant Income Details ",min_value=0)
coappl_ln = st.number_input("Please give the Co-Applicant Income Details as Nomenie",min_value=0)
loanamt = st.number_input("Please put Loan Amount ",min_value=0)
loanamtterm = st.number_input("Please enter Your Loan Term Amount",min_value=0)

property = st.selectbox("Please Select Property Area",prop_list)


if st.button("Predict"):
     us_gen = gend_map[gender]
     us_mar = mar_map[married]
     
     us_ed = edu_map[edu]
     us_self = aply_map[self_em]
     us_prop = prop_map[property]

     features = np.array([[us_gen,us_mar,dependent,us_ed,us_self,appl_ln,coappl_ln,loanamt,loanamtterm,us_prop]])

     predictions = model.predict(features)[0]
     pred_string = list(label.keys())[list(label.values()).index(predictions)]

     # Display the Prediction 
     st.success(f"Prediction of Loan Status: {pred_string}")

     