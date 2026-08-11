# 🏠 House Price Prediction — Linear Regression

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red)
![R2 Score](https://img.shields.io/badge/R²%20Score-97.24%25-brightgreen)
![Status](https://img.shields.io/badge/Status-Live-success)

> A machine learning web app that predicts house prices using Linear Regression — built with Python, Scikit-learn, and deployed on Streamlit Cloud.

🔗 **Live App:** [Click here to try it](https://house-price-predictor-calvd78saem5uzyujb6o6j.streamlit.app/)

---

## 📌 Project Overview

This project predicts the sale price of a house based on key features like size, quality, year built, and more. The model was trained on the Kaggle House Prices dataset and achieves **97.24% R² accuracy** after feature engineering and outlier removal — improved from a 46% baseline.

---

## 🎯 Problem Statement

> Given a set of house features, can we accurately predict the sale price?

---

## 📊 Dataset

| Detail | Info |
|---|---|
| Source | Kaggle — House Prices Dataset |
| Total Records | 1,460 houses |
| Target Variable | SalePrice |

---

## 🔧 Features Used

| Feature | Description |
|---|---|
| GrLivArea | Above-ground living area (sq ft) |
| OverallQual | Overall quality rating (1–10) |
| YearBuilt | Year the house was built |
| TotalBsmtSF | Total basement area (sq ft) |
| GarageArea | Garage size (sq ft) |
| FullBath | Number of full bathrooms |
| BedroomAbvGr | Number of bedrooms above ground |
| LotArea | Total lot size (sq ft) |

---

## 🧪 Model Performance

| Metric | Score |
|---|---|
| **R² Score** | **97.24%** |
| Baseline R² (3 features only) | 46.25% |
| Improvement | +50.99% after feature engineering |

> 💡 Key insight: Adding `OverallQual` alone jumped R² from 46% to 70%+. Removing outliers pushed it to 97.24%.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core programming language |
| Pandas & NumPy | Data cleaning & manipulation |
| Matplotlib | Data visualization |
| Scikit-learn | ML model (LinearRegression) |
| Pickle | Model serialization |
| Streamlit | Web app & deployment |
| GitHub | Version control |

---

## 📈 ML Pipeline

```
Raw CSV Data
    ↓
Exploratory Data Analysis (EDA)
    ↓
Data Cleaning (nulls, duplicates, outliers)
    ↓
Feature Selection (8 key features)
    ↓
Train / Test Split (80% / 20%)
    ↓
Linear Regression Model
    ↓
Evaluation (MAE, RMSE, R² Score)
    ↓
Streamlit Web App Deployment
```

---

## 🚀 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/your-username/house-price-predictor.git

# 2. Go to project folder
cd house-price-predictor

# 3. Install requirements
pip install -r requirements.txt

# 4. Run the app
python -m streamlit run house_app.py
```

---

## 📁 Project Structure

```
house-price-predictor/
│
├── house_app.py                     # Streamlit web application
├── house_price_prediction.ipynb     # Full ML pipeline notebook
├── house_model.pkl                  # Saved trained model
├── house_prices_practice.csv        # Dataset
├── requirements.txt                 # Dependencies
└── README.md                        # Project documentation
```

---

## 💡 Key Learnings

- Feature selection has massive impact — went from 46% to 97% R²
- `OverallQual` is the single strongest predictor of house price
- Outlier removal significantly improves Linear Regression accuracy
- Streamlit makes ML models accessible to non-technical users

---

## 👤 Author

**Pratik Mishra**
- 📧 pratikmisha141@gmail.com
- 🔗 [LinkedIn](https://linkedin.com/in/pratik-mishra)
- 🐙 [GitHub](https://github.com/Pratik1419)

---

⭐ If you found this project useful, please give it a star!
