import requests
import pandas as pd
import os

# Create output folder
os.makedirs("data/raw/live_nav", exist_ok=True)

# Mutual fund scheme codes
funds = {
    "HDFC_Top_100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

# Loop through each fund
for fund_name, scheme_code in funds.items():

    print("\n" + "="*60)
    print(f"Fetching {fund_name}")

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:
        # Send request
        response = requests.get(url)

        # Convert JSON
        data = response.json()

        # Print scheme name
        print("Scheme Name:")
        print(data['meta']['scheme_name'])

        # Convert NAV history to DataFrame
        nav_df = pd.DataFrame(data['data'])

        # Show top rows
        print(nav_df.head())

        # Save CSV
        output_file = f"data/raw/live_nav/{fund_name}.csv"

        nav_df.to_csv(output_file, index=False)

        print(f"Saved: {output_file}")

    except Exception as e:
        print(f"Error fetching {fund_name}")
        print(e)