import pandas as pd
from sqlalchemy import create_engine

# Load cleaned data
df = pd.read_csv("../dataset/cleaned_superstore.csv")

# Create SQLite DB
engine = create_engine("sqlite:///../dataset/superstore.db")

# Load table
df.to_sql("sales_data", con=engine, if_exists="replace", index=False)

print("DATA LOADED TO SQL SUCCESSFULLY")