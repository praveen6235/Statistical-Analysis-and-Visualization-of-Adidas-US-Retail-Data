import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

data = pd.read_csv("C:\\Users\\prave\\OneDrive\\Desktop\\python12314539\\data.csv")

print(data.head(5))

print(data.tail(5))

print(data.info())

print(data.describe())

plt.title("Total Sales Per Product Using Bar-Chart")

plt.xlabel("Product")

plt.ylabel("Total Sales")

plt.bar(data['Product'], data['Total Sales'], color = 'skyblue')

plt.show()

sales_by_product = data.groupby('Product')['Units Sold'].sum()

plt.figure(figsize = (8, 8))

plt.pie(sales_by_product, labels = sales_by_product, autopct = '%1.1f%%', startangle = 140)

plt.title("Units Solds Percentage Per Product Using Pie-Chart")

plt.axis('equal')

plt.show()

data['Invoice Date'] = pd.to_datetime(data['Invoice Date'], format = '%d-%m-%Y')

data['Month'] = data['Invoice Date'].dt.to_period('M')

monthly_sales = data.groupby('Month')['Total Sales'].sum().reset_index()

monthly_sales['Month'] = monthly_sales['Month'].dt.to_timestamp()

plt.figure(figsize=(14, 7))

sns.lineplot(x = 'Month', y = 'Total Sales', data = monthly_sales, marker = 'o')

plt.title('Monthly Total Sales Trend', fontsize = 18)

plt.xlabel('Month', fontsize = 14)

plt.ylabel('Total Sales', fontsize = 14)

plt.xticks(rotation = 45)

plt.grid(True)

plt.show()

num_data = data.select_dtypes(include = ['float64', 'int64'])

corr = num_data.corr()

plt.figure(figsize = (10, 8))

sns.heatmap(corr, annot = True, cmap = 'coolwarm', fmt = ".2f", linewidth = 0.5)

plt.title("Correlation Heatmap", fontsize = 18)

plt.show()

plt.figure(figsize = (10, 6))

sns.histplot(data['Units Sold'], bins = 30, kde = True, color = 'skyblue')

plt.title(f'Distribution of {"Units Sold"}', fontsize = 18)

plt.xlabel('Units Sold', fontsize = 14)

plt.ylabel('Frequency', fontsize = 14)

plt.grid('True')

plt.show()

plt.figure(figsize =(10, 6))

sns.boxplot(x = data['Total Sales'], color = 'lightgreen')

plt.title('BoxPlot of Total Sales', fontsize = 18)

plt.xlabel('Total Sales', fontsize = 14)

plt.show()

plt.figure(figsize=(10, 6))

plt.scatter(data['Total Sales'], data['Operating Profit'], alpha = 0.5,color = 'blue')

plt.title('Scatter plot of Total Sales vs Operating profit')

plt.xlabel('Total Sales ($)')

plt.ylabel('Operating Sales ($)')

plt.grid(True)

plt.show()
