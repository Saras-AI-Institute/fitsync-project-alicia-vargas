import streamlit as st
import pandas as pd

def render_global_sidebar():
    with st.sidebar:
        st.header("📥 Data Import")
        
        # Define the widgets INSIDE the function
        up_apple = st.file_uploader("Upload Health", type=["csv"], key="apple_uploader")
        up_daylio = st.file_uploader("Upload Mood", type=["csv"], key="daylio_uploader")
        
        # MOVE THE CHECKS INSIDE HERE (Indented!)
        if up_apple is not None:
            if 'uploaded_apple' not in st.session_state:
                st.session_state['uploaded_apple'] = pd.read_csv(up_apple)
                st.rerun()

        if up_daylio is not None:
            if 'uploaded_daylio' not in st.session_state:
                st.session_state['uploaded_daylio'] = pd.read_csv(up_daylio)
                st.rerun()