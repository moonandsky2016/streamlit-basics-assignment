import streamlit as st
import pandas as pd

# Title and description
st.title("Sales Dashboard")
st.subheader("Simple sales summary with category filter")

# Hardcoded dataset
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Headphones", "Monitor", "Keyboard"],
    "Category": ["Electronics", "Electronics", "Electronics", "Accessories", "Accessories", "Accessories"],
    "Sales": [1200, 800, 600, 150, 300, 100]
}

df = pd.DataFrame(data)

# Sidebar filter
st.sidebar.header("Filter Options")
category = st.sidebar.selectbox(
    "Select Category",
    options=df["Category"].unique()
)

# Filtered data
filtered_df = df[df["Category"] == category]

# Display table
st.write(f"### Showing data for: {category}")
st.dataframe(filtered_df)

# Line chart
st.write("### Sales Trend")
st.line_chart(filtered_df["Sales"])