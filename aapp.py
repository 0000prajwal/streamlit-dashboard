import streamlit as st
import pandas as pd


# Title
st.title("📊 Sales Dashboard")

# Load data
df = pd.read_csv("sales_data.csv")

# Show data
st.subheader("Raw Data")
st.write(df)

# Sales by Region
st.subheader("Sales by Region")
region_sales = df.groupby("Region")["Sales"].sum()
st.bar_chart(region_sales)

# Sales by Product
st.subheader("Sales by Product")
product_sales = df.groupby("Product")["Sales"].sum()
st.bar_chart(product_sales)