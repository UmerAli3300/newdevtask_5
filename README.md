# Task 5: Interactive Business Dashboard in Streamlit

## Objective
Build an interactive dashboard to analyze Global Superstore sales, profit, and customer performance.

## Approach
- Loaded and cleaned Global Superstore dataset.
- Built Streamlit dashboard with filters: Region, Category, Sub-Category.
- Displayed KPIs: Total Sales, Total Profit, Top 5 Customers.
- Added bonus: Monthly sales trend chart.

## Features
 Interactive filters (sidebar)  
 Real-time KPI updates  
 Top 5 customers table + bar chart  
 Monthly sales trend line chart  

## Insight
- Sales and profit vary significantly by region/category — filters enable deep dives.
- Top customers drive significant revenue — focus retention efforts here.

## How to Run
1. `pip install streamlit pandas openpyxl matplotlib seaborn`
2. Place `Sample - Superstore.xlsx` in same folder
3. Run: `streamlit run task5newdev.py`
