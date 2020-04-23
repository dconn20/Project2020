import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

iris = pd.read_csv("iris.csv")

iris.columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']

#Boxplots

sns.set(style="whitegrid", palette="muted", rc={'figure.figsize':(11.7,8.27)})

title="Compare the Distributions of Sepal Length"

sns.boxplot(x="species", y="sepal_length", data=iris)

# increasing font size
plt.title(title, fontsize=26)
# Show the plot
plt.show()

title="Compare the Distributions of Sepal Width"

sns.boxplot(x="species", y="sepal_width", data=iris)

# increasing font size
plt.title(title, fontsize=26)
# Show the plot
plt.show()

title="Compare the Distributions of Petal Length"

sns.boxplot(x="species", y="petal_length", data=iris)

# increasing font size
plt.title(title, fontsize=26)
# Show the plot
plt.show()

title="Compare the distributions of Petal Width"

sns.boxplot(x="species", y="petal_width", data=iris)

# increasing font size
plt.title(title, fontsize=26)
# Show the plot
plt.show()

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



#Swarmplot

#setting the background color and size of graph
sns.set(style="whitegrid", palette="muted", rc={'figure.figsize':(11.7,8.27)})

# "Melt" the dataset
iris = pd.melt(iris, "species", var_name="measurement")

sns.swarmplot(x="measurement", y="value", hue="species",palette="muted", data=iris)

#Remove the top and right spines from plot
sns.despine()
plt.show()



