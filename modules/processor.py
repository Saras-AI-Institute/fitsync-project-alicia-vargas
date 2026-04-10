import pandas as pd


def load_data():
    # Read the CSV file
    df = pd.read_csv('data/health_data.csv')

    # Handle missing values
    # Fill missing 'Steps' with median value
    df['Steps'].fillna(df['Steps'].median(), inplace=True)

    # Fill missing 'Sleep_Hours' with 7.0
    df['Sleep_Hours'].fillna(7.0, inplace=True)

    # Fill missing 'Heart_Rate_bpm' with 68
    df['Heart_Rate_bpm'].fillna(68, inplace=True)

    # Fill other columns with their median values
    # Exclude non-numeric columns for median calculation
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    for col in numeric_cols:
        if col not in ['Steps', 'Sleep_Hours', 'Heart_Rate_bpm']:
            df[col].fillna(df[col].median(), inplace=True)

    # Convert the 'Date' column to datetime objects
    df['Date'] = pd.to_datetime(df['Date'])

    return df


def calculate_recovery_score(df):
    """
    Calculate the recovery score for each row in the DataFrame based on sleep hours, heart rate, and steps.
    Adds a new column 'Recovery_Score' to the DataFrame.
    """
    # Initialize recovery score with base value of 50
    df['Recovery_Score'] = 50

    # Adjust score based on Sleep_Hours
    df.loc[df['Sleep_Hours'] >= 7, 'Recovery_Score'] += 20  # Good Sleep
    df.loc[df['Sleep_Hours'] < 6, 'Recovery_Score'] -= 20  # Poor Sleep

    # Adjust score based on Heart_Rate_bpm
    heart_rate_factor = (95 - df['Heart_Rate_bpm']) / 45 * 20
    df['Recovery_Score'] += heart_rate_factor

    # Adjust score based on Steps
    steps_factor = (df['Steps'] - 4000) / 12000 * 10
    df['Recovery_Score'] += steps_factor

    # Ensure Recovery_Score stays within 0 to 100
    df['Recovery_Score'] = df['Recovery_Score'].clip(lower=0, upper=100)

    return df

def process_data():
    """
    Main entry point for data processing.
    Loads the data, calculates scores, and returns the final DataFrame.
    """
    # 1. Call load_data() to get the cleaned DataFrame
    df = load_data()

    # 2. Call calculate_recovery_score() to add the Recovery Score
    df = calculate_recovery_score(df)

    # 3. Return the final processed DataFrame
    return df