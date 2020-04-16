import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("iris.csv")

#plt.scatter(df['sepal_length'], df['sepal_width'])
#plt.show()

plt.style.use('ggplot')
plt.hist(df['sepal_length'])
plt.xlabel('sepal_length')
plt.show()
plt.hist(df['sepal_width'])
plt.show()
plt.hist(df['petal_length'])
plt.show()
plt.hist(df['petal_width'])
plt.show()

#df.hist(column=["SepalLengthCm", "SepalWidthCm", "PetalLengthCm",
# "PetalWidthCm", "Species"], figsize=(10, 10))


#print(df) 

