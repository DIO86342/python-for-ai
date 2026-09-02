import numpy as np
import matplotlib.pyplot as plt


#SCATTER
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x,y, color="yellow")

# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])

# plt.scatter(x,y, color="red")
# plt.show()


#BAR
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# plt.bar(x,y)#QAAB VERTICAL BARS
# plt.show()


# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# plt.barh(x, y)#QAAB HORIZENTAL BARS
# plt.show()


x = np.random.normal(170, 10, 250)
y = np.random.normal(170, 10, 250)

# plt.hist(x)#HISTOGRAM BAR
plt.barh(x,y)
plt.show()

