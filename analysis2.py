import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("iris.csv")

#with open("summary.txt", 'w') as f:
 #   f.write('df')



with open("iris.csv") as f:
    with open("copy.txt", "w") as f1:
        for line in f:
            f1.write(line)