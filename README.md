# Diabetes Prediction Website

This repository contains code for a web application that predicts the likelihood of an individual having diabetes based on various input features. The application is built using Streamlit and scikit-learn.

## Features

The website allows users to input the following features:

- Gender: Select the gender of the individual (Male or Female).
- Age: Enter the age of the individual.
- Hypertension: Select if the individual has hypertension (Yes or No).
- Heart Disease: Select if the individual has a heart disease (Yes or No).
- Smoking History: Select the smoking history of the individual (Never, Former, or Current).
- BMI: Enter the Body Mass Index (BMI) of the individual.
- HbA1c Level: Enter the HbA1c level of the individual.
- Blood Glucose Level: Enter the blood glucose level of the individual.

## Getting Started

To run the web application locally, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/diabetes-prediction-website.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Run the application: `streamlit run app.py`

## How it Works

1. When the application is launched, a web page will open in your browser.
2. You will see input fields and dropdown menus to enter the individual's information.
3. Enter the required details and click the "Predict" button.
4. The application will use a pre-trained SVM model to predict the likelihood of the individual having diabetes.
5. The prediction result will be displayed on the web page.
6. The input data along with the prediction will be stored in a CSV file (`diabetes_prediction_dataset.csv`) for future reference.

## Data Analysis and Model Training

The initial dataset (`diabetes_prediction_dataset.csv`) was used to analyze the relationships between different variables and diabetes. The dataset was preprocessed, including data cleaning, handling missing values, and mapping categorical variables. Feature selection was performed using ANOVA F-value, and the selected features were standardized.

A support vector machine (SVM) model was trained using the selected features, and its performance was evaluated using accuracy. The trained SVM model was saved as a pickle file (`svm_model.pkl`) for future use.

## Folder Structure

- `app.py`: Contains the code for the Streamlit web application.
- `svm_model.pkl`: The pre-trained SVM model saved as a pickle file.
- `diabetes_prediction_dataset.csv`: The dataset used for analysis and model training.
- `requirements.txt`: Lists the required packages and their versions.

## Contributions

Contributions to this repository are welcome. If you have any suggestions or improvements, feel free to open an issue or submit a pull request
