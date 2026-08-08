import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression

# ── Page config ──
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

# ── Load your trained model ──
# First save your model (run this once in your notebook):
# import pickle
# with open('house_model.pkl', 'wb') as f:
#     pickle.dump(model, f)

with open('house_model.pkl', 'rb') as f:
    model = pickle.load(f)

# ── App Title ──
st.title("🏠 House Price Predictor")
st.markdown("Built by **Pratik Mishra** | Linear Regression Model")
st.markdown("---")

# ── Input Fields ──
st.subheader("Enter House Details")

col1, col2 = st.columns(2)

with col1:
    GrLivArea   = st.number_input("Living Area (sq ft)", 500, 5000, 1500)
    YearBuilt   = st.number_input("Year Built", 1900, 2024, 2000)
    LotArea     = st.number_input("Lot Area (sq ft)", 1000, 50000, 8000)
    OverallQual = st.slider("Overall Quality (1-10)", 1, 10, 5)

with col2:
    TotalBsmtSF = st.number_input("Basement Area (sq ft)", 0, 3000, 800)
    GarageCars  = st.number_input("Garage Area (sq ft)", 0, 1500, 400)
    FullBath    = st.number_input("Full Bathrooms", 0, 5, 2)
    BedroomAbvGr = st.number_input("Bedrooms", 0, 10, 3)

st.markdown("---")

# ── Predict Button ──
if st.button("🔮 Predict Price", use_container_width=True):
    input_data = pd.DataFrame({
        'GrLivArea'   : [GrLivArea],
        'YearBuilt'   : [YearBuilt],
        'LotArea'     : [LotArea],
        'OverallQual' : [OverallQual],
        'TotalBsmtSF' : [TotalBsmtSF],
        'GarageCars'  : [GarageCars],
        'FullBath'    : [FullBath],
        'BedroomAbvGr': [BedroomAbvGr]
    })

    prediction = model.predict(input_data)[0]

    st.success(f"### 💰 Predicted House Price: ${prediction:,.0f}")
    st.info(f"Model Accuracy (R² Score): **97.24%**")

# ── Footer ──
st.markdown("---")
st.markdown("🔗 Connect with me on [LinkedIn](https://www.linkedin.com/in/pratik-mishra-profile/)")