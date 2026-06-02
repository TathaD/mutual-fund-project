import pandas as pd
import os

# Dataset folder path
data_path = "data/raw"

# Get all CSV files
csv_files = [file for file in os.listdir(data_path) if file.endswith(".csv")]

print(f"Found {len(csv_files)} CSV files")

# Loop through files
for file in csv_files:

    print("\n" + "="*60)
    print(f"Loading File: {file}")

    file_path = os.path.join(data_path, file)

    try:
        # Read CSV
        df = pd.read_csv(file_path)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nHead:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error loading {file}")
        print(e)