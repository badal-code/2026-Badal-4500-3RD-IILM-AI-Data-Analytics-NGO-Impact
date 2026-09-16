# AI Data Analytics — NGO Impact & Donation Analytics

**Author:** Badal  
**Institution:** IILM University, Greater Noida  
**Domain:** AI Data Analytics / Social Impact Analytics

> **Data notice:** This repository uses synthetic demonstration data. It does not contain confidential or proprietary InAmigos Foundation records.

## 1. Project Overview

This project presents an end-to-end data analytics workflow for an NGO/social-impact context. It combines donation analytics, beneficiary impact analysis, volunteer analytics, program efficiency metrics, exploratory machine learning and an interactive dashboard.

The project is designed as a portfolio-quality demonstration of how Python-based analytics can turn structured operational data into measurable insights.

## 2. Problem Statement

NGO operations can involve multiple data dimensions such as donations, programs, beneficiaries and volunteers. A structured analytics workflow can help organize these records, identify trends, compare program activity and monitor measurable indicators.

## 3. Objectives

- Analyze donation patterns and funding distribution.
- Identify trends by program, state, donor type and channel.
- Evaluate beneficiary attendance and outcome indicators.
- Analyze volunteer participation and contribution hours.
- Demonstrate donor segmentation using K-Means clustering.
- Build an interactive Streamlit dashboard.
- Maintain reproducible and documented analytics workflows.

## 4. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming |
| Pandas | Data manipulation |
| NumPy | Numerical processing |
| Scikit-learn | Machine learning |
| Plotly | Interactive visualization |
| Streamlit | Dashboard |
| Jupyter | Exploratory analysis |
| Git/GitHub | Version control |

## 5. Datasets

The repository contains four synthetic datasets:

- `donations.csv`
- `beneficiaries.csv`
- `volunteers.csv`
- `programs.csv`

See [`data/DATA_DICTIONARY.md`](data/DATA_DICTIONARY.md) for field definitions.

## 6. Data Processing Pipeline

```text
Synthetic Data
      ↓
Data Validation
      ↓
Cleaning & Transformation
      ↓
Exploratory Data Analysis
      ↓
Analytical Modules
      ↓
Machine Learning
      ↓
Plotly Visualizations
      ↓
Streamlit Dashboard
```

## 7. Analytical Modules

### Module 1 — Donation & Donor Analysis
- Total funds raised
- Average donation
- Donor type comparison
- Donation channel analysis
- Repeat donor share
- State-wise contribution

### Module 2 — Beneficiary Impact Analysis
- Beneficiary distribution
- Attendance analysis
- Outcome score analysis
- Urban/rural comparison
- Program-level impact indicators

### Module 3 — Program Efficiency Analysis
- Program budgets
- Planned vs represented beneficiaries
- Cost per represented beneficiary
- Funding distribution

### Module 4 — Volunteer Analytics
- Volunteer count
- Volunteer hours
- Skill-area distribution
- Program-wise contribution
- Activity duration

### Module 5 — Donor Segmentation & Machine Learning
K-Means clustering is demonstrated using aggregated donor-type features:
- total contribution
- average contribution
- donation count
- repeat-donor rate

The clusters are exploratory and should not be treated as validated labels for real individuals.

### Module 6 — Time-Series & Impact Trends
- Monthly donation trends
- Program funding trends
- Beneficiary outcome patterns
- Monitoring-oriented KPIs

## 8. Visualizations

The project uses Plotly for:
- bar charts
- line charts
- scatter plots
- comparative KPI views
- program and channel analysis

## 9. Interactive Dashboard

The Streamlit dashboard provides:
- donation KPIs
- state and program filters
- program funding charts
- monthly donation trend
- beneficiary impact table
- attendance vs outcome visualization
- volunteer contribution analysis
- program budget table

### Run Dashboard

```bash
pip install -r requirements.txt
streamlit run dashboard/app.py
```

## 10. Data Cleaning & Transformation

The cleaning layer performs:
- duplicate removal
- numeric type conversion
- date conversion
- missing-value handling
- positive donation validation
- monthly feature creation

Reusable functions are stored in `src/data_cleaning.py`.

## 11. Machine Learning

The project demonstrates unsupervised learning with K-Means.

### Workflow

```text
Aggregated Donor Features
          ↓
Feature Scaling
          ↓
K-Means Clustering
          ↓
Exploratory Segments
          ↓
Visualization
```

The ML component is intentionally presented as a demonstration rather than a production decision system.

## 12. Repository Structure

```text
├── README.md
├── requirements.txt
├── CHANGELOG.md
├── data/
├── src/
├── notebooks/
├── dashboard/
├── reports/
├── screenshots/
├── models/
└── .github/workflows/
```

## 13. Reproducibility

Synthetic data is generated with a fixed random seed (`42`) so the demonstration can be reproduced consistently.

## 14. Data Ethics

This repository does not include personal donor or beneficiary information.

Any future integration with real organizational data should follow:
- authorization requirements
- privacy and data-minimization principles
- secure storage
- access control
- appropriate anonymization
- organizational policies

## 15. Limitations

- Demonstration datasets are synthetic.
- Results cannot be interpreted as real organizational findings.
- Donor segmentation is exploratory.
- Program efficiency metrics depend on the available fields.
- No production deployment or real-time data pipeline is included.

## 16. Future Scope

- Authorized real-data integration
- Automated ETL pipeline
- Advanced donor-level segmentation
- Predictive donation forecasting
- More robust model evaluation
- Secure dashboard deployment
- Automated reporting
- Role-based access controls

## 17. Learning Outcomes

This project demonstrates practical experience with:
- Python data analysis
- Pandas and NumPy
- exploratory data analysis
- data cleaning
- KPI design
- interactive visualization
- machine learning fundamentals
- Streamlit dashboard development
- Git/GitHub project organization
- responsible handling of synthetic data

## 18. Project Documentation

- [`reports/PROJECT_REPORT.md`](reports/PROJECT_REPORT.md)
- [`reports/PROJECT_REPORT_OUTLINE.md`](reports/PROJECT_REPORT_OUTLINE.md)
- [`data/DATA_DICTIONARY.md`](data/DATA_DICTIONARY.md)
- [`dashboard/README.md`](dashboard/README.md)

## 19. Author

**Badal**  
B.Tech CSE — IILM University, Greater Noida
intern at amingos
2scs1003004500


## 20. Project Summary

This repository demonstrates how an AI/data analytics workflow can combine structured data processing, descriptive analytics, machine learning and interactive visualization into a single social-impact analytics solution.
