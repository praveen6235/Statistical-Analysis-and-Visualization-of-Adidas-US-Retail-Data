import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

data = pd.read_csv("C:\\Users\\prave\\OneDrive\\Desktop\\python12314539\\data.csv")

# Using Matplotlib, pandas, seaborn lib to plot the bar graph.

plt.title("Total Sales Per Product Using Bar-Chart")

plt.xlabel("Product") # x-axis

plt.ylabel("Total Sales") # y-axis

plt.bar(data['Product'], data['Total Sales'], color = 'skyblue')

plt.xticks(rotation=45)

plt.tight_layout()  

plt.show()
