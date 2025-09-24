import pandas as pd

# Step 1: Load data
df = pd.read_csv("Sample_Pharmaceutical_Drug_Sales.csv")

# Step 2: Check the columns
print("Columns in CSV:", df.columns)

# Step 3: Clean column names
df.columns = df.columns.str.lower().str.strip()

# Step 4: Remove duplicates
df = df.drop_duplicates()

# Step 5: Remove rows with missing values
df = df.dropna()

# Step 6: Save the cleaned file
df.to_csv("clean_drug_sales.csv", index=False)

print("✅ Cleaned data saved to 'clean_drug_sales.csv'")
print(df.head())
