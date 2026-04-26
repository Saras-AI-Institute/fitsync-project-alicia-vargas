import streamlit as st
import pandas as pd
import plotly.express as px
from modules.processor import process_data
#following line is for a demo version. comment out or delete once using real data to insure integrity of data. Remember to also filter out line 40.
from modules.demo_story import apply_demo_logic
# 1. Page Configuration
st.set_page_config(
    layout="wide", 
    page_title="FitSync | Data Intelligence",
    page_icon="📊"
)

# 2. Data Loading with Cache
@st.cache_data
def get_clean_data():
    return process_data()

df = get_clean_data()
# 3. Sidebar Navigation & Filters
with st.sidebar:
    st.title("Filters")
    time_range = st.selectbox(
        "Select Time Range",
        options=["Last 7 Days", "Last 30 Days", "All time"],
        index=2
    )
    st.divider()
    st.info("The dashboard updates automatically based on your /data folder.")

# 4. Filter Logic
last_date = df['Date'].max()
if time_range == "Last 7 Days":
    df_filtered = df[df['Date'] > (last_date - pd.Timedelta(days=7))]
elif time_range == "Last 30 Days":
    df_filtered = df[df['Date'] > (last_date - pd.Timedelta(days=30))]
else:
    df_filtered = df

# --- MOVE THE DEMO NUDGE HERE ---
# Now that df_filtered actually exists, we can apply the logic!
from modules.demo_story import apply_demo_logic
df_filtered = apply_demo_logic(df_filtered)
# --------------------------------

# 5. Header
st.title("📊 Personal Health Analytics")
st.markdown(f"**Viewing:** {time_range} | **Timeline:** {df_filtered['Date'].min().strftime('%Y-%m-%d')} to {last_date.strftime('%Y-%m-%d')}")

# 6. Top-Level Metrics
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric("Avg Steps", f"{int(df_filtered['Steps'].mean()):,}")
with m2:
    st.metric("Avg Sleep", f"{df_filtered['Sleep_Hours'].mean():.1f}h")
with m3:
    st.metric("Avg Recovery", f"{df_filtered['Recovery_Score'].mean():.1f}%")
with m4:
    st.metric("Avg Mood", f"{df_filtered['Mood_Score'].mean():.1f}/10")

st.divider()

# 7. Row 1: Physical Performance
col1, col2 = st.columns(2)

with col1:
    # Recovery & Sleep Trend
    fig_trend = px.line(
        df_filtered, 
        x='Date', 
        y=['Recovery_Score', 'Sleep_Hours'],
        title="Physical Readiness vs. Sleep Duration",
        color_discrete_sequence=["#ff4b4b", "#00d4ff"] # Vibrant Red and Blue
    )
    st.plotly_chart(fig_trend, use_container_width=True)

