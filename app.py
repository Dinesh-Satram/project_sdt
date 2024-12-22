import streamlit as st
import pandas as pd
import plotly.express as px


# Load dataset
df = pd.read_csv("vehicles_us.csv")

# Display a header
st.header("Car Advertisement Dataset Dashboard")

st.subheader("Price Distribution")
fig_hist = px.histogram(df, x="price", nbins=50, title="Price Distribution of Vehicles")
st.plotly_chart(fig_hist)

st.subheader("Price vs Odometer")
fig_scatter = px.scatter(df, x="odometer", y="price", color="condition", 
                         title="Price vs Odometer with Condition")
st.plotly_chart(fig_scatter)

# Checkbox for 4WD vehicles
if st.checkbox("Show only 4WD vehicles"):
    filtered_df = df[df["is_4wd"] == 1.0]
    st.subheader("Filtered Data: 4WD Vehicles")
    st.write(filtered_df)
