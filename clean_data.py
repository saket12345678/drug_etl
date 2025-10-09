import pandas as pd

# Step 1: Load the raw dataset
df = pd.read_csv("Sample_Pharmaceutical_Drug_Sales.csv")

# Step 2: Display initial info
print("Initial shape:", df.shape)
print("Columns:", df.columns.tolist())

# Step 3: Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Step 4: Remove duplicates
df = df.drop_duplicates()

# Step 5: Handle missing values (drop or fill)
df = df.dropna()  # Drop rows with nulls

# Step 6: Check for invalid data types
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].str.strip()

# Step 7: Save the cleaned file
df.to_csv("clean_drug_sales.csv", index=False)

print("✅ Cleaning complete!")
print("Final shape:", df.shape)
