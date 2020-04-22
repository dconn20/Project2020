import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas.testing as tm
import sys 


iris = pd.read_csv("iris.csv")



# Summary
sys.stdout = open("summary.txt", "w")

iris.columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']

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

byspecies = iris.groupby('species')
table2 = byspecies.describe()
pd.set_option('display.max_columns', None)
print(table2)


sys.stdout.close()




# Pairplots
sns.set_style("whitegrid")
sns.pairplot(iris, hue ="species",height=3)
plt.savefig("pairplot.png")
plt.show()
#plt.savefig("pairplot.jpeg")



# Histogram
plt.style.use('ggplot')
plt.hist(iris['sepal_length'])
plt.xlabel('sepal_length')
plt.show()
plt.hist(iris['sepal_width'])
plt.xlabel('sepal_width')
plt.show()
plt.hist(iris['petal_length'])
plt.xlabel('petal_length')
plt.show()
plt.hist(iris['petal_width'])
plt.xlabel('petal_width')
plt.show()



