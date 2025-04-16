import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

data = pd.read_csv("C:\\Users\\prave\\OneDrive\\Desktop\\python12314539\\data.csv")

num_data = data.select_dtypes(include = ['float64', 'int64'])

corr = num_data.corr()

plt.figure(figsize = (10, 8))

sns.heatmap(corr, annot = True, cmap = 'coolwarm', fmt = ".2f", linewidth = 0.5)

plt.title("Correlation Heatmap", fontsize = 18)

plt.show()
