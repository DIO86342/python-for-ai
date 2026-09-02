import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd



# x = np.array([1,2,3,34,6,654,3,6,5])

# y = np.mean(x)
# y2 = np.sort(x)
# y3 = np.median(x)
# y4 = np.mod(x)
# print(y4)
# # print(y2)
# # print(y3)
# # print(y)




#STANDARD DAVIATION & VARIANCE

# x = np.array([1,2,3,34,6,654,3,6,5])
# y1 = np.std(x)#Standard daviation
# y2 = np.var(x)#Vriance
# print(y1)
# print(y2)



#Percentiles?
"""Example
    Imagine the heights of 100 students.
    If your height is at the 90th percentile, approximately:
    90 students are shorter than you
    10 students are taller than you
"""
# x = np.array([40, 50, 55, 60, 65, 70, 75, 80, 90, 100])
# x2  = np.percentile(x, 80)
# print(x2)


#Data Distribution
# X =np.random.uniform(0,5,200)#Create an array containing 200 random floats between 0 and 5:
# print(X)



# y = np.random.uniform(1,100,20)
# plt.hist(y)
# plt.show()

# x = np.random.uniform(0,100,1000)
# plt.pie(x)
# plt.hist(x)
# plt.show()



# x = np.random.normal(5,1,1000)
# plt.hist(x,100)
# plt.show()