import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas.testing as tm



df = pd.read_csv("iris.csv")

#plt.scatter(df['sepal_length'], df['sepal_width'])
#plt.show()

# Summary
with open("iris.csv") as f:
    with open("summary.txt", "w") as f1:
        for line in f:
            f1.write(line)



# Pairplots
sns.set_style("whitegrid")
sns.pairplot(df, hue ="species",height=3)
plt.show()
plt.savefig("pairplot.png")



# Histogram
plt.style.use('ggplot')
plt.hist(df['sepal_length'])
plt.xlabel('sepal_length')
plt.show()
plt.hist(df['sepal_width'])
plt.xlabel('sepal_width')
plt.show()
plt.hist(df['petal_length'])
plt.xlabel('petal_length')
plt.show()
plt.hist(df['petal_width'])
plt.xlabel('petal_width')
plt.show()



