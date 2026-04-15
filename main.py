import streamlit as st

# 1. Page Configuration
st.set_page_config(
    layout="wide", 
    page_title="FitSync | Your Health Journey",
    page_icon="🏃"
)

# 2. Hero Section
st.title("🏃 Welcome Back, Alicia")
st.markdown("#### *Data-driven insights to fuel your next session*")
st.write("---")

# 3. User Journey Grid (Simplified for the user)
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📊 My Dashboard")
    st.write("Check your steps, sleep quality, and current recovery status for today.")
    if st.button("Go to My Dashboard", use_container_width=True):
        st.switch_page("pages/1_Dashboard.py")

with col2:
    st.markdown("### 📈 Health Trends")
    st.write("See how your habits have changed over the last month and hit your goals.")
    if st.button("Explore My Trends", use_container_width=True):
        st.switch_page("pages/2_Trends.py")

st.write("---")

# 4. Motivational / Status Section (Consumer Style)
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