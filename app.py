import streamlit as st
import pickle 
import pandas as pd
import numpy as np


model = pickle.load(open('Log_reg_loan_status.pkl','rb'))  # rb = read binary
st.title('Loan Status Prediction Web App')
st.header('Fill the details to generate Loan Status')

col1, col2 =  st.columns(2)

with col1:
    dependents = st.slider('Dependents',min_value=0,max_value=3)
    app_income = st.number_input('Applicant Income',min_value=1000,max_value=34000)
    co_app_income = st.number_input('Co-Applicant Income',min_value=0,max_value=9000)
    loan_amount = st.number_input('Loan Amount',min_value=30,max_value=500)
    loan_amount_term = st.selectbox('Loan Amount Term',[84,120,180,240,300,360,480])
    credit_hist = st.selectbox('Credit History',[0,1])

with col2:
    gender = st.selectbox('Gender',['Male','Female'])
    married = st.selectbox('Married',['Yes','No'])
    education = st.selectbox('Education',['Graduate','Not Graduate'])
    self_emp = st.selectbox('Self_Employed',['Yes','No'])
    property = st.selectbox('Property Type',['Rural','Urban','Semi-Urban'])

if gender=="Male":
    gen_m = 1
    gen_f = 0
else:
    gen_m = 0
    gen_f = 1

if married == "Yes" :
    mar_yes = 1
    mar_no = 0
else:
    mar_yes = 0
    mar_no = 1

if education == "Graduate":
    edu_grad = 1
    edu_ngrad = 0
else:
    edu_grad = 0
    edu_ngrad = 1

if self_emp == "Yes" :
    se_yes = 1
    se_no = 0
else:
    se_yes = 0
    se_no = 1

if property == "Semi-Urban":
    prop_surb = 1
    prop_urb = 0
    pro_rur = 0 
elif property == "Urban":
    prop_surb = 0
    prop_urb = 1
    pro_rur = 0
else:
    prop_surb = 0
    prop_urb = 0
    pro_rur = 1



test_data = np.array([dependents,app_income,co_app_income,loan_amount,
                      loan_amount_term,
            credit_hist,gen_m,mar_yes,edu_ngrad, se_yes,prop_surb,prop_urb])

test_data = test_data.reshape(1,12)
test_df = pd.DataFrame(test_data,columns=['Dependents', 'ApplicantIncome', 'CoapplicantIncome', 
                        'LoanAmount','Loan_Amount_Term', 'Credit_History',
                        'Gender_Male', 'Married_Yes','Education_Not Graduate', 
                         'Self_Employed_Yes','Property_Area_Semiurban',
                         'Property_Area_Urban'])   

st.dataframe(test_df)  
gen_prediction = st.button("Predict")
if gen_prediction:
    st.success(model.predict(test_df)[0])









