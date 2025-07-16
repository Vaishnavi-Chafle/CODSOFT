# CODSOFT Internship – Machine Learning

This repository contains the tasks I have completed as part of the **Machine Learning Internship at CODSOFT**.

---

## Task 1 – Customer Churn Prediction Web Application

### Project Overview

The goal of this project is to build a **Customer Churn Prediction System** that identifies which customers are likely to stop using a service based on their demographics and behavior.

I have developed a **Machine Learning model using Random Forest Classifier** and deployed it as an **interactive Web App using Streamlit**.

The app allows users to input customer data manually or via a **CSV file** to get churn predictions.

---

### Features

- Customer data analysis & visualization  
- Predict customer churn in real-time  
- Supports both individual and bulk predictions  
- Clean and simple user interface using **Streamlit**

---

### Technologies Used

- Python  
- Pandas, NumPy  
- Scikit-learn  
- Random Forest Classifier  
- SMOTE for imbalance handling  
- Streamlit for web deployment  
- Matplotlib, Seaborn, Plotly for data visualization  
- Joblib for model saving

---

## How to Run the Project Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Vaishnavi-Chafle/CODSOFT.git
cd CODSOFT/Task-1_Customer-Churn-Prediction
```

### 2️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```
### 3️⃣ Download the Trained Model
Due to GitHub file size limits, the trained model is stored in Google Drive.

📥 [Download Model Files Here](https://drive.google.com/file/d/1WNMQ7yWj5Adzyri6UOhKHMCiHTBgWQi7/view?usp=drive_link)

After downloading, place the files inside:
```arduino
Task-1_Customer-Churn-Prediction/models/
├── churn_model.pkl
└── scaler.pkl
```

### 4️⃣ Run the Streamlit Web App
```bash
streamlit run app.py
```
### Folder Structure
```bash
CODSOFT/
└── Task-1_Customer-Churn-Prediction/
    ├── app.py                # Streamlit web application
    ├── models/               # Trained model & scaler (download separately)
    ├── utils/                # Preprocessing helpers
    ├── data/                 # Sample input file
    ├── notebooks/            # Model training notebook
    └── requirements.txt      # Required libraries
```

### Demo Screenshot
![Demo Screenshot](./Task-1_Customer-Churn-Prediction/demo_screenshot.png)

### Project Video Demo

### About the Internship
Internship Name: CODSOFT Machine Learning Internship
Duration: 1 Month
Mode: Virtual
Deliverables: 3 Machine Learning Projects

### Contact
[Vaishnavi Chafle](https://www.linkedin.com/in/vaishnavi-chafle-357438262/)
LinkedIn Profile

Thank You! 🙌
