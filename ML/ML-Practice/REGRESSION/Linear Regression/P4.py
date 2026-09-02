import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error
from scipy import stats
import numpy as np

path = pd.read_csv(r"C:\Users\hp\Downloads\Salary Data.csv")

new_path = path.dropna()

change_data = pd.get_dummies(
    new_path,
    columns=['Gender'],
    dtype=int,
    drop_first=True
)

print(change_data.head())

new_path['Age'] = new_path['Age'].astype(int)
new_path['Salary'] = new_path['Age'].astype(int)


x = new_path['Age']
y = new_path['Salary']

m, b, r, p, std_err = stats.linregress(x,y)

def my_function(x):
    return m * x + b

model = list(map(my_function, x))

my_line = np.linspace(my_function,x)

plt.plot(x, model)
plt.scatter(x,y)
plt.show()