# SaaS Churn Analytics

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical-blue?logo=numpy)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange?logo=plotly)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Viz-lightblue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit)

---

## 📊 Overview

This project analyzes **customer churn in a SaaS platform** using a multi-table real-world dataset.  
The goal is to identify **key churn drivers** and generate **actionable insights** to improve customer retention.

---

## ⚙️ Methodology

### 1. Data Cleaning & Preprocessing
- Standardized date formats and handled missing values  
- Ensured consistency across multiple datasets  

### 2. Aggregations & Data Integrity
- Performed **pre-aggregation of support tickets and feature usage**  
- Prevented **cartesian joins and duplication errors**  
- Maintained accurate metric calculations  

### 3. Data Integration
- Merged **5 datasets**:
  - Accounts  
  - Subscriptions  
  - Churn Events  
  - Support Tickets  
  - Feature Usage  
- Built a **master dataset (~700+ records)** using joins  

### 4. Exploratory Data Analysis
- Analyzed churn across:
  - Plan tiers  
  - Customer tenure  
  - Feature usage  
  - Support interactions  

### 5. Visualization & Dashboard
- Built **Matplotlib & Seaborn visualizations**  
- Developed a **Streamlit dashboard** for interactive insights  

---

## 📈 Key Insights

- **Churn Rate:** ~80% of users churned  
- **Support Impact:** Higher support ticket volume correlates with increased churn  
- **Engagement:** Low-engagement users show significantly higher churn risk  
- **Tenure Effect:** Customers with longer tenure are far less likely to churn  

---

## 🛠 Tech Stack

- **Python** (Pandas, NumPy)  
- **Visualization** (Matplotlib, Seaborn)  
- **Dashboard** (Streamlit)  
- **Notebook** (Jupyter)  

---

## 🚀 How to Run

```bash
# Clone repo
git clone https://github.com/Kalash-Harchandani/saas-churn-analysis.git

# Navigate
cd saas-churn-analysis

# Install dependencies
pip install -r requirements.txt

# Run notebook
jupyter notebook
