import streamlit as st
import numpy as np
import joblib

st.set_page_config(page_title="Calories Burnt Predictor", page_icon="🔥")

st.title("🔥 Calories Burnt Predictor")
st.caption("XGBoost model trained on exercise data")

# ── Load model ────────────────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    return joblib.load("calories_model.pkl")

try:
    model = load_model()
except FileNotFoundError:
    st.error("⚠️ `calories_model.pkl` not found. Run the notebook with `joblib.dump` first.")
    st.stop()

# ── Inputs ────────────────────────────────────────────────────────────────────
st.subheader("Enter Your Exercise Details")

col1, col2 = st.columns(2)

with col1:
    gender   = st.selectbox("Gender", ["Male", "Female"])
    age      = st.number_input("Age (years)",      min_value=15,   max_value=80,  value=25)
    height   = st.number_input("Height (cm)",      min_value=130,  max_value=220, value=170)
    weight   = st.number_input("Weight (kg)",      min_value=30,   max_value=150, value=70)

with col2:
    duration = st.number_input("Duration (min)",   min_value=1,    max_value=120, value=30)
    heart_rt = st.number_input("Heart Rate (bpm)", min_value=50,   max_value=200, value=100)
    body_tmp = st.number_input("Body Temp (°C)",   min_value=36.0, max_value=41.0, value=37.5, step=0.1)

# ── Predict ───────────────────────────────────────────────────────────────────
if st.button("Predict Calories Burnt", type="primary", use_container_width=True):
    gender_enc = 0 if gender == "Male" else 1
    features   = np.array([[gender_enc, age, height, weight, duration, heart_rt, body_tmp]])
    prediction = model.predict(features)[0]

    st.success(f"### 🔥 Estimated Calories Burnt: `{prediction:.1f}` kcal")