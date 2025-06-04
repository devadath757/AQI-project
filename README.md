# AQI-project
Project Description:
# Air Quality Index (AQI) Predictor
The Air Quality Index (AQI) Predictor is a complete end-to-end web-based machine learning project designed to predict the AQI level of a region based on pollutant concentrations. Built using Python, Streamlit, and Scikit-learn, this project combines a visually pleasing frontend interface with a reliable backend prediction model to offer real-time insights into air quality. The goal is to raise awareness about pollution and promote healthier living environments.
# Objective
This application predicts the AQI by taking six air pollutant concentrations as input:

PM1 (Particulate Matter 1.0)

PM2.5 (Particulate Matter 2.5)

NO₂ (Nitrogen Dioxide)

SO₂ (Sulfur Dioxide)

CO (Carbon Monoxide)

O₃ (Ozone)

It helps users understand how polluted the air is in a given region and provides health-related interpretations based on the AQI value.
# Backend
The backend is powered by a Linear Regression model trained using the scikit-learn library. The training process includes:

Data cleaning and preprocessing (done in the Jupyter notebook assign.ipynb)

Model training using a real-world dataset containing pollutant readings and AQI values (Bangalore_AQI_Dataset.csv)

The trained model is saved using Python's pickle module in a file named li.pkl

This model is then loaded dynamically within the Streamlit app and used to make predictions based on user inputs.
# Frontend
The frontend is built with Streamlit, a Python library for building interactive web apps. Key features include:

A clean, mobile-friendly layout with responsive design

Custom CSS styling for modern appearance (buttons, fonts, layout)

Organized input fields using two columns for better user experience

Interactive visualizations using Plotly (gauge meter that reflects the AQI status)

Color-coded prediction messages (green for good air, red for unhealthy, etc.)

Informative tooltips and messages explaining each pollutant and AQI level

The app is structured in sections:

Header and Introduction

Input Form for Pollutants

Prediction Output with Interpretation

Plotly Visualization (Gauge Meter)

Footer with Credits
# Files in the Project
aqi.py — Main Streamlit app; contains frontend code, model loading, input handling, and output display logic.

assign.ipynb — Jupyter notebook with full machine learning pipeline: data loading, preprocessing, training, testing, and model saving.

li.pkl — Pre-trained linear regression model saved using pickle.

Bangalore_AQI_Dataset.csv — Real dataset with pollutant and AQI values collected from Bangalore.

(Optional) requirements.txt — List of Python libraries needed to run the project.
# How It Works
User inputs pollutant concentrations through the web interface.

The app feeds these inputs to the pre-trained ML model.

The model returns a predicted AQI value.

Based on the value, the app displays:

AQI Category (Good, Moderate, Unhealthy, etc.)

Health recommendations

A dynamic gauge chart using Plotly
# Created By
Indrajith & Devadath
Delivering data-driven insights for a healthier environment.






