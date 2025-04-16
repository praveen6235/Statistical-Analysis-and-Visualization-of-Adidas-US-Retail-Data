import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

data = pd.read_csv("C:\\Users\\prave\\OneDrive\\Desktop\\python12314539\\data.csv")

plt.figure(figsize=(10, 6))

plt.scatter(data['Total Sales'], data['Operating Profit'], alpha = 0.5,color = 'blue')

plt.title('Scatter plot of Total Sales vs Operating profit')

plt.xlabel('Total Sales ($)')

plt.ylabel('Operating Sales ($)')

plt.grid(True)

plt.show()
