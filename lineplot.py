import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

data = pd.read_csv("C:\\Users\\prave\\OneDrive\\Desktop\\python12314539\\data.csv")

#Using US Adidas Sales Dataset, I Created a Line-Chart

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
