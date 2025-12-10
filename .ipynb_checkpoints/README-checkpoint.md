<p align="center">
  <img src="https://img.shields.io/badge/Student%20Performance%20Analyzer-%20Data%20Science-blueviolet?style=for-the-badge" alt="project badge"/>
</p>

# 🎓 Student Performance Analyzer
Analyze and visualize student exam performance using Python 🐍, Pandas, and Seaborn to uncover patterns and insights.

**Author:** Kishan S T  
🎓 B.Tech CSE (Data Science) | Christ (Deemed to be University)  
📧 [kishan45@gmail.com](mailto:kishan45@gmail.com)  
🌐 [GitHub Profile](https://github.com/KISHAN-ST)

## 📁 Project Structure
student-performance-analyzer/
├── 📂 data/ → Datasets  
├── 📓 notebooks/ → Jupyter notebooks  
├── ⚙️ src/ → Helper scripts  
└── 📘 README.md → Project overview

## 🚀 How to Run
1. Open **Anaconda Navigator** 🐍
2. Activate your environment (`spa`)
3. Launch **Jupyter Notebook**
4. Open and run: `notebooks/Student_Performance_Analyzer.ipynb`

## 🧩 Project Progress

### **Phase 1: Setup**
✅ Created GitHub repository  
✅ Added project structure and README.md  
✅ Set up Python environment (`spa`) in Anaconda  
✅ Created Jupyter notebook for analysis  

---

### **Phase 2: Data Loading & Cleaning**
✅ Loaded dataset from **Kaggle**  
✅ Explored dataset using `.info()` and `.describe()`  
✅ Checked for missing values using `.isnull().sum()`  
✅ Verified clean dataset ready for analysis  


## 📊 Phase 3: Data Comparison & Visualization

In this phase, I explored the relationships between different factors influencing student performance. Using **Seaborn** and **Matplotlib**, I created visual comparisons to understand trends better.

### 🔍 Key Tasks:
- Compared **test preparation courses** with math, reading, and writing scores  
- Added **hue-based color differentiation** to make the visual insights clearer  
- Visualized results using **bar plots** with `sns.barplot()`  

### 📈 Sample Code:
```python
plt.figure(figsize=(8,5))
sns.barplot(x='test preparation course', y='math score', data=data, hue='gender', palette='cool')
plt.title('Math Score by Test Preparation Course and Gender')
plt.show()

## 📌 Phase 4 – Correlation Analysis

**What I did in this phase:**
- Calculated correlation matrix for the dataset  
- Visualized correlation using a heatmap  
- Identified top positive and negative relationships  
- Used insights to understand what factors influence others  

**Key Learnings:**
- Correlation shows relationships, not causation  
- Strong correlation helps in selecting features for ML models  

**Outputs Generated:**
- Correlation matrix  
- Heatmap visualization  