with col2:
    # Recovery vs Steps Scatter
    fig_scatter = px.scatter(
        df_filtered, 
        x='Steps', 
        y='Recovery_Score', 
        color='Sleep_Hours',
        size='Sleep_Hours',
        title="Movement Impact on Recovery",
        color_continuous_scale='Portland'
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

# 8. Row 2: Mind & Body Correlation
col3, col4 = st.columns(2)

with col3:
    # Mood vs Steps with Trendline
    fig_mood_steps = px.scatter(
        df_filtered, 
        x='Steps', 
        y='Mood_Score', 
        color='Sleep_Hours',
        trendline="ols",
        title="Correlation: Steps vs. Emotional State",
        color_continuous_scale='Turbo'
    )
    st.plotly_chart(fig_mood_steps, use_container_width=True)

with col4:
    # Heart Rate vs Recovery
    fig_hr = px.scatter(
        df_filtered, 
        x='Heart_Rate_bpm', 
        y='Recovery_Score', 
        color='Mood_Score',
        title="Heart Rate Variability & Recovery Density",
        color_continuous_scale='Magma'
    )
    st.plotly_chart(fig_hr, use_container_width=True)

st.divider()
st.subheader("🕸️ The Lifestyle Footprint")

# 1. Clean and Explode (Same logic as before)
df_radar = df_filtered.copy()
df_radar['activities'] = df_radar['activities'].str.split(' | ')
df_radar = df_radar.explode('activities')
df_radar['activities'] = df_radar['activities'].str.strip()
df_radar = df_radar[~df_radar['activities'].isin(['No Entry', 'None', '', 'nan', '|'])]

if not df_radar.empty:
    radar_data = df_radar.groupby('activities')['Recovery_Score'].mean().reset_index()

    # 2. Create the smoothed Radar Chart
    fig_radar = px.line_polar(
        radar_data, 
        r='Recovery_Score', 
        theta='activities', 
        line_close=True,
        template="plotly_dark"
    )

    # 3. Apply the "Adobe Glow" Styling
    fig_radar.update_traces(
        fill='toself', 
        fillcolor='rgba(0, 212, 255, 0.3)', # Light blue glow with transparency
        line_color='#00d4ff',             # Electric Cyan border
        line_width=3,
        line_shape='spline',              # THIS SMOOTHS THE CHOPPY LINES
        marker=dict(
            color='#ff4b4b',              # Vibrant red points
            size=8,
            symbol='diamond'
        )
    )

    # 4. Clean up the "choppy" numbers and axis
    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                showticklabels=False,      # Hide the messy numbers on the lines
                ticks="",
                gridcolor="rgba(255, 255, 255, 0.1)"
            ),
            angularaxis=dict(
                gridcolor="rgba(255, 255, 255, 0.1)",
                tickfont=dict(size=12, color="#eee")
            ),
            bgcolor="rgba(0,0,0,0)"        # Transparent background
        ),
        showlegend=False,
        margin=dict(l=80, r=80, t=20, b=20)
    )
    
    st.plotly_chart(fig_radar, use_container_width=True)
    
    st.info(f"""
**Understanding the Footprint:** Your **Recovery Score** is a calculated metric of overall physical readiness, derived from your Sleep Hours, average Heart Rate, and activity volume. 

The 'spikes' in this chart identify which specific lifestyle activities consistently correlate with a higher readiness score, helping you see which habits truly fuel your performance.
""")
else:
    st.warning("Insufficient data for the footprint analysis.")

# 6. Footer
st.caption("FitSync v2.0 | Processing independent data streams from Apple Health & Daylio")

# 9. Activity Intelligence
st.divider()
st.subheader("🧠 Activity Intelligence")
act_col1, act_col2 = st.columns([2, 1])

with act_col1:
    # Split activities and calculate average mood
    # We clean the activity strings first
    df_act = df_filtered.copy()
    df_act['activities'] = df_act['activities'].str.split(' | ')
    df_exploded = df_act.explode('activities')
    
    # Clean up any extra spaces
    df_exploded['activities'] = df_exploded['activities'].str.strip()
    # Remove 'No Entry' or empty strings from the visualization
    df_exploded = df_exploded[~df_exploded['activities'].isin(['No Entry', 'None', '|', ''])]
    
    avg_mood_act = df_exploded.groupby('activities')['Mood_Score'].mean().sort_values(ascending=False).reset_index()

    fig_bar = px.bar(
        avg_mood_act, 
        x='activities', 
        y='Mood_Score', 
        color='Mood_Score',
        title="What activities boost your mood most?",
        color_continuous_scale='Turbo'
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with act_col2:
    st.markdown("#### **Insights & Observations**")
    if not avg_mood_act.empty:
        best_act = avg_mood_act.iloc[0]['activities']
        st.success(f"**Top Mood Booster:** Your data shows that **{best_act}** consistently results in your highest mood scores.")
    
    st.info("""
    **Developer Note:** This analysis uses an 'exploded' dataset to isolate individual habits from combined logs, allowing for granular lifestyle analysis.
    """)

# 10. Footer
st.caption(f"FitSync v2.0 | Processing {len(df_filtered)} data points for this view.")