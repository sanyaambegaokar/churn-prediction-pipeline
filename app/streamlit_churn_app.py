import streamlit as st
import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression

# Load the trained model (you'll save it in the next step)
model = joblib.load('app/churn_model.pkl')

# Load your customer feature dataset
#df = pd.read_csv('~/Desktop/customer_features.csv')
df = pd.read_csv('app/customer_features.csv')

# Page config
st.set_page_config(page_title="Churn Risk Checker", layout="centered")

st.title("🔍 Customer Churn Prediction")
st.write("Select a customer to see their predicted churn risk:")

# Select customer
customer_id = st.selectbox("Choose Customer ID", df['customer_id'].unique())
selected = df[df['customer_id'] == customer_id].copy()

# Show customer features
st.subheader("Customer Features")
st.write(selected[[
    'total_orders', 'total_items', 'total_revenue',
    'avg_order_value', 'days_since_last_order'
]])

# Prepare input
features = selected[[
    'total_orders', 'total_items', 'total_revenue',
    'avg_order_value', 'days_since_last_order'
]]

# Predict
prob = model.predict_proba(features)[0][1]
prediction = model.predict(features)[0]

st.subheader("Churn Prediction")
st.metric("Churn Probability", f"{prob:.2%}")
st.write("Churn Status:", "🔴 Churned" if prediction == 1 else "🟢 Active")
