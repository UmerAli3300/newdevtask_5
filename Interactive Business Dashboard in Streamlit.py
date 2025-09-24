import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
plt.style.use('seaborn-v0_8')

# LOAD DATA
@st.cache_data
def load_data():
    try:
        df = pd.read_excel('/home/umer/my-forecasting-project/Sample - Superstore.xlsx', engine='openpyxl')
        df['Order Date'] = pd.to_datetime(df['Order Date'])
        return df
    except FileNotFoundError:
        st.error("File not found. Please check the file path.")
        st.stop()
    except Exception as e:
        st.error(f"Error loading data: {e}")
        st.stop()

df = load_data()

# DASHBOARD
st.title("Global Superstore Sales Dashboard")
st.markdown("Analyze sales, profit, and customer performance with interactive filters.")

# SIDEBAR FILTERS
st.sidebar.header("Filter Data")

regions = df['Region'].unique()
categories = df['Category'].unique()
sub_categories = df['Sub-Category'].unique()

selected_region = st.sidebar.multiselect("Select Region", regions, default=regions)
selected_category = st.sidebar.multiselect("Select Category", categories, default=categories)
selected_subcategory = st.sidebar.multiselect("Select Sub-Category", sub_categories, default=sub_categories)

filtered_df = df[
    (df['Region'].isin(selected_region)) &
    (df['Category'].isin(selected_category)) &
    (df['Sub-Category'].isin(selected_subcategory))
]

st.sidebar.markdown(f"**Filtered Records: {len(filtered_df):,}**")

# KPIs
col1, col2 = st.columns(2)

with col1:
    st.metric("Total Sales", f"${filtered_df['Sales'].sum():,.0f}")

with col2:
    st.metric("Total Profit", f"${filtered_df['Profit'].sum():,.0f}")

# Top 5 Customers
st.subheader("Top 5 Customers by Sales")
top_customers = filtered_df.groupby('Customer Name')['Sales'].sum().nlargest(5).reset_index()

# Display as table
st.dataframe(top_customers.style.format({'Sales': '${:,.0f}'}))

# Bar chart
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=top_customers, x='Sales', y='Customer Name', palette='viridis')
ax.set_title('Top 5 Customers by Sales', fontweight='bold')
ax.set_xlabel('Sales ($)', fontweight='bold')
ax.set_ylabel('Customer Name', fontweight='bold')
ax.grid(axis='x', alpha=0.3)
st.pyplot(fig)

# Monthly Sales Trend
st.subheader("Monthly Sales Trend")
monthly_sales = filtered_df.set_index('Order Date').resample('M')['Sales'].sum()

fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.plot(monthly_sales.index, monthly_sales.values, marker='o', linewidth=2, color='steelblue')
ax2.set_title('Monthly Sales Trend', fontweight='bold')
ax2.set_xlabel('Month', fontweight='bold')
ax2.set_ylabel('Sales ($)', fontweight='bold')
ax2.grid(True, alpha=0.3)
plt.xticks(rotation=45)
st.pyplot(fig2)
