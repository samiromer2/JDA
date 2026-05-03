import pandas as pd

df = pd.read_csv("data.csv")
print(df.head())


#clean data 
df = df.dropna()
# convert date
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

df["month"] = df["InvoiceDate"].dt.month
df["profit"] = df["UnitPrice"] * df["Quantity"]


top_products = df.groupby("StockCode")["profit"].sum().sort_values(ascending=False)
print(top_products.head())

region_sales = df.groupby("Country")["profit"].sum()
print(region_sales.head())

monthly_sales = df.groupby("month")["profit"].sum()
print(monthly_sales.head())


import matplotlib.pyplot as plt

top_products.head(5).plot(kind="bar")
plt.title("Top 5 Products by Revenue")
plt.show()

monthly_sales.plot(kind="line")
plt.title("Monthly Revenue Trend")
plt.show()