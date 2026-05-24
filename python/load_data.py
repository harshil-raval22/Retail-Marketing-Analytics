import pandas as pd

# Load dataset
df = pd.read_csv("../dataset/superstore.csv", encoding="latin1")

# First 5 rows
print("FIRST 5 ROWS")
print(df.head())

print("\nDATA SHAPE")
print(df.shape)

print("\nCOLUMNS")
print(df.columns)

print("\nDATA TYPES")
print(df.dtypes)