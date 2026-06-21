import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb
import joblib
from sklearn.metrics import mean_absolute_error, r2_score

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Poultry Farm AI Dashboard",
    page_icon="🐔",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown("""
<style>

.main {
    background-color: #f8f9fa;
}

.stMetric {
    background-color: white;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.05);
}

h1, h2, h3 {
    color: #1f2937;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# TITLE
# =========================================================
st.title("🐔 Poultry Farm AI Dashboard")
st.markdown("### Weekly Profit Prediction using XGBoost")

# =========================================================
# LOAD DATA
# =========================================================
@st.cache_data
def load_data():

    file_path = "poultry_farm_v2(AutoRecovered).xlsx"

    farm = pd.read_excel(
        file_path,
        sheet_name='Farm Data'
    )

    finance = pd.read_excel(
        file_path,
        sheet_name='Financial Data '
    )

    df = farm.merge(
        finance,
        on='date',
        how='inner'
    )

    df = df.rename(
        columns={'Stock_x': 'Stock'}
    ).drop(
        columns=['Stock_y'],
        errors='ignore'
    )

    df['date'] = pd.to_datetime(df['date'])

    df = df.sort_values('date').reset_index(drop=True)

    df['week_id'] = (
        df['date']
        .dt.to_period('W')
        .astype(str)
    )

    weekly = df.groupby('week_id').agg({

        'net_profit': 'sum',
        'HD%': 'mean',
        'Mortality_Rate_%': 'mean',
        'Stock': 'mean',
        'Feed_consumption_kg': 'sum',
        'eggs_daily': 'sum',
        'age_day': 'mean'

    }).reset_index()

    weekly = weekly.sort_values(
        'week_id'
    ).reset_index(drop=True)

    return weekly


weekly = load_data()

# =========================================================
# FEATURE ENGINEERING
# =========================================================
weekly['age_week'] = weekly['age_day'] // 7

for lag in [1, 2, 4]:

    weekly[f'profit_lag_{lag}'] = (
        weekly['net_profit'].shift(lag)
    )

    weekly[f'hd_lag_{lag}'] = (
        weekly['HD%'].shift(lag)
    )

for w in [2, 4, 6]:

    weekly[f'roll_profit_{w}'] = (
        weekly['net_profit']
        .rolling(w)
        .mean()
    )

    weekly[f'roll_hd_{w}'] = (
        weekly['HD%']
        .rolling(w)
        .mean()
    )

weekly = weekly.dropna().reset_index(drop=True)

# =========================================================
# TRAIN / TEST
# =========================================================
test_size = int(len(weekly) * 0.20)

train = weekly.iloc[:-test_size]
test  = weekly.iloc[-test_size:]

target = 'net_profit'

features = [

    col for col in weekly.columns

    if col not in ['week_id', target]

]

X_train = train[features]
y_train = train[target]

X_test = test[features]
y_test = test[target]

# =========================================================
# LOAD / TRAIN MODEL
# =========================================================
try:

    model = joblib.load(
        "weekly_profit_model2_final.pkl"
    )

except:

    model = xgb.XGBRegressor(

        n_estimators=250,
        learning_rate=0.03,
        max_depth=3,
        min_child_weight=10,
        subsample=0.70,
        colsample_bytree=0.70,
        reg_alpha=4.0,
        reg_lambda=8.0,
        random_state=42

    )

    model.fit(X_train, y_train)

# =========================================================
# EVALUATION
# =========================================================
pred_train = model.predict(X_train)
pred_test  = model.predict(X_test)

train_mae = mean_absolute_error(
    y_train,
    pred_train
)

test_mae = mean_absolute_error(
    y_test,
    pred_test
)

train_r2 = r2_score(
    y_train,
    pred_train
)

test_r2 = r2_score(
    y_test,
    pred_test
)

# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.header("📥 Enter Weekly Farm Data")

HD = st.sidebar.slider(
    "HD%",
    40.0,
    100.0,
    75.0
)

mortality = st.sidebar.slider(
    "Mortality Rate %",
    0.0,
    20.0,
    2.0
)

stock = st.sidebar.number_input(
    "Stock",
    value=70000
)

feed = st.sidebar.number_input(
    "Feed Consumption (kg)",
    value=9000
)

eggs = st.sidebar.number_input(
    "Eggs Produced",
    value=500000
)

age_day = st.sidebar.number_input(
    "Age (Days)",
    value=300
)

# =========================================================
# CREATE INPUT
# =========================================================
last_row = weekly.iloc[-1:].copy()

last_row['HD%'] = HD
last_row['Mortality_Rate_%'] = mortality
last_row['Stock'] = stock
last_row['Feed_consumption_kg'] = feed
last_row['eggs_daily'] = eggs
last_row['age_day'] = age_day
last_row['age_week'] = age_day // 7

input_data = last_row[features]

prediction = model.predict(input_data)[0]

# =========================================================
# METRICS
# =========================================================
st.subheader("📊 Model Performance")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Train MAE",
    f"{train_mae:,.0f}"
)

c2.metric(
    "Test MAE",
    f"{test_mae:,.0f}"
)

c3.metric(
    "Train R²",
    f"{train_r2:.2f}"
)

c4.metric(
    "Test R²",
    f"{test_r2:.2f}"
)

st.divider()

# =========================================================
# PREDICTION CARD
# =========================================================
st.subheader("💰 Expected Weekly Profit")

st.success(
    f"Predicted Net Profit: {prediction:,.0f} EGP"
)

st.divider()

# =========================================================
# ACTUAL VS PREDICTED
# =========================================================
st.subheader("📈 Actual vs Predicted")

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    y_test.values,
    label='Actual',
    linewidth=3
)

ax.plot(
    pred_test,
    label='Predicted',
    linewidth=3
)

ax.legend()

plt.xticks(rotation=45)

st.pyplot(fig)

# =========================================================
# FEATURE IMPORTANCE
# =========================================================
st.subheader("🔥 Feature Importance")

importance = pd.DataFrame({

    'Feature': features,
    'Importance': model.feature_importances_

})

importance = importance.sort_values(
    by='Importance',
    ascending=False
)

fig2, ax2 = plt.subplots(figsize=(10, 6))

sns.barplot(

    data=importance.head(10),

    x='Importance',
    y='Feature',

    ax=ax2

)

st.pyplot(fig2)

# =========================================================
# CORRELATION HEATMAP
# =========================================================
st.subheader("🧠 Correlation Heatmap")

fig3, ax3 = plt.subplots(figsize=(12, 8))

corr = weekly.corr(numeric_only=True)

sns.heatmap(

    corr,
    annot=True,
    cmap='coolwarm',
    fmt='.2f',
    ax=ax3

)

st.pyplot(fig3)

# =========================================================
# DATA PREVIEW
# =========================================================
st.subheader("📄 Weekly Data Preview")

st.dataframe(
    weekly.tail(20),
    use_container_width=True
)