import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sys 



iris=pd.read_csv("iris.csv")

iris.columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']

# To generate a Scatterplot using pandas #

iris.plot(kind="scatter" , x= 'sepal_lenght' , y='sepal_Width')

# Scatterplot in Seaborn #

iris = sns.load_dataset('iris')
sns.lmplot( x="petal_length" , y="petal_width" , data=iris, fit_reg=False, hue='species' , legend=False)
plt.legend(loc='lower right')
sns.plt.show()


# To display the plot #

plt.show()

# To change colours and size & display plot #

iris.plot(kind="scatter" , x="Sepal_Lenght" , y="Sepal_Width" , color="green" , s=70)
plt.show()

# To generate a jointplot using seaborn - joing a bivariate scatterplot and a univariate histogram in one grapph #

sns.joint(x="Sepal_Lenght" , y="Sepal_Width" , data=iris , size=5)
plt.show()


 

