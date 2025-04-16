import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

data = pd.read_csv("C:\\Users\\prave\\OneDrive\\Desktop\\python12314539\\data.csv")

#Printing the Basic Data Exploration with pandas

print(data.head(5))

print(data.tail(5))

print(data.info())

print(data.describe())

print(data.isnull().sum())

