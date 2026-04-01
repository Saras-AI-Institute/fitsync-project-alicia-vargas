import pandas as pd

def main():
    # Load the health_data.csv file
    data = pd.read_csv('data/health_data.csv') 
    
    # Print the first 5 rows
    print("First 5 rows:")
    print(data.head())
    
    # Print the number of missing values in each column
    print("\nMissing values in each column:")
    print(data.isnull().sum()) #adding up the null

if __name__ == "__main__":
    main()