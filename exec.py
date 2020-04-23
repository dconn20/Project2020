import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

iris=pd.read_csv("iris.csv")

iris.columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']

# Violinplot

sns.set(style="whitegrid", palette="muted", rc={'figure.figsize':(11.7,8.27)})

sns.violinplot(x="species", y="petal_length", palette="muted", data=iris)
plt.show()

sns.violinplot(x="species", y="petal_width", palette="muted", data=iris)
plt.show()

sns.violinplot(x="species", y="sepal_length", palette="muted", data=iris)
plt.show()

sns.violinplot(x="species", y="sepal_width", palette="muted", data=iris)
plt.show()