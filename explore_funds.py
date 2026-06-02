import pandas as pd

# Load dataset
fund_master = pd.read_csv("data/raw/01_fund_master.csv")

# Fund houses
print("\nFund Houses:")
print(fund_master['fund_house'].unique())

# Categories
print("\nCategories:")
print(fund_master['category'].unique())

# Sub categories
print("\nSub Categories:")
print(fund_master['sub_category'].unique())

# Risk categories
print("\nRisk Categories:")
print(fund_master['risk_category'].unique())