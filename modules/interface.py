import streamlit as st
import pandas as pd

def render_global_sidebar():
    with st.sidebar:
        st.header("📥 Data Import")
        
        # Two upload slots
        up_apple = st.file_uploader("Upload Apple Health (CSV)", type=["csv"], key="apple_upload")
        up_daylio = st.file_uploader("Upload Daylio (CSV)", type=["csv"], key="daylio_upload")
        
        # Logic to save to 'Memory'
        if up_apple:
            st.session_state['raw_apple'] = pd.read_csv(up_apple)
        if up_daylio:
            st.session_state['raw_daylio'] = pd.read_csv(up_daylio)
            
        if st.button("Reset to Demo Data"):
            for key in ['raw_apple', 'raw_daylio']:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()