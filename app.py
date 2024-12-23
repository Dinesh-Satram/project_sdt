import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df_cars = pd.read_csv("vehicles_us.csv")

# Preprocess missing values
df_cars['model_year'] = df_cars.groupby('model')['model_year'].transform(lambda x: x.fillna(x.median()))
df_cars['cylinders'] = df_cars.groupby('model')['cylinders'].transform(lambda x: x.fillna(x.median()))
df_cars['odometer'] = df_cars.groupby(['model', 'model_year'])['odometer'].transform(lambda x: x.fillna(x.median()))

# Remove outliers
price_lower, price_upper = df_cars['price'].quantile([0.05, 0.95])
model_year_lower, model_year_upper = df_cars['model_year'].quantile([0.05, 0.95])
df_cars = df_cars[(df_cars['price'] >= price_lower) & (df_cars['price'] <= price_upper)]
df_cars = df_cars[(df_cars['model_year'] >= model_year_lower) & (df_cars['model_year'] <= model_year_upper)]

# Streamlit App
st.title("Vehicle Dataset Dashboard")
st.markdown(
    """
    This application provides insights into the vehicle dataset, including:
    - Scatter plots for price and odometer readings.
    - A histogram for price distribution.
    - Preprocessing of missing values and outlier removal.
    """
)

# Dataset Overview
st.header("Dataset Overview")
st.write("Here is a preview of the processed dataset:")
st.dataframe(df_cars.head())

# Price vs Odometer scatterplot
st.subheader("Price vs Odometer Scatter Plot")
scatter_plot = px.scatter(
    df_cars,
    x='odometer',
    y='price',
    color='model_year',
    title="Price vs Odometer (Colored by Model Year)",
    labels={"odometer": "Odometer (miles)", "price": "Price (USD)", "model_year": "Model Year"},
    hover_data=['model', 'condition']
)
st.plotly_chart(scatter_plot)

# Histogram for Price Distribution
st.subheader("Price Distribution Histogram")
price_histogram = px.histogram(
    df_cars,
    x='price',
    nbins=50,
    title="Price Distribution",
    labels={"price": "Price (USD)"},
    color_discrete_sequence=['blue']
)
st.plotly_chart(price_histogram)

# Additional Interactivity
st.sidebar.header("Filters")
selected_condition = st.sidebar.multiselect(
    "Select Condition(s):",
    options=df_cars['condition'].unique(),
    default=df_cars['condition'].unique()
)
filtered_data = df_cars[df_cars['condition'].isin(selected_condition)]

st.subheader("Filtered Data (Based on Condition)")
st.write(f"Displaying {len(filtered_data)} rows out of {len(df_cars)}:")
st.dataframe(filtered_data)
