# Forest Weather Index (FWI) Prediction

This project is an end-to-end Machine Learning application that predicts the **Forest Weather Index (FWI)** using meteorological and fire-related inputs. It covers data preprocessing, feature engineering, model training, evaluation, serialization, and deployment using Flask.

---

## Project Description

The Forest Weather Index (FWI) is a critical component of the Canadian Forest Fire Danger Rating System and is used to estimate the intensity of forest fires.  
This application allows users to input weather conditions and fire indicators through a web interface and obtain a real-time FWI prediction.

---

## Dataset

**Dataset Used:** Algerian Forest Fires Dataset  
**Source File:** `datasets/Algerian_forest_fires_dataset_UPDATE.csv`

### Data Preprocessing
- Removed null values and invalid rows
- Stripped and cleaned column names
- Converted features to appropriate numeric data types
- Encoded categorical variables:
  - `Classes`: not fire → 0, fire → 1
  - `region`: Bejaia → 0, Sidi-Bel Abbes → 1
- Removed date columns (`day`, `month`, `year`)
- Saved cleaned data for reuse

**Cleaned Dataset:** `datasets/cleaned_dataset.csv`

---

## Features and Target

### Input Features
- Temperature
- RH (Relative Humidity)
- Ws (Wind Speed)
- Rain
- FFMC
- DMC
- DC
- ISI
- BUI
- Classes
- region

### Target Variable
- FWI (Forest Weather Index)

---

## Model Details

- **Algorithm:** Linear Regression
- **Feature Scaling:** StandardScaler
- **Train-Test Split:** 80% training / 20% testing
- **Serialization:** Model and scaler saved using `pickle`

---

## Model Performance

| Metric | Value |
|--------|-------|
| Mean Squared Error (MSE) | 0.3323 |
| Mean Absolute Error (MAE) | 0.4268 |
| Root Mean Squared Error (RMSE) | 0.5765 |
| R² Score | 0.9890 |

An R² score of **0.989** indicates that the model explains approximately **98.9% of the variance** in the Forest Weather Index.

---

## Project Structure

```text
Forest_fire_prediction/
├── datasets/
│   ├── Algerian_forest_fires_dataset_UPDATE.csv
│   └── cleaned_dataset.csv
│
├── models/
│   ├── LinearRegression.pkl
│   └── scaler.pkl
│
├── src/
│   ├── linearregression.py
│   ├── application.py
│   └── templates/
│       └── home.html
│
└── README.md
```

## Flask Web Application

### Routes
- `/` – Renders the input form
- `/predict` – Accepts POST request, predicts FWI, and displays the result

### Prediction Workflow
1. User enters inputs in the web form
2. Inputs are converted to numeric values
3. Features are arranged in training order
4. StandardScaler is applied
5. Model predicts FWI
6. Result is displayed on the page

---

## How to Run the Project

### 1. Install Dependencies
pip install flask pandas numpy scikit-learn matplotlib

### 2. Train the Model
python src/linearregression.py

### 3. Start the Flask Application
python src/application.py

### 4. Open in Browser
http://127.0.0.1:5000/
---

## Author

Sai Chaitanya  
Machine Learning | Data Science | Applied AI

---

## License

This project is intended for educational and portfolio demonstration purposes.








