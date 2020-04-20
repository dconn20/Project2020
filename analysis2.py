import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("iris.csv")

#Boxplots

sns.set(style="whitegrid", palette="GnBu_d", rc={'figure.figsize':(11.7,8.27)})

title="Compare the Distributions of Sepal Length"

sns.boxplot(x="species", y="sepal_length", data=df)

# increasing font size
plt.title(title, fontsize=26)
# Show the plot
plt.show()

title="Compare the Distributions of Sepal Width"

sns.boxplot(x="species", y="sepal_width", data=df)

# increasing font size
plt.title(title, fontsize=26)
# Show the plot
plt.show()

title="Compare the Distributions of Petal Length"

sns.boxplot(x="species", y="petal_length", data=df)

# increasing font size
plt.title(title, fontsize=26)
# Show the plot
plt.show()

title="Compare the distributions of Petal Width"

sns.boxplot(x="species", y="petal_width", data=df)

# increasing font size
plt.title(title, fontsize=26)
# Show the plot
plt.show()

#Swarmplot

#setting the background color and size of graph
sns.set(style="whitegrid", palette="GnBu_d", rc={'figure.figsize':(11.7,8.27)})

# "Melt" the dataset
df = pd.melt(df, "species", var_name="measurement")


sns.swarmplot(x="measurement", y="value", hue="species",palette="GnBu_d", data=df)

#Remove the top and right spines from plot
sns.despine()
plt.show()


