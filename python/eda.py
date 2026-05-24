import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("../dataset/cleaned_superstore.csv")

print("EDA STARTED")
print(df.head())

# Convert dates
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# -------------------------
# 1. Monthly Sales Trend
# -------------------------
monthly_sales = df.groupby(
    df["Order_Date"].dt.to_period("M")
)["Sales"].sum()

plt.figure(figsize=(10,5))
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# -------------------------
# 2. Monthly Profit Trend
# -------------------------
monthly_profit = df.groupby(
    df["Order_Date"].dt.to_period("M")
)["Profit"].sum()

plt.figure(figsize=(10,5))
monthly_profit.plot()
plt.title("Monthly Profit Trend")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()

# -------------------------
# 3. Top 10 Products by Sales
# -------------------------
top_products = (
    df.groupby("Product_Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,6))
top_products.plot(kind="bar")
plt.title("Top 10 Products by Sales")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# -------------------------
# 4. Region-wise Sales
# -------------------------
region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8,5))
region_sales.plot(kind="bar")
plt.title("Region Wise Sales")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# -------------------------
# 5. Category Sales
# -------------------------
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")
plt.title("Category Wise Sales")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# -------------------------
# 6. Discount vs Profit
# -------------------------
plt.figure(figsize=(8,5))
plt.scatter(df["Discount"], df["Profit"])
plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()

print("EDA COMPLETED")