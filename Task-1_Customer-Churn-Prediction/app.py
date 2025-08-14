import joblib

model = joblib.load("models/churn_model.pkl")
scaler = joblib.load("models/scaler.pkl")

import streamlit as st
import numpy as np
import pandas as pd
import joblib
from utils.preprocess import preprocess_input, preprocess_batch

# Load the model and scaler
model = joblib.load("models/churn_model.pkl")
scaler = joblib.load("models/scaler.pkl")

st.title("🏦 Customer Churn Prediction Web App")

menu = st.sidebar.radio("Choose Option", ["Single Prediction", "Batch Prediction"])

if menu == "Single Prediction":
    st.header("🔍 Predict for a Single Customer")

    credit_score = st.number_input("Credit Score", 300, 850, 600)
    age = st.number_input("Age", 18, 100, 35)
    tenure = st.slider("Tenure", 0, 10, 3)
    balance = st.number_input("Balance", 0.0, 250000.0, 50000.0)
    num_of_products = st.selectbox("Number of Products", [1,2,3,4])
    has_crcard = st.selectbox("Has Credit Card?", [1,0])
    is_active = st.selectbox("Is Active Member?", [1,0])
    salary = st.number_input("Estimated Salary", 0.0, 300000.0, 100000.0)
    geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
    gender = st.selectbox("Gender", ["Male", "Female"])

    input_data = {
        "CreditScore": credit_score,
        "Age": age,
        "Tenure": tenure,
        "Balance": balance,
        "NumOfProducts": num_of_products,
        "HasCrCard": has_crcard,
        "IsActiveMember": is_active,
        "EstimatedSalary": salary,
        "Geography": geography,
        "Gender": gender
    }

    if st.button("Predict"):
        scaled_input = preprocess_input(input_data, scaler)
        churn_prob = model.predict_proba(scaled_input)[0][1]
        churn_pred = model.predict(scaled_input)[0]

        if churn_pred == 1:
            st.error(f"⚠️ High Risk of Churn: {churn_prob*100:.2f}%")
        else:
            st.success(f"✅ Low Risk of Churn: {churn_prob*100:.2f}%")

elif menu == "Batch Prediction":
    st.header("📂 Bulk Prediction (CSV Upload)")
    uploaded_file = st.file_uploader("Upload CSV", type=['csv'])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        processed_data = preprocess_batch(df, scaler)
        probs = model.predict_proba(processed_data)[:,1]
        preds = model.predict(processed_data)

        df['Churn_Probability (%)'] = np.round(probs * 100, 2)
        df['Prediction'] = np.where(preds==1, "Churn", "No Churn")

        st.dataframe(df)
        st.download_button("Download Predictions", df.to_csv(index=False), "predictions.csv")

