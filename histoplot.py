import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

data = pd.read_csv("C:\\Users\\prave\\OneDrive\\Desktop\\python12314539\\data.csv")

plt.figure(figsize = (10, 6))

sns.histplot(data['Units Sold'], bins = 30, kde = True, color = 'skyblue')

plt.title(f'Distribution of {"Units Sold"}', fontsize = 18)

plt.xlabel('Units Sold', fontsize = 14)

plt.ylabel('Frequency', fontsize = 14)

plt.grid('True')

plt.show()
