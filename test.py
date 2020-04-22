import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sys 

sys.stdout = open("summary.txt", "w")

iris=pd.read_csv("iris.csv")

iris.columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']

iris.shape

iris['species'].unique()

#sys.stdout = open("summary.txt", "w")
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

byspecies = iris.groupby('species')
table2 = byspecies.describe()
pd.set_option('display.max_columns', None)
print(table2)


sys.stdout.close()


 

