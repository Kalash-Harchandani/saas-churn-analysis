# SaaS Churn Analytics

This project analyzes customer churn for a SaaS platform using a real-world dataset. The goal is to uncover the key drivers behind user attrition and provide actionable business insights for improving customer retention.

## Project Structure

```
saas-churn-analysis/
├── data/                       # Contains the CSV files (accounts, subscriptions, churn_events, etc.)
├── notebooks/
│   └── analysis.ipynb          # Jupyter Notebook with the end-to-end data processing and analytics
├── venv/                       # Python virtual environment
└── README.md                   # Project documentation
```

## Methodology

1. **Data Preprocessing & Cleaning**: Formatted date types and handled missing values across multiple tables.
2. **Aggregations & Logic Validations**: Implemented structured data logic (pre-aggregation of support tickets and feature usage) prior to joining metrics to the main table to avoid cartesian explosions and inaccurate measurements.
3. **Data Integration**: Merged five disparate datasets (Accounts, Subscriptions, Churn Events, Support Tickets, Feature Usage) into a master analytical dataframe.
4. **Visualizations**: Generated business-ready visualizations exploring the correlation between pricing tiers, feature usage, customer support occurrences, and churn trends.

## Key Insights

- **Overall Churn**: Stands at approximately ~70%.
- **Impact of Support Tickets**: Support friction is a leading indicator for churn; churned accounts exhibit significantly higher average tickets.
- **Feature Usage vs. Attrition**: Usage rates do not significantly differ between retained vs. churned customers, indicating that product adoption is not the bottleneck.
- **Tenure Correlation**: Retained customers stay substantially longer (~4.5x), emphasizing that initial onboarding & issue resolution in the first few months are critical to crossing the "retention plateau."

## Tech Stack
- **Python** (Pandas, NumPy)
- **Data Visualization** (Matplotlib, Seaborn)
- **Jupyter Notebook**
