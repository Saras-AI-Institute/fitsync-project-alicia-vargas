import pandas as pd
import streamlit as st

def calculate_recovery_score(df):
    """Business logic to calculate daily physical readiness."""
    # Ensure columns are numeric before calculating
    df['Steps'] = pd.to_numeric(df['Steps'], errors='coerce').fillna(0)
    df['Sleep_Hours'] = pd.to_numeric(df['Sleep_Hours'], errors='coerce').fillna(7)
    df['Heart_Rate_bpm'] = pd.to_numeric(df['Heart_Rate_bpm'], errors='coerce').fillna(70)

    df['Recovery_Score'] = 50
    df.loc[df['Sleep_Hours'] >= 7, 'Recovery_Score'] += 20
    df.loc[df['Sleep_Hours'] < 6, 'Recovery_Score'] -= 20
    
    # Mathematical factors for HR and Steps
    df['Recovery_Score'] += (95 - df['Heart_Rate_bpm']) / 45 * 20
    df['Recovery_Score'] += (df['Steps'] - 4000) / 12000 * 10
    
    df['Recovery_Score'] = df['Recovery_Score'].clip(lower=0, upper=100)
    return df

def process_data():
    """
    MASTER PIPELINE: 
    Checks for uploads, cleans data, and merges into one final table.
    """
    # 1. SELECT DATA SOURCE
    if 'uploaded_apple' in st.session_state and 'uploaded_daylio' in st.session_state:
        health_df = st.session_state['uploaded_apple']
        mood_df_raw = st.session_state['uploaded_daylio']
        st.sidebar.success("✅ Using your uploaded files!")
    else:
        try:
            health_df = pd.read_csv('data/health_data.csv')
            mood_df_raw = pd.read_csv('data/daylio.csv')
            st.sidebar.info("ℹ️ Using local demo data")
        except FileNotFoundError:
            st.error("No data found. Please upload files.")
            return None

    # 2. CLEAN HEALTH DATA
    health_df['Date'] = pd.to_datetime(health_df['Date'])
    health_df = calculate_recovery_score(health_df)

    # 3. CLEAN MOOD DATA
    # Handle different possible column names for date
    mood_date_col = 'date' if 'date' in mood_df_raw.columns else 'Date'
    if 'full_date' in mood_df_raw.columns: mood_date_col = 'full_date'
    
    mood_df_raw['Date'] = pd.to_datetime(mood_df_raw[mood_date_col])
    mood_df_raw['mood'] = mood_df_raw['mood'].ffill().fillna('meh')
    mood_df_raw['activities'] = mood_df_raw['activities'].fillna('No Entry')

    mood_map = {"rad": 10, "good": 8, "meh": 5, "bad": 3, "awful": 1}
    mood_df_raw['Mood_Score'] = mood_df_raw['mood'].map(mood_map)

    # 4. THE MERGE
    # We define final_df here so it's guaranteed to exist for the return
    final_df = pd.merge(
        health_df, 
        mood_df_raw[['Date', 'Mood_Score', 'activities']], 
        on='Date', 
        how='inner'
    )

    final_df = final_df.round(2)

    return final_df