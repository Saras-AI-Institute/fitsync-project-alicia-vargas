import pandas as pd #organizes into tables
import numpy as np #gives range
from datetime import datetime, timedelta 

# Set random seed for reproducibility
np.random.seed(42)

# Generate dates for the year 2025
start_date = datetime(2025, 1, 1)
dates = [start_date + timedelta(days=i) for i in range(365)] #running a loop so that all the other dates

# Generate synthetic data
steps = np.random.normal(loc=8500, scale=1800, size=365).clip(3000, 18000)#loc means mean, scale is standard div
sleep_hours = np.random.normal(loc=7.2, scale=1.0, size=365).clip(4.5, 9.5)
heart_rate = np.random.normal(loc=68, scale=10, size=365).clip(48, 110)
calories_burned = np.random.uniform(1800, 4200, 365)
active_minutes = np.random.uniform(20, 180, 365)

# Create DataFrame or rows and columns
data = pd.DataFrame({
    'Date': dates,
    'Steps': steps,
    'Sleep_Hours': sleep_hours,
    'Heart_Rate_bpm': heart_rate,
    'Calories_Burned': calories_burned,
    'Active_Minutes': active_minutes
})

# Introduce 5% missing values in each column
for column in data.columns: #skip date column
    data.loc[data.sample(frac=0.05).index, column] = np.nan #loc is lock

# Save to CSV
output_path = 'data/health_data.csv'
data.to_csv(output_path, index=False)

print(f"Synthetic fitness data generated and saved to {output_path}.")
