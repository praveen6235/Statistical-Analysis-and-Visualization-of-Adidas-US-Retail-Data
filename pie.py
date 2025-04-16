import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

data = pd.read_csv("C:\\Users\\prave\\OneDrive\\Desktop\\python12314539\\data.csv")

sales_by_product = data.groupby('Product')['Units Sold'].sum()

plt.figure(figsize = (8, 8))

plt.pie(sales_by_product, labels = sales_by_product.index, autopct = '%1.1f%%', startangle = 140)

plt.title("Units Solds Percentage Per Product Using Pie-Chart")

plt.axis('equal')

plt.show()
