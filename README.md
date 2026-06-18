# 📊 Bluestock Mutual Fund Analytics Capstone

## End-to-End Mutual Fund Analytics Platform using Python, SQLite & Power BI

An end-to-end data analytics project that transforms raw mutual fund datasets into actionable business insights through automated ETL pipelines, financial risk analysis, and interactive Power BI dashboards.

---

## 📌 Project Overview

This project demonstrates the complete analytics lifecycle—from data ingestion and preprocessing to advanced financial analysis and business intelligence visualization.

The platform enables users to evaluate mutual fund performance, analyze investor behaviour, measure portfolio risk, and generate data-driven investment insights.

---

## 🚀 Key Features

* Automated ETL Pipeline using Python
* Data Cleaning & Preprocessing
* SQLite Database Integration
* Exploratory Data Analysis (EDA)
* Historical Value at Risk (VaR)
* Conditional Value at Risk (CVaR)
* Rolling 90-Day Sharpe Ratio
* Investor Cohort Analysis
* SIP Continuity Analysis
* Sector Concentration Analysis (HHI)
* Risk-Based Mutual Fund Recommendation System
* Interactive Power BI Dashboard

---

## 🛠️ Tech Stack

| Technology       | Usage                       |
| ---------------- | --------------------------- |
| Python           | Data Processing & Analytics |
| Pandas           | Data Manipulation           |
| NumPy            | Numerical Computing         |
| SQLite           | Database Management         |
| SQL              | Querying                    |
| Power BI         | Dashboard & Visualization   |
| Matplotlib       | Charts & Analysis           |
| Git & GitHub     | Version Control             |
| Jupyter Notebook | Data Exploration            |

---

## 📂 Project Structure

```text
mutual-fund-project/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── EDA_Analysis.ipynb
│   └── Advanced_Analytics.ipynb
│
├── reports/
│   ├── var_cvar_report.csv
│   ├── rolling_sharpe_chart.png
│   ├── cohort_analysis.csv
│   ├── sip_continuity_analysis.csv
│   └── hhi_report.csv
│
├── dashboard/
│   └── bluestock_mf_dashboard.pbix
│
├── recommender.py
├── clean_data.py
├── data_ingestion.py
├── load_to_sqlite.py
├── live_nav_fetch.py
├── README.md
└── requirements.txt
```

---

## 📈 Dashboard Highlights

The Power BI dashboard provides an interactive overview of:

* Total Assets Under Management (AUM)
* SIP Inflow Trends
* Fund Performance Analysis
* Risk vs Return Comparison
* Investor Demographics
* Transaction Analysis
* Sector Allocation
* Market Trend Analysis

Interactive slicers enable dynamic filtering by state, age group, fund category, and investment period.

---

## 📊 Advanced Analytics

### Historical VaR & CVaR

Calculated downside risk using the 95% confidence level to estimate potential losses under adverse market conditions.

### Rolling 90-Day Sharpe Ratio

Measured risk-adjusted fund performance over time using rolling window analysis.

### Investor Cohort Analysis

Segmented investors by their first investment year to identify long-term behavioural trends.

### SIP Continuity Analysis

Detected investors at risk of discontinuing SIPs based on transaction intervals.

### Sector Concentration Analysis (HHI)

Evaluated portfolio diversification using the Herfindahl-Hirschman Index.

### Fund Recommendation System

Developed a rule-based recommendation engine that suggests the top three mutual funds based on user-selected risk appetite and Sharpe Ratio.

---

## 📌 Business Outcomes

* Automated financial data processing workflow
* Improved visibility into fund performance
* Quantified portfolio downside risk
* Enhanced investor behaviour analysis
* Measured portfolio diversification
* Enabled data-driven investment recommendations
* Delivered interactive business intelligence dashboards

---

## 📷 Dashboard Preview

> Add screenshots of:
>
> * Industry Overview
> * Fund Performance
> * Investor Analytics
> * SIP & Market Trends

---

## ⚙️ How to Run

### Clone the Repository

```bash
git clone https://github.com/TathaD/mutual-fund-project.git
cd mutual-fund-project
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run ETL Pipeline

```bash
python data_ingestion.py
python clean_data.py
python load_to_sqlite.py
```

### Run Advanced Analytics

```bash
jupyter notebook notebooks/Advanced_Analytics.ipynb
```

### Run Fund Recommender

```bash
python recommender.py
```

### Open Dashboard

Open `bluestock_mf_dashboard.pbix` using Microsoft Power BI Desktop.

---

## 🔮 Future Enhancements

* Real-time NAV integration using APIs
* Machine Learning-based fund recommendation engine
* Investor churn prediction
* Time-series forecasting
* Cloud deployment
* Automated reporting
* Web-based analytics platform

---

## 👨‍💻 Author

**Tathagata Das**

B.Tech in Computer Science & Engineering

St. Thomas' College of Engineering & Technology

GitHub: https://github.com/TathaD

---

## ⭐ Acknowledgement

This project was developed as part of the **Bluestock Mutual Fund Analytics Capstone**, demonstrating the practical application of data engineering, financial analytics, and business intelligence to solve real-world investment analysis challenges.
