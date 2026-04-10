import streamlit as st
from modules.processor import process_data
import pandas as pd

# 1. Page Configuration
st.set_page_config(layout="wide", page_title="FitSync")

# 2. Title
st.title("FitSync - Personal Health Analytics")
st.markdown("---")

# 3. Sidebar Filter
st.sidebar.header("Filters")
time_range = st.sidebar.selectbox(
    "Select Time Range", 
    options=["Last 7 Days", "Last 30 Days", "All time"], 
    index=2
)

# 4. Load the full dataset
df = process_data()

# 5. Apply the logic for Filtering
# We use the 'Date' column to determine what to keep
if time_range == "Last 7 Days":
    # Get the latest date in the data and go back 7 days
    last_date = df['Date'].max()
    df = df[df['Date'] > (last_date - pd.Timedelta(days=7))]
elif time_range == "Last 30 Days":
    # Get the latest date in the data and go back 30 days
    last_date = df['Date'].max()
    df = df[df['Date'] > (last_date - pd.Timedelta(days=30))]
# Note: If "All time" is selected, we just use the 'df' as it is.

# 6. Create the 3-column layout
col1, col2, col3 = st.columns(3)

# 7. Display the metrics (Now calculated from the FILTERED df)
with col1:
    avg_steps = int(df['Steps'].mean())
    st.metric(label="Average Steps", value=f"{avg_steps:,}", delta=None)

with col2:
    avg_sleep = round(df['Sleep_Hours'].mean(), 1)
    st.metric(label="Average Sleep Hours", value=f"{avg_sleep}h", delta=None)

with col3:
    avg_recovery = round(df['Recovery_Score'].mean(), 1)
    st.metric(label="Average Recovery Score", value=f"{avg_recovery}%", delta=None)

# 8. Data Overview
st.markdown(f"### Data Overview ({time_range})")
st.dataframe(df, use_container_width=True, height=400)