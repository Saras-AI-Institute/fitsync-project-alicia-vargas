import pandas as pd
import numpy as np
from datetime import datetime, timedelta

num_days = 730 
end_date = datetime.now()
start_date = end_date - timedelta(days=num_days)

mood_options = ["rad", "good", "meh", "bad", "awful"]
activities_list = ["gym", "friends", "yoga", "work", "cooking"]

data = []

for i in range(num_days):
    current_date = start_date + timedelta(days=i)
    
    # Standard mood generation
    mood = np.random.choice(mood_options)
    acts = " | ".join(np.random.choice(activities_list, size=2, replace=False))
    
    # --- THE CHAOS STEP ---
    # 10% chance to make the mood MISSING (NaN)
    if np.random.random() < 0.10:
        mood = np.nan
        
    # 10% chance to make the activities MISSING
    if np.random.random() < 0.10:
        acts = np.nan
    # ----------------------

    data.append({
        "date": current_date.strftime("%Y-%m-%d"),
        "mood": mood,
        "activities": acts
    })

df = pd.DataFrame(data)
df.to_csv('daylio.csv', index=False)
print("✅ Success! Generated 2 years of MESSY data.")