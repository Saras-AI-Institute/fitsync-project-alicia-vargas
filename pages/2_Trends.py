import streamlit as st
import plotly.express as px
from modules.processor import process_data
from modules.demo_story import apply_demo_logic
import pandas as pd

# 1. Page Configuration
st.set_page_config(layout="wide", page_title="FitSync | Long-term Trends")

@st.cache_data
def load_data():
    return process_data()

df = load_data()

# 2. Filter & Demo Logic
time_range = st.sidebar.selectbox("Select Time Range", options=["Last 7 Days", "Last 30 Days", "All time"], index=2)

last_date = df['Date'].max()
if time_range == "Last 7 Days":
    filtered_df = df[df['Date'] > (last_date - pd.Timedelta(days=7))]
elif time_range == "Last 30 Days":
    filtered_df = df[df['Date'] > (last_date - pd.Timedelta(days=30))]
else:
    filtered_df = df.copy()

# Apply the storyteller logic so the trends look consistent with the dashboard
filtered_df = apply_demo_logic(filtered_df)

st.title("📈 Long-term Trend Analysis")
st.markdown("Exploring the deep correlations between lifestyle habits and physical outcomes over time.")
st.divider()

# 3. The Correlation Matrix (The "Pro" Visual)
st.subheader("🔗 The Metric Correlation Matrix")
# Selecting only numerical columns for the matrix
corr_cols = ['Recovery_Score', 'Sleep_Hours', 'Steps', 'Mood_Score', 'Heart_Rate_bpm']
corr_matrix = filtered_df[corr_cols].corr()

fig_corr = px.imshow(
    corr_matrix,
    text_auto=".2f",
    color_continuous_scale='RdBu_r', # Red is negative, Blue is positive
    title="How do my metrics influence each other?"
)
st.plotly_chart(fig_corr, use_container_width=True)
st.info("**How to read this:** A score closer to 1.0 (Red) means the metrics move together. For example, as Sleep increases, Recovery usually follows.")

st.divider()

# 4. Weekly Patterns (Heatmap Style)
st.subheader("📅 Weekly Recovery Patterns")
filtered_df['Day_of_Week'] = filtered_df['Date'].dt.day_name()
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Calculate average recovery per day
weekly_avg = filtered_df.groupby('Day_of_Week')[['Recovery_Score', 'Mood_Score']].mean().reindex(day_order).reset_index()

fig_weekly = px.bar(
    weekly_avg, 
    x='Day_of_Week', 
    y='Recovery_Score', 
    color='Mood_Score',
    color_continuous_scale='Viridis',
    title="Average Physical Readiness by Day of Week"
)
st.plotly_chart(fig_weekly, use_container_width=True)

# 5. Distribution Histograms (Now simplified in one row)
st.divider()
st.subheader("📊 Consistency Check (Distributions)")
col1, col2, col3 = st.columns(3)

with col1:
    st.plotly_chart(px.histogram(filtered_df, x='Steps', title='Steps Distribution', color_discrete_sequence=['#00d4ff']), use_container_width=True)

with col2:
    st.plotly_chart(px.histogram(filtered_df, x='Sleep_Hours', title='Sleep Distribution', color_discrete_sequence=['#7a4bff']), use_container_width=True)

with col3:
    st.plotly_chart(px.histogram(filtered_df, x='Recovery_Score', title='Recovery Distribution', color_discrete_sequence=['#ff4b4b']), use_container_width=True)

st.caption(f"FitSync Trends Engine | Analyzing {len(filtered_df)} unique days of health data.")