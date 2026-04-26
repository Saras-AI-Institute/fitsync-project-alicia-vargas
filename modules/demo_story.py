# modules/demo_story.py

def apply_demo_logic(df):
    """
    Adjusts synthetic data to create a logical 'story' for demonstrations.
    This creates visible correlations between activities and biometrics.
    """
    # 1. The 'Health' Boost: Yoga and Meditation improve scores
    df.loc[df['activities'].str.contains('yoga|meditation', case=False, na=False), 'Recovery_Score'] += 18
    df.loc[df['activities'].str.contains('yoga|meditation', case=False, na=False), 'Mood_Score'] += 2
    
    # 2. The 'Stress' Tax: Work and Stress lower scores
    df.loc[df['activities'].str.contains('work|stress', case=False, na=False), 'Recovery_Score'] -= 12
    df.loc[df['activities'].str.contains('work|stress', case=False, na=False), 'Heart_Rate_bpm'] += 10
    
    # 3. Physical Intensity: Gym/Running shows high HR
    df.loc[df['activities'].str.contains('gym|running', case=False, na=False), 'Heart_Rate_bpm'] += 20
    
    # Ensure data stays in realistic ranges
    df['Recovery_Score'] = df['Recovery_Score'].clip(20, 100)
    df['Mood_Score'] = df['Mood_Score'].clip(1, 10)
    
    return df
# Inside modules/demo_story.py

