import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]


# slope, intercept, r, p, std_err = stats.linregress(x,y)

# def my_function(x):
#     return slope * x + intercept

# my_model = list(map(my_function, x))

# plt.scatter(x,y)
# plt.plot(x, my_model)
# plt.show()


# print("Slope:", slope)
# print("Intercept:", intercept)


# print("P:", p)





# x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
# y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

# m, b, r, p, std_err = stats.linregress(x,y)

# def my_function(x):
#     return m * x + b

# my_model = list(map(my_function,x))
# plt.scatter(x,y)
# plt.plot(x, my_model)
# plt.show()



# x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
# y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

# m, b, r, p, std_err = stats.linregress(x,y)


# def my_function(x):
#     return m * x + b

# my_model = list(map(my_function, x))
# plt.scatter(x,y)
# plt.plot(my_model, x)
# plt.show()



path = pd.read_csv(r"C:\Users\hp\Downloads\Salary Data.csv")



# print(path.isnull().sum())
new_path = path.dropna()
# print(new_path.isnull().sum())


# x = new_path['Age']
# y = new_path['Salary']

# m, b, r, p, std_err = stats.linregress(x,y)

# def my_function(x):
#     return m * x + b

# my_model = list(map(my_function, x))



# print(r**2)
# plt.scatter(x,y, color='green')
# plt.plot(x, my_model, color="red")
# plt.show()






