import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

iris=pd.read_csv("iris.csv")

iris.columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']


#plt.scatter(iris['sepal_length'],['sepal_width'])
#plt.title('Scatter plot')
#plt.xlabel('petal_length')
#plt.ylabel('petal_width')
#plt.show()

iris = sns.load_dataset('iris')
sns.lmplot( x="petal_length" , y="petal_width" , data=iris, fit_reg=False, hue='species' , legend=False)
plt.legend(loc='lower right')
plt.show()

iris = sns.load_dataset('iris')
sns.lmplot( x="sepal_length" , y="sepal_width" , data=iris, fit_reg=False, hue='species' , legend=False)
plt.legend(loc='lower right')
plt.show()