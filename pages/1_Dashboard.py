import streamlit as st

# 1. Page Configuration
st.set_page_config(layout="wide", page_title="FitSync")

from modules.processor import process_data
import pandas as pd


@st.cache_data
# 4. Load the full dataset
def load_data():
    return process_data()

df = load_data()

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
#st.markdown(f"### Data Overview ({time_range})")
#st.dataframe(df, use_container_width=True, height=400)

# 9. Visualizations (The part that was missing!)
import plotly.express as px

# Create the first row of charts
chart_row1_col1, chart_row1_col2 = st.columns(2)
with chart_row1_col1:
    # Dual Line Chart: Recovery Score and Sleep Hours
    fig_recovery_sleep = px.line(
        df, 
        x='Date',
        y=['Recovery_Score', 'Sleep_Hours'],
        title="Recovery Score & Sleep Trend"
    )
    st.plotly_chart(fig_recovery_sleep, use_container_width=True)

with chart_row1_col2:
    # Scatter Plot: recovery score vs steps
    fig_steps_recovery = px.scatter(
        df, 
        x='Steps', 
        y='Recovery_Score', 
        color='Sleep_Hours', 
        title="Recovery Score vs Daily Steps"
    )
    st.plotly_chart(fig_steps_recovery, use_container_width=True)

# Create the second row of charts
chart_row2_col1, chart_row2_col2 = st.columns(2)
with chart_row2_col1:
    # Scatter Plot: Recovery Score vs Heart Rate
    fig_hr_recovery = px.scatter(
        df, 
        x='Heart_Rate_bpm',
        y='Recovery_Score',
        title="Recovery Score vs Resting Heart Rate"
    )
    st.plotly_chart(fig_hr_recovery, use_container_width=True)

with chart_row2_col2:
    # Line Chart: Calories Burned
    fig_calories = px.line(
        df,
        x='Date',
        y='Calories_Burned',
        title="Daily Calories Burned Trend"
    )
    st.plotly_chart(fig_calories, use_container_width=True)

