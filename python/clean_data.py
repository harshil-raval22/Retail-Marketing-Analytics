import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("../dataset/superstore.csv", encoding="latin1")

print("DATA LOADED SUCCESSFULLY")
print(df.head())

# Original shape
print("\nORIGINAL SHAPE:")
print(df.shape)

# Missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())

# Duplicates
print("\nDUPLICATES:")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Clean columns
df.columns = df.columns.str.strip()
df.columns = df.columns.str.replace(" ", "_")
print(df.columns.tolist())

print("\nCLEANED COLUMNS:")
print(df.columns)

# Convert dates
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    format="%d-%m-%Y",
    errors="coerce"
)

df["Ship_Date"] = pd.to_datetime(
    df["Ship_Date"],
    format="%d-%m-%Y",
    errors="coerce"
)

# Remove rows where date conversion failed
df = df.dropna(subset=["Order_Date", "Ship_Date"])

# Remove invalid rows
df = df[df["Sales"] > 0]
df = df[df["Quantity"] > 0]

# Clean text columns
text_cols = [
    "Customer_Name",
    "Segment",
    "Country",
    "City",
    "State",
    "Region",
    "Category",
    "Product_Name"
]

# Only clean columns that actually exist
for col in text_cols:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip()

# Final shape
print("\nFINAL CLEANED SHAPE:")
print(df.shape)

# Save cleaned file
df.to_csv("../dataset/cleaned_superstore.csv", index=False)

print("\nCLEANED FILE SAVED SUCCESSFULLY")