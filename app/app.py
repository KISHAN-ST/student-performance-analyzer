import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns


# Load model and feature columns
model = joblib.load("rf_math_model.joblib")
feature_cols = joblib.load("feature_columns.joblib")

data = pd.read_csv("StudentsPerformance.csv")


st.title("Student Performance Analyzer – Math Score Predictor")
st.markdown("""
### 📘 About This App  
This tool predicts a student's **Math Score** based on their reading score, writing score, lunch type, gender, parental education, and test preparation.

It uses a **Random Forest Regression model** trained on the popular *Students Performance* dataset.

""")


# UI Inputs
gender = st.selectbox("Gender", ["male", "female"])
race = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
parent = st.selectbox("Parental Level of Education", [
    "associate's degree", "bachelor's degree", "master's degree",
    "some college", "some high school", "high school"
])
lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
prep = st.selectbox("Test Preparation Course", ["none", "completed"])
reading = st.slider("Reading Score", 0, 100, 50)
writing = st.slider("Writing Score", 0, 100, 50)
st.markdown("---")


# Create input row
df = pd.DataFrame([{
    "gender": gender,
    "race_ethnicity": race,
    "parental_level_of_education": parent,
    "lunch": lunch,
    "test_preparation_course": prep,
    "reading_score": reading,
    "writing_score": writing
}])

# Encode exactly like training
df_encoded = pd.get_dummies(df, drop_first=True)
df_encoded = df_encoded.reindex(columns=feature_cols, fill_value=0)

# Predict
if st.button("Predict Math Score"):
    pred = model.predict(df_encoded)[0]
    st.success(f"Predicted Math Score: {pred:.2f}")

st.info("""
### 📈 Model Performance  
- **Random Forest R²:** 0.85  
- **MAE:** ~4.6  
""")

st.success(f"🎯 Predicted Math Score: **{pred:.2f}**")

st.subheader("📌 Math Score by Gender")

fig, ax = plt.subplots(figsize=(8,4))
sns.boxplot(x="gender", y="math score", data=data, ax=ax)
st.pyplot(fig)

st.subheader("🍱 Lunch Type vs Math Score")

fig, ax = plt.subplots(figsize=(8,4))
sns.boxplot(x="lunch", y="math score", data=data, ax=ax)
st.pyplot(fig)

st.subheader("📚 Test Prep Course vs Math Score")

fig, ax = plt.subplots(figsize=(8,4))
sns.boxplot(x="test preparation course", y="math score", data=data, ax=ax)
st.pyplot(fig)

st.subheader("🔥 Correlation Heatmap")

# Select ONLY numeric columns for correlation
numeric_data = data.select_dtypes(include=['int64', 'float64'])

fig, ax = plt.subplots(figsize=(8, 4))
sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)


