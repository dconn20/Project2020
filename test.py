import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

iris=pd.read_csv("iris.csv")

iris.columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']

#you can specific the number to show here
iris.head(10)

iris.shape

iris['species'].unique()
print(iris.groupby('species').size())

iris.min()
iris.max()
iris.mean()
iris.median()
iris.std()

summary = iris.describe()
summary = summary.transpose()
summary.head()
print(summary)