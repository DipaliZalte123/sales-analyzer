import pandas as pd
import matplotlib.pyplot as plt

# Load sales data
df = pd.read_csv('sales_data.csv')
print(df)

# Task 1: Find total sales
total = df['Sales'].sum()
print(f"Total Sales: {total}")

# Task 2: Find best month
best_month = df.loc[df['Sales'].idxmax()]
print(f"Best Month: {best_month['Month']} - {best_month['Sales']}")

# Task 3: Make bar chart
plt.bar(df['Month'], df['Sales'])
plt.title('Monthly Sales')
plt.savefig('sales_graph.png')
print("Graph saved!")