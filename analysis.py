import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")

plt.scatter(df['sepal_length'], df['sepal_width'])
plt.show()