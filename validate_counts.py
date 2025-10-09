import pandas as pd
import snowflake.connector

# Step 1: Count rows in cleaned CSV
df = pd.read_csv("clean_drug_sales.csv")
file_count = len(df)
print("File record count:", file_count)

# Step 2: Connect to Snowflake
conn = snowflake.connector.connect(
    user="SAKET9741",
    password="Teleperformance@1",
    account="TAZMFAA-RU52374",
    warehouse="COMPUTE_WH",
    role="ACCOUNTADMIN",
    database="DRUG_ETL",
    schema="PUBLIC"
)

cur = conn.cursor()

# Step 3: Query Snowflake record count
cur.execute("SELECT COUNT(*) FROM DRUG_SALES;")
snowflake_count = cur.fetchone()[0]
print("Snowflake record count:", snowflake_count)

# Step 4: Compare
if file_count == snowflake_count:
    print("✅ Validation successful! File and Snowflake counts match.")
else:
    print("⚠️ Validation failed! Counts do not match.")

cur.close()
conn.close()
