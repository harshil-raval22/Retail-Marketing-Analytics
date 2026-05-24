import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///../dataset/superstore.db")

# Query 1: Region with highest sales
query1 = """
SELECT Region, SUM(Sales) AS Total_Sales
FROM sales_data
GROUP BY Region
ORDER BY Total_Sales DESC;
"""

result1 = pd.read_sql(query1, engine)
print("\nREGION SALES:")
print(result1)


# Query 2: Top 10 profitable products
query2 = """
SELECT Product_Name, SUM(Profit) AS Total_Profit
FROM sales_data
GROUP BY Product_Name
ORDER BY Total_Profit DESC
LIMIT 10;
"""

result2 = pd.read_sql(query2, engine)
print("\nTOP PROFIT PRODUCTS:")
print(result2)


# Query 3: Category-wise sales
query3 = """
SELECT Category, SUM(Sales) AS Total_Sales
FROM sales_data
GROUP BY Category
ORDER BY Total_Sales DESC;
"""

result3 = pd.read_sql(query3, engine)
print("\nCATEGORY SALES:")
print(result3)


# Query 4: Loss-making products
query4 = """
SELECT Product_Name, SUM(Profit) AS Total_Profit
FROM sales_data
GROUP BY Product_Name
HAVING Total_Profit < 0
ORDER BY Total_Profit ASC
LIMIT 10;
"""

result4 = pd.read_sql(query4, engine)
print("\nLOSS MAKING PRODUCTS:")
print(result4)


# Query 5: Monthly sales trend
query5 = """
SELECT
    strftime('%Y-%m', Order_Date) AS Month,
    SUM(Sales) AS Monthly_Sales
FROM sales_data
GROUP BY Month
ORDER BY Month;
"""

result5 = pd.read_sql(query5, engine)
print("\nMONTHLY SALES:")
print(result5)

print("\nSQL ANALYSIS COMPLETED")