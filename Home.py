import streamlit as st
import pandas as pd
from modules.interface import render_global_sidebar
from modules.processor import process_data

# 1. THE ONLY PAGE CONFIG (Must be at the very top)
st.set_page_config(
    layout="centered", 
    page_title="FitSync | Peak Performance",
    page_icon="🌈"
)

# 2. Sidebar Activation (Global for all pages)
render_global_sidebar()

# 3. Rainbow Header Styling
st.markdown("""
    <div style="height: 8px; background: linear-gradient(to right, #ff4b4b, #ff9f4b, #f4ff4b, #4bff5a, #4b9fff, #7a4bff); border-radius: 10px; margin-bottom: 30px;"></div>
    """, unsafe_allow_html=True)

# 4. Hero Section
st.title("FitSync.")
st.markdown("""
    ### *Where your body meets your mind.*
    
    FitSync is a holistic health intelligence platform designed to bridge the gap 
    between physical recovery and emotional well-being. By merging biometrics 
    with daily reflections, we help you find your unique rhythm for peak performance.
    """)

st.write("---")

# 5. Feature Columns
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### 🏃 Physical")
    st.caption("Automated tracking of steps, sleep, and heart rate variability.")

with col2:
    st.markdown("#### 🧠 Mental")
    st.caption("Deep integration with your daily reflections and mood cycles.")

with col3:
    st.markdown("#### 📈 Intelligence")
    st.caption("Proprietary Recovery Scores built on multi-source data fusion.")

st.write("<br><br>", unsafe_allow_html=True)

# 6. Call to Action
st.info("Ready to see your insights? Navigate to the **Dashboard** or **Trends** in the sidebar.")

# 7. Data Engine Preview
try:
    # This calls your processor. If the user uploaded files via the sidebar,
    # ensure your processor is updated to handle session_state data!
    df = process_data()
    st.divider()
    
    # Progress tracker
    progress_val = (len(df) / 730)
    st.write(f"**Alicia's Journey:** {len(df)} days logged")
    st.progress(min(progress_val, 1.0))
    
except Exception as e:
    st.error("Engine Offline: Ensure your CSV files are in the /data folder or uploaded via the sidebar.")

# 8. Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("FitSync Health v2.0 | Built with Python for SarasAI")