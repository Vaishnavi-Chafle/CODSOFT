import numpy as np
import pandas as pd

def preprocess_input(data, scaler):
    geo_germany = 1 if data["Geography"] == "Germany" else 0
    geo_spain = 1 if data["Geography"] == "Spain" else 0
    gender_male = 1 if data["Gender"] == "Male" else 0

    features = np.array([[
        data["CreditScore"],
        data["Age"],
        data["Tenure"],
        data["Balance"],
        data["NumOfProducts"],
        data["HasCrCard"],
        data["IsActiveMember"],
        data["EstimatedSalary"],
        geo_germany,
        geo_spain,
        gender_male
    ]])

    return scaler.transform(features)

def preprocess_batch(df, scaler):
    df['Geo_Germany'] = (df['Geography'] == 'Germany').astype(int)
    df['Geo_Spain'] = (df['Geography'] == 'Spain').astype(int)
    df['Gender_Male'] = (df['Gender'] == 'Male').astype(int)

    features = df[["CreditScore", "Age", "Tenure", "Balance", "NumOfProducts",
                   "HasCrCard", "IsActiveMember", "EstimatedSalary", "Geo_Germany",
                   "Geo_Spain", "Gender_Male"]]

    return scaler.transform(features)
