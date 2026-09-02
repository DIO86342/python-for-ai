import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


path = pd.read_csv(r"C:\Users\hp\Downloads\Salary Data.csv").dropna()


x = path['Age']
y = path['Salary']


model = np.poly1d(np.polyfit(x,y,3))

line = np.linspace(x.min(), x.max(), 100)


plt.plot(line, model(line))
plt.scatter(x,y)
plt.show()