import pandas as pd

def load_data():
    """Loads and cleans the physical health data."""
    df = pd.read_csv('data/health_data.csv')

    # Handle missing numerical values with medians/constants
    df['Steps'] = df['Steps'].fillna(df['Steps'].median())
    df['Sleep_Hours'] = df['Sleep_Hours'].fillna(7.0)
    df['Heart_Rate_bpm'] = df['Heart_Rate_bpm'].fillna(68)

    # Convert the 'Date' column to datetime objects
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def load_mood_data():
    """Loads and cleans the categorical mental health data (Daylio)."""
    df = pd.read_csv('data/daylio.csv')
    
    # 1. Handle missing Mood strings using Forward Fill (ffill)
    # This carries the previous day's mood forward into gaps
    df['mood'] = df['mood'].ffill()
    df['mood'] = df['mood'].fillna('meh') # Backup for the first row

    # 2. Handle missing activities
    df['activities'] = df['activities'].fillna('No Entry')

    # 3. Transform categories to numerical scores
    mood_map = {"rad": 10, "good": 8, "meh": 5, "bad": 3, "awful": 1}
    df['Mood_Score'] = df['mood'].map(mood_map)

    # 4. Standardize column names for the Join
    df['Date'] = pd.to_datetime(df['date'])
    
    return df[['Date', 'Mood_Score', 'activities']]

def calculate_recovery_score(df):
    """Business logic to calculate daily physical readiness."""
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
    Integrates multiple data sources into a single unified intelligence table.
    """
    # 1. Get Physical Data
    health_df = load_data()
    health_df = calculate_recovery_score(health_df)

    # 2. Get Mental Data
    mood_df = load_mood_data()

    # 3. THE MERGE (Inner Join)
    # This aligns the rows so that May 1st Health matches May 1st Mood.
    final_df = pd.merge(health_df, mood_df, on='Date', how='inner')

    final_df = final_df.round(2) # Keeps everything to 2 decimal places

    return final_df