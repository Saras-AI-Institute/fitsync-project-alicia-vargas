from modules.processor import process_data

# Now Python knows what "process_data" is!
df = process_data()

print("--- Data Successfully Merged ---")
print(df.head())