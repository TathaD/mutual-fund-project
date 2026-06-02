import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Unique AMFI codes
master_codes = set(fund_master['amfi_code'])
nav_codes = set(nav_history['amfi_code'])

# Missing codes
missing_codes = master_codes - nav_codes

# Output
print("\nMissing AMFI Codes:")
print(missing_codes)

print(f"\nTotal Missing Codes: {len(missing_codes)}")

# Validation summary
if len(missing_codes) == 0:
    print("\nAll AMFI codes from fund_master exist in nav_history.")
else:
    print("\nSome AMFI codes are missing in nav_history.")