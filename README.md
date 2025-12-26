```markdown
# Forest Weather Index (FWI) Prediction – Machine Learning & Flask Application

This project is an end-to-end Machine Learning application that predicts the **Forest Weather Index (FWI)** using meteorological and fire-related inputs. It covers the complete ML lifecycle: data cleaning, feature engineering, model training, evaluation, serialization, and deployment using Flask.

---

## 📝 Project Description
The Forest Weather Index (FWI) is a critical component of the Canadian Forest Fire Danger Rating System (CFFDRS) used to estimate the intensity of forest fires. This application allows users to input weather conditions and fire indicators through a web interface to obtain real-time FWI predictions.



---

## 📊 Dataset
**Dataset Used:** Algerian Forest Fires Dataset  
**Source File:** `datasets/Algerian_forest_fires_dataset_UPDATE.csv`

### Data Preprocessing
* **Cleaning:** Removed null values, invalid rows, and stripped whitespace from column names.
* **Type Conversion:** Converted features to appropriate numeric data types.
* **Encoding:** * `Classes`: `not fire → 0`, `fire → 1`
    * `region`: `Bejaia → 0`, `Sidi-Bel Abbes → 1`
* **Feature Selection:** Removed date columns (`day`, `month`, `year`) to focus on atmospheric and fuel indicators.

**Cleaned Dataset:** `datasets/cleaned_dataset.csv`

---

## ⚙️ Features & Target
### Input Features
The model utilizes 11 key features:
* **Meteorological:** Temperature, RH (Relative Humidity), Ws (Wind Speed), Rain.
* **Fire Indicators:** FFMC, DMC, DC, ISI, BUI.
* **Categorical:** Classes, Region.

### Target Variable
* **FWI:** Forest Weather Index.

---

## 🤖 Model Details
* **Algorithm:** Linear Regression
* **Feature Scaling:** `StandardScaler` (to normalize input variance)
* **Train-Test Split:** 80% Training / 20% Testing
* **Artifacts:** The trained model and scaler are serialized using `pickle`.

### Model Performance
The Linear Regression model demonstrated strong predictive performance:

| Metric | Value |
| :--- | :--- |
| **Mean Squared Error (MSE)** | 0.3323 |
| **Mean Absolute Error (MAE)** | 0.4268 |
| **Root Mean Squared Error (RMSE)** | 0.5765 |
| **R² Score** | **0.9890** |

> **Note:** An R² score of 0.989 indicates that the model explains approximately 98.9% of the variance in the Forest Weather Index.

---

## 📁 Project Structure
```text
Forest_fire_prediction/
│
├── datasets/
│   ├── Algerian_forest_fires_dataset_UPDATE.csv
│   └── cleaned_dataset.csv
│
├── models/
│   ├── LinearRegression.pkl
│   └── scaler.pkl
│
├── src/
│   ├── linearregression.py    # Model training and preprocessing script
│   ├── application.py         # Flask application backend
│   └── templates/
│       └── home.html          # Prediction UI (HTML form)
│
└── README.md

```

---

## 🌐 Flask Web Application

The web interface provides an intuitive way to interact with the model.

### Prediction Workflow

1. **Input:** User enters values into the HTML form.
2. **Processing:** Inputs are converted to numeric format and aligned with training features.
3. **Scaling:** The `scaler.pkl` is applied to the raw inputs.
4. **Inference:** The `LinearRegression.pkl` model calculates the FWI.
5. **Output:** The predicted FWI value is rendered back to the user.

---

## 🚀 How to Run the Project

### 1. Install Dependencies

Ensure you have Python installed, then run:

```bash
pip install flask pandas numpy scikit-learn matplotlib

```

### 2. Train the Model (Optional)

If you wish to re-generate the pickle files:

```bash
python src/linearregression.py

```

### 3. Start the Flask App

```bash
python src/application.py

```

### 4. Open in Browser

Navigate to: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 👤 Author

**Sai Chaitanya** *Machine Learning | Data Science | Applied AI*

---

## 📜 License

This project is intended for educational and portfolio demonstration purposes.
