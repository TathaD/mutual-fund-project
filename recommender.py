import pandas as pd
import numpy as np

# Load datasets
fund_master = pd.read_csv("data/processed/01_fund_master_clean.csv")
nav_history = pd.read_csv("data/processed/02_nav_history_clean.csv")

# Convert date
nav_history["date"] = pd.to_datetime(nav_history["date"])

# Sort data
nav_history = nav_history.sort_values(["amfi_code", "date"])

# Calculate daily returns
nav_history["daily_return"] = (
    nav_history.groupby("amfi_code")["nav"]
    .pct_change()
)

# Calculate Sharpe Ratio
sharpe_list = []

for fund in nav_history["amfi_code"].unique():

    returns = nav_history[
        nav_history["amfi_code"] == fund
    ]["daily_return"].dropna()

    if len(returns) > 30:

        sharpe = (
            returns.mean() /
            returns.std()
        ) * np.sqrt(252)

        sharpe_list.append(
            [fund, sharpe]
        )

# Create DataFrame
sharpe_df = pd.DataFrame(
    sharpe_list,
    columns=["amfi_code", "sharpe_ratio"]
)

# Merge with fund details
funds = fund_master.merge(
    sharpe_df,
    on="amfi_code"
)

# Ask user
risk = input(
    "Enter Risk (Low / Moderate / High): "
)

# Filter by risk
recommend = funds[
    funds["risk_category"].str.lower()
    ==
    risk.lower()
]

# Sort by Sharpe Ratio
recommend = recommend.sort_values(
    "sharpe_ratio",
    ascending=False
)

# Display top 3
print("\nTop 3 Recommended Funds\n")

print(
    recommend[
        [
            "scheme_name",
            "fund_house",
            "risk_category",
            "sharpe_ratio"
        ]
    ].head(3)
)