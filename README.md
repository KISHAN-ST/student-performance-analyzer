<p align="center">
  <img src="https://img.shields.io/badge/Student%20Performance%20Analyzer-%20Data%20Science-blueviolet?style=for-the-badge" alt="project badge"/>
</p>

# 🎓 Student Performance Analyzer
A complete end-to-end Machine Learning project that predicts **Math Scores** of students and provides deep visual insights using **Python, EDA, ML Models, and a Streamlit Web App**.

---

## 👨‍💻 Author
**Kishan S T**  
🎓 B.Tech CSE (Data Science), Christ University  
📧 Email: *stkishan45@gmail.com*  
🌐 GitHub: https://github.com/KISHAN-ST  

---

# 📁 Project Structure
```
student-performance-analyzer/
│
├── app/                         → Streamlit Deployment
│   ├── app.py
│   ├── rf_math_model.joblib
│   ├── feature_columns.joblib
│   ├── StudentsPerformance.csv
│
├── data/                        → Training-related datasets
│   ├── StudentsPerformance.csv
│   ├── train_encoded.csv
│
├── notebooks/                   → EDA + Model Training Notebooks
│   ├── Student_Performance_Analyzer.ipynb
│   ├── prepare_training_data.ipynb
│
├── src/                         → Helper scripts (future expansion)
│   ├── train_model.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 🚀 How to Run the Project Locally

### 1️⃣ Install Python Packages
```
pip install -r requirements.txt
```

### 2️⃣ Run the Streamlit App
```
cd app
streamlit run app.py
```

App will open at:
```
http://localhost:8501
```

---

# 🧩 PHASE-WISE PROJECT BREAKDOWN

Below is the entire project explained in phases exactly like a professional ML workflow.

---

# ✅ **Phase 1: Setup**
- Created GitHub repository  
- Organized project folder structure  
- Set up Python virtual environment (`spa`)  
- Installed required libraries  
- Created initial notebook for exploration  

---

# ✅ **Phase 2: Data Loading & Cleaning**
- Loaded the Kaggle dataset  
- Analyzed structure using `.info()` and `.describe()`  
- Checked missing values → none found  
- Cleaned and standardized column names  
- Dataset ready for EDA  

---

# 📊 **Phase 3: Data Comparison & Visualization**
Using Seaborn + Matplotlib to explore patterns:

### ✔ Visualization tasks:
- Math score vs test preparation  
- Reading vs writing score relationship  
- Gender-wise performance distribution  
- Lunch type vs performance  

### Example plot:
```python
plt.figure(figsize=(8,5))
sns.barplot(x='test preparation course', y='math score',
            data=data, hue='gender', palette='cool')
plt.title('Math Score by Test Preparation Course and Gender')
plt.show()
```

---

# 🔥 **Phase 4: Correlation Analysis**
- Generated correlation matrix  
- Built heatmap using Seaborn  
- Identified strong correlations:
  - Reading ↔ Math  
  - Writing ↔ Math  
  - Reading ↔ Writing  
- Used insights for feature selection  

---

# 🧠 **Phase 5: Feature Engineering**
### ✔ Created `overall_score`  
(but removed from model later to prevent leakage)

### ✔ One-hot encoded categorical columns:
- Gender  
- Lunch  
- Test prep  
- Race/Ethnicity  
- Parental education  

### ✔ Shape After Encoding:
- 1000 rows × 14 features (after dropping target + leakage)

---

# 🤖 **Phase 6: Model Training & Evaluation**

Two models were trained and compared:

## 🔹 Linear Regression
- R² Score: **0.88**
- MAE: **4.21**

## 🔹 Random Forest Regressor (Final Model)
- n_estimators = 200  
- R² Score: **0.85**
- MAE: **4.67**

### ✔ Final Model Saved:
- `rf_math_model.joblib`
- `feature_columns.joblib`

This ensures **perfect alignment** with Streamlit input.

---

# 🌐 **Phase 7: Streamlit Deployment**

Built a fully working app with:

### ✔ Clean UI  
### ✔ Dropdowns + Sliders  
### ✔ Real-time prediction  
### ✔ Automatic one-hot encoding  
### ✔ Safe feature alignment  
### ✔ Display of model performance  

---

# 📊 **Phase 8: Dashboard + Feature Importance + EDA**

Added a complete dashboard inside Streamlit:

### ✔ Math score distribution  
### ✔ Reading vs writing scatter plot  
### ✔ Gender, lunch, test-prep boxplots  
### ✔ Correlation heatmap  
### ✔ Random Forest feature importance plot  
### ✔ Organized UI Sections  

This turns the app into a **full analytics tool**, not just a predictor.

---

# 🧾 **Phase 9: Documentation + GitHub Setup**

- Prepared professional-quality README.md  
- Organized project into clean modular folders  
- Created `requirements.txt`  
- Added `.gitignore`  
- Ready for GitHub deployment  

---

# 📦 Requirements

```
streamlit
pandas
numpy
matplotlib
seaborn
scikit-learn
joblib
```

---

# 🎯 Conclusion

This project demonstrates:

- End-to-end ML pipeline  
- Proper feature engineering  
- Understanding of leakage prevention  
- Model evaluation & interpretation  
- Deployment using Streamlit  
- Professional dashboard & UI  
- Clean documentation  

A complete Data Science project fit for resumes, GitHub portfolios, and LinkedIn posts.

---

# 📬 Contact
💼 **Kishan S T**  
📧 Email: *stkishan45@gmail.com*  
🌐 GitHub: https://github.com/KISHAN-ST  
