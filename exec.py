import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

iris=pd.read_csv("iris.csv")

iris.columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']





data = pd.read_csv('iris.csv', sep=',', header = None, names = ['sepalLength', 'sepalWidth', 'petalLength', 'petalWidth', 'species'])
print(data.head())
print("The data frame has (rows, columns):", (data.shape))
print(data.dtypes)

data['species'] = data['species'].astype('category')
print(data.dtypes)

table1 = data.describe()
print(table1)


byspecies = data.groupby('species')
table2 = byspecies.describe()
print(table2)
