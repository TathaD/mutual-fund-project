import pandas as pd
from pathlib import Path

raw_path = Path("data/raw")
processed_path = Path("data/processed")

processed_path.mkdir(exist_ok=True)

for file in raw_path.glob("*.csv"):

    print(f"Cleaning {file.name}")

    df = pd.read_csv(file)

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove extra spaces from text columns
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].astype(str).str.strip()

    output_file = processed_path / f"{file.stem}_clean.csv"

    df.to_csv(output_file, index=False)

    print(f"Saved -> {output_file}")