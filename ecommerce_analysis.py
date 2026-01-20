import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/ecommerce_sales.csv")
df['order_date'] = pd.to_datetime(df['order_date'])
df['total_sales'] = df['price'] * df['quantity']

print("\n--- Business KPIs ---")
print("Total Revenue:", df['total_sales'].sum())
print("Total Orders:", df['order_id'].nunique())
print("Average Order Value:", df['total_sales'].mean())

product_sales = df.groupby('product')['total_sales'].sum().sort_values(ascending=False)
category_sales = df.groupby('category')['total_sales'].sum()
df['month'] = df['order_date'].dt.to_period('M')
monthly_sales = df.groupby('month')['total_sales'].sum()

product_sales.plot(kind='bar', title='Revenue by Product')
plt.show()

category_sales.plot(kind='pie', autopct='%1.1f%%', title='Category Revenue Share')
plt.show()

monthly_sales.plot(kind='line', marker='o', title='Monthly Sales Trend')
plt.show()
