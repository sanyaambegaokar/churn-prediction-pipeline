# 🧠 Customer Churn Prediction Pipeline
(Full-stack customer churn prediction project using PostgreSQL, dbt, Python, scikit-learn, and Streamlit)

A full-stack data project that predicts customer churn based on historical transaction behavior using PostgreSQL, dbt, Python, scikit-learn, and Streamlit.

---

## 🚀 Overview
This project simulates how a modern data team ingests, transforms, and operationalizes customer data to predict churn and guide retention strategies. 
Built from scratch using open retail data, it includes:

- ✅ Data ingestion into PostgreSQL
- ✅ Data transformation with dbt (staging + marts)
- ✅ Feature engineering and churn labeling in Python
- ✅ Logistic regression model training
- ✅ Deployed Streamlit app for churn risk scoring

---

## 🧱 Architecture
Excel → PostgreSQL → dbt → Python → scikit-learn → Streamlit


---

## 📊 Dataset

- Source: [UCI Online Retail II Dataset](https://archive.ics.uci.edu/ml/datasets/Online+Retail+II)
- Two years of transaction data from a UK-based online retailer.
- Features include: invoice ID, customer ID, order date, product, quantity, and price.

---

## 🧪 ML Model

- Target: **Predict whether a customer is churned (inactive for 90+ days)**
- Features: total_orders, total_items, total_revenue, avg_order_value, days_since_last_order
- Model: Logistic Regression (`scikit-learn`)
- Evaluation: Precision, Recall, F1 Score

---

## 🌐 Streamlit App (Local Preview)
 🔍 Predict churn risk for a selected customer using the trained model.

Run it locally:

## 🧠 Key Learnings
- How to structure full-stack data projects (raw → model → app)
- Building modular, testable SQL transformations in dbt
- Using feature engineering + labeling for ML-ready data
- Deploying interactive ML apps with Streamlit

## 🌐 Streamlit App (Live)

🟢 Try it live → [Click here to open the app](https://YOUR-STREAMLIT-APP-URL)

> Predict customer churn using the trained model. Select a customer ID and view churn probability and key metrics.


🙋‍♀️ Author
Sanya Ambegaokar
@sanyaambegaokar
