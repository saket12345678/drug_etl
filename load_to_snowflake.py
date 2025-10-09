import pandas as pd
from snowflake.connector import connect
from snowflake.connector.pandas_tools import write_pandas

# -----------------------------
# Step 1: Load CSV into DataFrame
# -----------------------------
df = pd.read_csv("clean_drug_sales.csv")  # replace with your file path

# -----------------------------
# Step 2: Clean column names
# -----------------------------
# Remove spaces, lowercase/uppercase, replace special characters
df.columns = df.columns.str.strip().str.upper().str.replace(' ', '_')

# -----------------------------
# Step 3: Remove duplicates & missing values
# -----------------------------
df = df.drop_duplicates()
df = df.dropna()  # optional: you can also handle missing values differently

# -----------------------------
# Step 4: Connect to Snowflake
# -----------------------------
conn = connect(
    user="SAKET9741",
    password="Teleperformance@1",
    account="TAZMFAA-RU52374",
    warehouse="COMPUTE_WH",
    role="ACCOUNTADMIN",
    database="DRUG_ETL",
    schema="PUBLIC"
)

# -----------------------------
# Step 5: Create/Replace Table
# -----------------------------
# Dynamically generate SQL from DataFrame columns
columns_sql = ",\n".join([f"{col} STRING" for col in df.columns])
create_table_sql = f"CREATE OR REPLACE TABLE DRUG_SALES (\n{columns_sql}\n)"
conn.cursor().execute(create_table_sql)
print("✅ Table created or replaced successfully in Snowflake.")

# -----------------------------
# Step 6: Write DataFrame to Snowflake
# -----------------------------
success, nchunks, nrows, _ = write_pandas(conn, df, "DRUG_SALES")

if success:
    print(f"✅ Data loaded successfully! Rows inserted: {nrows} in {nchunks} chunks.")
else:
    print("❌ Data load failed.")

# -----------------------------
# Step 7: Close connection
# -----------------------------
conn.close()
