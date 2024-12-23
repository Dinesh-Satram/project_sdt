# SDT_project
# Car Advertisement Dataset Dashboard

## Overview
This project is a **Streamlit-based web application** for visualizing and analyzing the "Car Advertisement Dataset." The app provides an interactive dashboard to explore key insights from the dataset, such as price distribution and relationships between price and odometer readings.

Additionally, an **Exploratory Data Analysis (EDA)** is conducted in `EDA.ipynb`, offering a deeper understanding of the dataset.

---

## Features
- **Price Distribution**: A histogram visualizing the price range of vehicles in the dataset.
- **Price vs Odometer Scatter Plot**: Interactive visualization showing the relationship between a car's price and odometer reading, categorized by condition.
- **Filter for 4WD Vehicles**: A checkbox allows users to filter and display data specific to 4-wheel drive vehicles.

---

## Dataset
The application uses a dataset named `vehicles_us.csv` with the following attributes:
- `price`: The price of the vehicle.
- `odometer`: The odometer reading of the vehicle (in miles).
- `condition`: The condition of the vehicle (e.g., new, used, etc.).
- `is_4wd`: Indicates if the vehicle has 4-wheel drive (1.0 = Yes, 0.0 = No).

---

## Requirements
The application requires the following Python packages:
- `pandas==2.0.3`
- `streamlit==1.25.0`
- `plotly==5.15.0`

Make sure these dependencies are listed in your `requirements.txt` file.

---

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/project_sdt.git
   cd project_sdt

2. Install the required dependencies:
pip install -r requirements.txt

3. Run the Streamlit application:
streamlit run app.py

4. Open the app in your browser at:
https://project-sdt-a799.onrender.com



File Descriptions

app.py: The main file for the Streamlit application.
vehicles_us.csv: The dataset used for the dashboard.
EDA.ipynb: A Jupyter notebook containing exploratory data analysis of the dataset.

Deployment

This application is deployed on Render. Access it live at: https://<APP_NAME>.onrender.com
