import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def readFile(name_file):
    return pd.read_csv(name_file, delimiter=',', parse_dates=['PassengerId'], index_col = 'PassengerId')


plt.style.use('ggplot')
data = readFile("train.csv")
new_data = data[['Age']]
new_data.plot()
plt.show()

print(new_data)
