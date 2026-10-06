# Salary Prediction using Machine Learning

## Project Description

This project predicts an employee's salary based on their years of experience using Machine Learning.

The project uses a Salary Dataset containing two main variables:

* **Experience Years** – input feature
* **Salary** – target variable

A Linear Regression model is trained on the dataset to learn the relationship between experience and salary.

## Dataset

The dataset was obtained from:

Sagar Chhabriya's Data Science GitHub repository.

The dataset contains 200 records with the following columns:

* Experience Years
* Salary

## Machine Learning Model

The model used in this project is **Linear Regression**.

Linear Regression is suitable for this project because the goal is to predict a numerical value (salary) based on years of experience.

The dataset is divided into:

* **80% training data**
* **20% testing data**

The model is trained using the training data and evaluated using the testing data.

## Model Evaluation

The model is evaluated using the following metrics:

Evaluation Metrics

MAE: 4056.34
MSE: 23745684.25
RMSE: 4872.95
R² Score: 0.9831

These metrics are used to measure how well the model predicts salary values.

## Streamlit Application

A Streamlit web application is created for making predictions.

The user enters their **years of experience**, and the trained Linear Regression model predicts the expected salary.

The Streamlit application loads the previously saved model instead of training the model again.

## Project Structure

```text
Salary_Prediction/
│
├── app.py
├── requirements.txt
├── README.md
│
└── model/
    └── salary_prediction_model.pkl
```

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Joblib
* Streamlit
* Matplotlib

## Conclusion

This project demonstrates an end-to-end Machine Learning workflow, starting from loading and exploring the dataset, training and evaluating a Linear Regression model, saving the trained model, and using it in a Streamlit application for salary prediction.
