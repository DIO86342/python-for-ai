import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import r2_score



path = pd.read_csv(r"C:\Users\hp\Downloads\archive (10)\Iris.csv")




# # print(path.to_string())
# print(path.head())
# print(path.tail())
# print(path.duplicated().sum())
# print(path.info())
# print(path.isnull().sum())
# x = path["SepalLengthCm"]
# y = path["SepalWidthCm"]
# m, b, r, p, std_err = stats.linregress(x,y)
# def my_function(x):
#     return m * x + b
# my_model = list(map(my_function, x))



# plt.plot(my_model, x)


x = path["SepalLengthCm"]
print(x.shape)
# y = path["SepalWidthCm"]
# my_model = np.poly1d(np.polyfit(x,y,1))
# my_line = np.linspace(x.min(), x.max(),100)

# print(r2_score(y,my_model(x)))
# plt.scatter(x,y)
# plt.plot(my_line,my_model(my_line))
# plt.show()