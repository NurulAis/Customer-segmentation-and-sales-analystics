
# Retail Customer Segmentation & Sales Analytics Using RFM and Machine Learning
[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue)](https://www.python.org/) 
[![ML: K-Means](https://img.shields.io/badge/ML%20Algorithm-K--Means-orange)](https://scikit-learn.org/stable/)
[![Status: Complete](https://img.shields.io/badge/Status-Complete-green)](https://github.com/NurulAis/Customer-segmentation-and-sales-analystics)
[![Looker Studio](https://img.shields.io/badge/Dashboard-Looker%20Studio-B043FF)](https://lookerstudio.google.com/u/0/reporting/911492e8-c36d-490f-b1f8-bee117ae25f2/page/k7fiF)

This project performs a 360-degree analysis of e-commerce transaction data, integrating in-depth Exploratory Data Analysis (EDA) and RFM analysis to power an **advanced Machine Learning-based segmentation model**.



## 🔗 Full Report, Segment Profiles, and Business Recommendations
The complete methodology, detailed charts on sales trends, demographic insights, and comprehensive segment profiles are available on my portfolio website: 
* **[Full Report](https://www.notion.so/Retail-Customer-Segmentation-Sales-Analytics-Using-RFM-and-Machine-Learning-2c43308755628027a14bdb006f2007ba)**
* **[Dashboard 1: Sales Performance](https://lookerstudio.google.com/u/0/reporting/126b8b8a-bcfb-4a93-9e08-25460bbf1e85/page/hxfiF)** 
* **[Dashboard 2: Customer Segmentation & RFM Deep Dive](https://lookerstudio.google.com/u/0/reporting/911492e8-c36d-490f-b1f8-bee117ae25f2/page/k7fiF)**


## 🎯 Project Goals
The primary objectives were to transform raw transaction data into actionable business intelligence:
1.  **Understand Business Performance**: Analyze sales trends, popular products, and customer demographics (gender, location, age) to identify growth opportunities.
2.  **Evaluate Customer Experience**: Extract insights on payment methods, product ratings, and customer feedback.
3.  **Advanced Segmentation**: Develop highly effective customer groups by integrating RFM scores with additional behavioral features using Machine Learning.

## ⚙️ Methodology Overview
The project was executed in two major phases: Data Analysis and Advanced Segmentation.

### Phase 1: Exploratory Data Analysis (EDA) & Business Insights
* **Sales Trend Analysis**: Investigated monthly sales patterns.
* **Product Insights**: Identified top-performing products
* **Customer & Operational Insights**: Analyzed **demographics**, preferred **payment methods**, and patterns in **customer ratings**.

### Phase 2: Multi-Dimensional Customer Segmentation (ML-Driven)
Customer groups were derived using a two-step approach:

1.  **RFM Baseline Segmentation**: Calculated Recency, Frequency, and Monetary values to establish initial segments.
2.  **Advanced ML Segmentation**: Develop highly effective customer groups by integrating RFM scores with **Age, product rating features, Gender, and Income** using Machine Learning.


## 📊 Key Findings & Segment Summary
### Business & Operational Insights
* **Sales Trends (Mar 2023 - Feb 2024)**: Sales demonstrated high consistency throughout the year, peaking with the highest revenue recorded in August 2023 and the lowest total transaction amount in February 2024.
* **Geographic & Revenue Drivers**: Revenue contribution analysis shows that Chicago is the highest-contributing city, followed by England at the state level, within the overall top revenue-generating country, the USA.
* **Product & Category Performance**: The Electronics category is the largest contributor to total revenue. Pepsi brand dominates individual product sales.
* **Customer Experience & Feedback**: The most frequent rating given by customers is 4 Stars, with the most common recorded qualitative feedback being "Excellent", indicating a generally high level of satisfaction.
* **Payment Method**: Credit Card stands out as the most dominant payment method used by customers, while PayPal is the least favored option.
* **Shipping Preference**: The majority of customers overwhelmingly prefer the Same Day shipping method, underscoring a strong demand for speed and convenience.
### Segmentation Results
* **Segmentation Outcome**: The analysis successfully yielded 5 distinct customer segments. This method revealed nuanced behavioral patterns, **enabling highly targeted retention and upsell campaigns** not achievable through pure RFM analysis.
**👉 For detailed data visualizations, statistical breakdowns, and actionable strategies derived from these insights, please see the full report on the dedicated website.**
## 📁 Repository Structure
| Directory/File | Description |
| :--- | :--- |
| `notebooks/` | Contains all analytical notebooks. |
| `src/` | Custom Python functions for feature engineering and data cleaning. |
| `data/` | Raw and cleaned dataset files. |
| `requirements.txt` | List of all Python dependencies. |

## Tech Stack
* **Language**: Python 3.10
* **Core Libraries**: Pandas, NumPy, Scikit-learn
* **Visualization**: Matplotlib, Seaborn
* **Dashboarding**: Looker Studio
* **Environment**: Jupyter Notebook, VS Code
