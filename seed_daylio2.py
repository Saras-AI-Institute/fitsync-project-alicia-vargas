import pandas as pd
import random
import numpy as np

def generate_correlated_daylio():
    file_path = "data/health_data.csv"
    
    try:
        # 1. Load your specific health data
        health_df = pd.read_csv(file_path)
        
        # 2. Clean the Data
        # Convert Date to string and handle the "Steps" column
        health_df['Date'] = pd.to_datetime(health_df['Date']).dt.strftime('%Y-%m-%d')
        
        # Convert Steps to numbers. 'coerce' turns blanks into NaN, then we fill with 0.
        health_df['Steps'] = pd.to_numeric(health_df['Steps'], errors='coerce').fillna(0)
        
    except Exception as e:
        print(f"❌ Error: Could not read {file_path}. Make sure the file exists and has 'Date' and 'Steps' columns.")
        print(f"Specific Error: {e}")
        return

    moods = []
    activities = []

    # 3. Correlation Logic Loop
    for index, row in health_df.iterrows():
        step_count = row['Steps']
        
        # Logic: Using your specific 'Steps' column to decide the mood
        if step_count > 9000:
            moods.append("rad")
            activities.append("Productive|Exercise")
        elif step_count > 5000:
            moods.append("good")
            activities.append("Work|Walk")
        elif step_count > 0:
            moods.append("meh")
            activities.append("Rest|Gaming")
        else:
            # This handles the days where steps are 0 or missing
            moods.append("bad")
            activities.append("Sick|Stayed in Bed")

    # 4. Create the Daylio-style output
    # Daylio format: full_date, date, weekday, mood, activities, note
    daylio_df = pd.DataFrame({
        "full_date": health_df['Date'],
        "date": health_df['Date'],
        "weekday": pd.to_datetime(health_df['Date']).dt.strftime('%A'),
        "mood": moods,
        "activities": activities,
        "note": ["Synthetic correlation based on health_data.csv" for _ in range(len(health_df))]
    })

    # 5. Save the result
    output_name = "data/test_mood_correlated.csv"
    daylio_df.to_csv(output_name, index=False)
    
    print(f"✅ Success! Generated {len(daylio_df)} rows.")
    print(f"📊 High steps (>9k) = 'rad', Low steps = 'meh', Missing steps = 'bad'.")
    print(f"📂 Created: {output_name}")

if __name__ == "__main__":
    generate_correlated_daylio()