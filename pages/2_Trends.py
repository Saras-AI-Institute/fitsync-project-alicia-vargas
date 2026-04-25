import streamlit as st
import plotly.express as px
from modules.processor import process_data
import pandas as pd

# 1. Page Configuration
st.set_page_config(layout="wide", page_title="Trends & Insights")

# 2. Title
st.title("Trends & Insights")
st.markdown("---")

# 3. Sidebar Filter
time_range = st.sidebar.selectbox(
    "Select Time Range", 
    options=["Last 7 Days", "Last 30 Days", "All time"], 
    index=2
)

@st.cache_data
# 4. Load the dataset
def load_data():
    return process_data()

df = load_data()

# 5. Apply the logic for Filtering
# Determine what to keep based on the 'Date' column
if time_range == "Last 7 Days":
    last_date = df['Date'].max()
    filtered_df = df[df['Date'] > (last_date - pd.Timedelta(days=7))]
elif time_range == "Last 30 Days":
    last_date = df['Date'].max()
    filtered_df = df[df['Date'] > (last_date - pd.Timedelta(days=30))]
else:
    filtered_df = df.copy()

# 6. Summary Statistics
st.markdown("### Summary Statistics")
summary_stats = filtered_df[['Recovery_Score', 'Sleep_Hours', 'Steps', 'Calories_Burned']].describe().loc[['mean', 'min', 'max']]
st.dataframe(summary_stats, use_container_width=True, height=200)

# 7. Average Recovery Score - Monthly Trend
st.markdown("### Average Recovery Score - Monthly Trend")
filtered_df['Month'] = filtered_df['Date'].dt.to_period('M')
monthly_avg_recovery = filtered_df.groupby('Month').Recovery_Score.mean().reset_index()

# Convert 'Month' to string for JSON serialization
monthly_avg_recovery['Month'] = monthly_avg_recovery['Month'].astype(str)

# Ensure filtered_df use strings for 'Month' where necessary
filtered_df['Month'] = filtered_df['Month'].astype(str)

fig_recovery_monthly = px.line(
    monthly_avg_recovery, 
    x='Month', 
    y='Recovery_Score', 
    labels={'Recovery_Score': 'Avg Recovery Score'},
    title="Monthly Average Recovery Score"
)
st.plotly_chart(fig_recovery_monthly, use_container_width=True)

# 8. Distribution Histograms
st.markdown("### Distributions")

# Create columns for histograms
col1, col2 = st.columns(2)

with col1:
    fig_steps_hist = px.histogram(
        filtered_df, 
        x='Steps',
        nbins=30,
        title='Distribution of Steps'
    )
    st.plotly_chart(fig_steps_hist, use_container_width=True)

    fig_calories_hist = px.histogram(
        filtered_df, 
        x='Calories_Burned',
        nbins=30,
        title='Distribution of Calories Burned'
    )
    st.plotly_chart(fig_calories_hist, use_container_width=True)

with col2:
    fig_recovery_hist = px.histogram(
        filtered_df, 
        x='Recovery_Score',
        nbins=30,
        title='Distribution of Recovery Score'
    )
    st.plotly_chart(fig_recovery_hist, use_container_width=True)

    fig_sleep_hist = px.histogram(
        filtered_df, 
        x='Sleep_Hours',
        nbins=30,
        title='Distribution of Sleep Hours'
    )
    st.plotly_chart(fig_sleep_hist, use_container_width=True)