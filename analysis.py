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

summary1 = iris.describe()
print(summary1)

byspecies = iris.groupby('species')
summary2 = byspecies.describe()
pd.set_option('display.max_columns', None)
print(summary2)

sys.stdout.close()



# Pairplots
sns.set_style("whitegrid")
sns.pairplot(iris, hue ="species",height=3)
plt.savefig("pairplot.png")
plt.show()



# Histogram
plt.style.use('ggplot')
plt.hist(iris['sepal_length'])
plt.xlabel('sepal_length')
plt.savefig("sepal_length.hist.png")
plt.show()
plt.hist(iris['sepal_width'])
plt.xlabel('sepal_width')
plt.savefig('sepal_width.hist.png')
plt.show()
plt.hist(iris['petal_length'])
plt.xlabel('petal_length')
plt.savefig('petal_length.hist.png')
plt.show()
plt.hist(iris['petal_width'])
plt.xlabel('petal_width')
plt.savefig('petal_width.hist.png')
plt.show()



