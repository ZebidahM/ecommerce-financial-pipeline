import pandas as pd
import glob # This library helps find files that match a pattern

def transform_data():
    # 1. FIND ALL YEARLY FILES
    # This looks for any CSV file in the data folder
    all_files = glob.glob("data/Year*.csv")
    print(f"Found {len(all_files)} files: {all_files}")

    # 2. COMBINE FILES (The "Challenge" from the job post)
    li = []
    for filename in all_files:
        print(f"Reading {filename}...")
        # Use memory-efficient dtypes
        df = pd.read_csv(filename, dtype={'Customer ID': 'float32'}, encoding='ISO-8859-1')
        li.append(df)

    # Concatenate everything into one big table
    master_df = pd.concat(li, axis=0, ignore_index=True)
    print(f"Combined total: {len(master_df):,} rows.")

    # 3. CLEANING
    # Remove rows without Customer IDs and handle duplicates
    master_df = master_df.dropna(subset=['Customer ID'])
    master_df = master_df.drop_duplicates()

    # Create Financial KPIs
    master_df['TotalRevenue'] = master_df['Quantity'] * master_df['Price']

    # 4. SAVE FOR POWER BI / SQL
    master_df.to_csv("data/cleaned_master_data.csv", index=False)
    print("✅ Success! 'data/cleaned_master_data.csv' is ready for analysis.")

if __name__ == "__main__":
    transform_data()