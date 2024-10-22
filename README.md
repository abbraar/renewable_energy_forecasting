# Solar Production Forecasting Project

## Overview
This project focuses on **solar production forecasting** for the French energy grid. Using historical data on solar energy production, we implemented various machine learning models to predict future energy production, ultimately deploying the best-performing model for public use. The goal is to help **renewable energy producers** accurately forecast their production and receive fair compensation, as per French energy regulations.

## Dataset Description
The dataset includes **hourly records** of wind and solar energy production (in megawatts) for the French grid since 2020. It was primarily collected to assist the **Commission de Régulation de l'Énergie (CRE)** in calculating reference prices, which are used to determine additional remuneration for renewable energy producers in France.

### Key Points:
- The dataset is used to calculate additional remuneration as outlined in Articles L. 314-18 to L. 314-27 of the **Energy Code**.
- The **additional remuneration** compensates producers for the difference between their market income and a pre-determined reference remuneration.
- This system ensures producers are exposed to short-term market price fluctuations while still receiving fair remuneration.

## Project Workflow

Before we dive into the details of the project steps, here's an overview of the entire workflow:

![Project Workflow](https://raw.githubusercontent.com/abbraar/renewable_energy_forecasting/8980eacf3b6d79078e0c8f76be20dcfe38552085/project_workflow.png)


### 1. Data Gathering & Preparation
- **Data Collection**: Retrieved hourly records for wind and solar production.
- **Datetime Processing**: Renamed and converted datetime columns for consistency.
- **Handling Missing & Duplicate Values**: Cleaned and imputed missing data, and removed duplicates.

### 2. Data Analysis
- **Resampling & Smoothing**: Resampled the data to align with the forecasting frequency and smoothed the time series.
- **Stationarity Check**: Analyzed data for stationarity.
- **Seasonal Decomposition**: Decomposed the solar data into trend, seasonality, and residuals using Seasonal Decomposition Analysis.

### 3. Model Selection & Training
We explored and compared several models, trained using historical solar energy production data.

#### Models Implemented:
1. **Prophet** (Best Performing Model)
   - **MAPE**: 20.6%
   - **MAE**: ~5000
2. **Simple RNN**
3. **TBATS**
4. **LSTM**
5. **Hybrid CNN-LSTM**
6. **GRU**
7. **N-BEATS**
8. **XGBoost**

### 4. Model Evaluation
We used the following evaluation metrics to compare model performance:
- **Mean Absolute Error (MAE)**
- **Mean Absolute Percentage Error (MAPE)**

### 5. Optimization & Final Model Selection
After evaluating the models, **Prophet** was chosen as the best model for solar production forecasting due to its superior accuracy.

## Deployment

#### 1. Model Export
- The trained Prophet model was exported using **Pickle** for use in deployment.

#### 2. API Development
- We wrapped the model in an API using **FastAPI**.

#### 3. Dockerization
- Created and deployed a Docker container for the API.

#### 4. Deployment
- The FastAPI app was deployed on **Render** for public access.

#### 5. Streamlit Application
We also built a **Streamlit app** to serve the forecasting model as a web service. The app was tested and deployed, allowing users to interact with the forecasting tool.

## Conclusion
While we initially worked on forecasting for both wind and solar data, the wind data lacked discernible trends and seasonality, which led to less reliable forecasting results. Therefore, we focused solely on deploying the solar forecasting model.

---

This project successfully delivers a reliable solar production forecasting tool, offering insights that can help renewable energy producers optimize their operations and ensure they receive appropriate compensation based on energy market dynamics.
