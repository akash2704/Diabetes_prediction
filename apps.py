import streamlit as st
import pandas as pd
import pickle

# Load the pre-trained SVM model
with open("svm_model.pkl", "rb") as f:
    svm_model = pickle.load(f)

# Function to make prediction using the SVM model
def predict_diabetes(gender, age, hypertension, heart_disease, smoking_history, bmi, hba1c_level, blood_glucose_level):
    features = [[age, bmi, hba1c_level, blood_glucose_level]]
    prediction = svm_model.predict(features)[0]
    return prediction

# Streamlit app
def main():
    st.title("Diabetes Prediction App")
    
    # Gender
    gender = st.radio("Select Gender:", ('Male', 'Female'))
    
    # Age
    age = st.number_input("Enter Age:", min_value=1, max_value=150)
    
    # Hypertension
    hypertension = st.selectbox("Hypertension:", ('No', 'Yes'))
    
    # Heart Disease
    heart_disease = st.selectbox("Heart Disease:", ('No', 'Yes'))
    
    # Smoking History
    smoking_history = st.radio("Smoking History:", ('Never', 'Former', 'Current'))
    
    # BMI
    bmi = st.number_input("Enter BMI:")
    
    # HbA1c Level
    hba1c_level = st.number_input("Enter HbA1c Level:")
    
    # Blood Glucose Level
    blood_glucose_level = st.number_input("Enter Blood Glucose Level:")
    
    # Predict button
    if st.button("Predict"):
        # Map radio button values to numeric values
        hypertension_mapping = {'No': 0, 'Yes': 1}
        heart_disease_mapping = {'No': 0, 'Yes': 1}
        hypertension = hypertension_mapping[hypertension]
        heart_disease = heart_disease_mapping[heart_disease]
        
        # Make prediction
        prediction = predict_diabetes(gender, age, hypertension, heart_disease, smoking_history, bmi, hba1c_level, blood_glucose_level)
        
        # Load the existing data from the CSV file
        data = pd.read_csv('diabetes_prediction_dataset.csv')
        
        # Append inputs and prediction to DataFrame
        new_row = {"gender": gender, "age": age, "hypertension": hypertension, "heart_disease": heart_disease, 
                   "smoking_history": smoking_history, "bmi": bmi, "HbA1c_level": hba1c_level, 
                   "blood_glucose_level": blood_glucose_level, "diabetes": prediction}
        
        # Append the new row to the existing data
        data = pd.concat([data, pd.DataFrame(new_row, index=[0])], ignore_index=True)
        
        # Save DataFrame to CSV
        data.to_csv('diabetes_prediction_dataset.csv', index=False)
        
        # Display prediction
        st.write("Prediction:", prediction)

# Run the app
if __name__ == '__main__':
    main()