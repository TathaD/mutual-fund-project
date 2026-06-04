import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

processed_path = Path("data/processed")

for file in processed_path.glob("*.csv"):

    table_name = file.stem.replace("_clean", "")

    print(f"Loading {file.name}")

    df = pd.read_csv(file)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"Loaded into table: {table_name}")

print("Database Created Successfully")