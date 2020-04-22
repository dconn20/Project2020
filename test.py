import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sys 



iris=pd.read_csv("iris.csv")

iris.columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']

table1 = iris.describe()
print(table1)


byspecies = iris.groupby('species')
table2 = byspecies.describe()
print(table2)


 

