import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# df = pd.read_excel("C:/Users/hp/Desktop/PythonProjects/python-for-ai/archive (8)/fitness_data_unformatted_issues.xlsx")
# # print(df.to_string())
# df.plot()
# plt.show()
# print(matplotlib.__version__)


# x = np.array([0,6])
# y = np.array([0,5])

# plt.plot(x,y, 'o' "r")
# plt.show()



# x=np.array([2,3,4,5,6,7])
# y=np.array([100,200,300,400,500,600])


# plt.plot(x,y, "o" "r")
# plt.show()


# y=np.array([3, 8, 1, 10, 5, 7])
# plt.plot(y, marker='o', color='r', ls='--',  ms=10)
# plt.show()



# y=np.array([3, 8, 1, 10, 5, 7])
# x=np.array([5, 8, 10, 2, 15, 4])

# plt.plot(x, 'o:r')
# plt.plot(y, '*--g')
# plt.show()
# plt.axis()
# plt.grid()




# x1 = np.array([0, 1, 2, 3])
# y1 = np.array([3, 8, 1, 10])
# x2 = np.array([0, 1, 2, 3])
# y2 = np.array([6, 2, 7, 11])


# plt.plot(x1,y1,x2,y2)
# plt.show()



# x = np.array([0,1,2,3,4])
# y = np.array([0,2,4,2,0])
# x2 = np.array([1,2,3])
# y2 = np.array([2,2,2])
# x3 = np.array([5,5,5,7,6.5,5,6.5,7,5])
# y3 = np.array([0,3,5,5,3,3,3,0,0])

# font1 = {
#     "family": "Serif",
#     "color" : "blue",
#     "size" : 20
# }


# plt.plot(x,y, 'o:r')
# plt.plot(x2,y2, '*--g')
# plt.plot(x3,y3)
# plt.xlabel("Wa ikanaa", fontdict=font1)
# plt.ylabel("Wa ikanaa")
# plt.ylabel("Wa ikanaa")
# plt.title("Anna waa ikan", loc="left")
# # plt.grid()
# plt.grid(axis="x") #Display only grid lines for the x-axis:
# plt.show()


# #plot one
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(1,2,1)
# plt.plot(x,y)


# #plot two

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(1,2,2)
# plt.plot(x,y)


# plt.show()\



# #plot one
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2,1,1)
# plt.plot(x,y)


# #plot two

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2,1,2)
# plt.plot(x,y)


# plt.show()




#plot one
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2,4,1)
plt.plot(x,y)

#plot 2
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2,4,2)
plt.plot(x,y)

#plot 2
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2,4,3)
plt.plot(x,y)

#plot 2
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2,4,4)
plt.plot(x,y)


#plot 2
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2,4,5)
plt.plot(x,y)


#plot 2
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2,4,6)
plt.plot(x,y)


#plot 2
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2,4,7)
plt.plot(x,y)

#plot 2
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2,4,8)
plt.plot(x,y)
plt.show()
