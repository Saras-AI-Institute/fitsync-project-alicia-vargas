import streamlit as st

# 1. Page Configuration
st.set_page_config(
    layout="wide", 
    page_title="FitSync | Your Health Journey",
    page_icon="🏃"
)
# This creates the sidebar content
with st.sidebar:
    st.header("📲 Data Integration")
    st.write("Upload your exports to sync your health journey.")
    
    # This adds the 'Upload' button to the sidebar
    health_file = st.file_uploader("Upload Health CSV", type="csv")
    mood_file = st.file_uploader("Upload Mood CSV", type="csv")

    st.divider()
    st.caption("Connected to: Apple Health v2.4")
    
# 2. Hero Section
st.title("🏃 Welcome Back, Alicia")
st.markdown("#### *Data-driven insights to fuel your next session*")
st.write("---")

# 3. User Journey Grid
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📊 My Dashboard")
    st.write("Check your steps, sleep quality, and current recovery status.")
    # This creates a link that looks like a button and points to your page
    st.markdown("""
        <a href="/Dashboard" target="_self">
            <div style="display: inline-block; padding: 0.5em 1em; color: white; background-color: #ff4b4b; border-radius: 5px; text-decoration: none; width: 100%; text-align: center;">
                Go to My Dashboard
            </div>
        </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("### 📈 Health Trends")
    st.write("See how your habits have changed over the last month.")
    # This points to the Trends page
    st.markdown("""
        <a href="/Trends" target="_self">
            <div style="display: inline-block; padding: 0.5em 1em; color: white; background-color: #ff4b4b; border-radius: 5px; text-decoration: none; width: 100%; text-align: center;">
                Explore My Trends
            </div>
        </a>
    """, unsafe_allow_html=True)

# 4. Motivational / Status Section
st.markdown("### Today's Focus")
status_col1, status_col2, status_col3 = st.columns(3)

with status_col1:
    st.success("✅ **Data Synced**\n\nYour latest activity is up to date.")

with status_col2:
    st.info("💡 **Daily Tip**\n\nUsers with 8+ hours of sleep see 20% higher recovery scores.")

with status_col3:
    st.warning("⚠️ **Goal Alert**\n\nYou're 2,000 steps away from your daily target!")

# 5. Clean Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("© 2026 FitSync Health | Designed for Peak Performance")