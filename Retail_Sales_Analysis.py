import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("Retail_Sales_Data.csv")
df['Date'] = pd.to_datetime(df['Date'])

# Monthly Sales Trend
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()
monthly_sales.plot(kind='bar', figsize=(10,5), title="Monthly Sales Trend")
plt.ylabel("Sales Amount")
plt.show()

# Top Products
top_products = df.groupby('Product')['Sales'].sum().sort_values(ascending=False)
top_products.plot(kind='bar', title="Top-Selling Products")
plt.ylabel("Total Sales")
plt.show()

# Region-wise Profit
region_profit = df.groupby('Region')['Profit'].mean()
region_profit.plot(kind='bar', color='orange', title="Average Profit by Region")
plt.ylabel("Average Profit")
plt.show()
