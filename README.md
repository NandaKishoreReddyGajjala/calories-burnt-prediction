# Calories Burnt Prediction — XGBoost

Predict the calories burnt during an exercise session from gender, age, height, weight,
duration, heart rate and body temperature, using an `XGBRegressor`. Includes a Streamlit app
for interactive predictions.

| | |
|---|---|
| 🚀 Live app | [https://calories-burnt-prediction-xgb.streamlit.app](https://calories-burnt-prediction-xgb.streamlit.app/) |
| 📓 Kaggle notebook | https://www.kaggle.com/code/nandakishorereddy1/calories-burnt-prediction-with-xgboost |
| 💻 GitHub | https://github.com/NandaKishoreReddyGajjala/calories-burnt-prediction |

## Results

| Metric | Score |
|---|---|
| Mean Absolute Error (test, 3 000 rows) | **1.48 kcal** |

Target range in the data is 1–314 kcal, so the model is very accurate. `Duration`, `Heart_Rate`
and `Body_Temp` are the strongest predictors.

## Dataset

Kaggle `fmendes/fmendesdat263xdemos` — `exercise.csv` (15 000 sessions, 7 features) joined with
`calories.csv` (target) on row order. No missing values.

## Project structure

```
calories-burnt-prediction/
├── data/
│   ├── exercise.csv                  # features
│   └── calories.csv                  # target
├── Calories_Burnt_Prediction.ipynb   # load → explore → visualise → correlation → split → train → evaluate → save
├── calories_model.pkl                # trained XGBRegressor (joblib)
├── app.py                            # Streamlit app
└── requirements.txt
```

## Run locally

```bash
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
streamlit run app.py
```

Re-run the notebook to retrain and overwrite `calories_model.pkl`.
