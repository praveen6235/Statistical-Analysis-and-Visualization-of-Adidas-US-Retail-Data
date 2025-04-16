import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

data = pd.read_csv("C:\\Users\\prave\\OneDrive\\Desktop\\python12314539\\data.csv")

plt.figure(figsize =(10, 6))

sns.boxplot(x = data['Total Sales'], color = 'lightgreen')

plt.title('BoxPlot of Total Sales', fontsize = 18)

plt.xlabel('Total Sales', fontsize = 14)

plt.show()
