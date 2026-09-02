import numpy as np


# f = np.array([1,2,3,4])
# print(f)

#NumPy is used to work with arrays. The array object in NumPy is called ndarray.
# array = np.array([1,2,3,4])
# print(array)
# print(type(array))

# array = np.array((1,2,3,4))
# print(array)
# print(type(array))

# #0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
# arr = np.array(42)
# print(arr)

#An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
# array = np.array([1,2,3,4])
# print(array)

#An array that has 1-D arrays as its elements is called a 2-D array.
# array = np.array([[1,2,3,4],[5,6,7,8]])
# print(array)


#An array that has 2-D arrays (matrices) as its elements is called 3-D array.
# array = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
# print(array)



# Check Number Dimensions?
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
# arr1 = np.array(42)
# arr2 = np.array([1,2,3,4])
# arr3 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# arr4 = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
# print(arr1.ndim,"-D")
# print(arr2.ndim,"-D")
# print(arr3.ndim,"-D")
# print(arr4.ndim,"-D")


# Higher Dimensional Arrays
# An array can have any number of dimensions.

# arr = np.array([1, 2, 3, 4], ndmin=6)

# print(arr)
# print('number of dimensions :', arr.ndim)





#NumPy Array Indexing
# array = np.array([1,2,3])
# print(array[0])
# print(array[0] + array[1])  

#Access 2-D Arrays
# array = np.array([[1,2,3], [4,5,6]])
# print(array[0,2]) #array 1 with index 2
# print(array)

# #Access 3-D Arrays
# array = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
# print(array[0,1,2])
# print(array.ndim)


# import numpy as np

# arr = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
# print(arr)
# print(arr[0, 1, 2])
# print(arr.ndim)



# #Slicing arrays
# arr = np.array([1,2,3,4,5,6,7])
# print(arr[1:5])
# print(arr[1:])
# print(arr[:7])
# print(arr[-3:-1])
# print(arr[1:5:2])



# arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(arr)
# print(arr[1,2:5])
# print(arr[1:2, 2])

# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[:2])


#Data Types in NumPy

#integer
# arr = np.array([1,2,3,4])
# print(arr.dtype)

# arr = np.array([1,2,3,4], dtype=np.int32)
# print(arr.dtype)

#string
# arr = np.array(["APPLE", "BANANA", "KIWI"])
# print(arr.dtype)
# arr = np.array([1.23,3.4,5.6,8.7])
# print(arr.dtype)

# arr = np.array([1.23,3.4,5.6,8.7], dtype=np.float16)
# print(arr.dtype)

#BOOLEAN
# arr = np.array([True, False, False, True])
# print(arr.dtype)

# arr = np.array([1,2,3,4])
# condition = arr > 2
# print(condition)

# CONVERTING DATA TYPES
# arr = np.array([1,2,3,4])
# B_arr = np.array([True, False,False])
# new_arr = arr.astype(float)
# NEW_ARR = new_arr.astype(int)
# B_New = B_arr.astype(int)
# print(new_arr)
# print(NEW_ARR)
# print(B_New)

# arr = np.array([[1,2,3,4],[5,6,7,8]])
# print(arr.shape)


# arr = np.array(
#     [
#         [
#             [1,2,3,4],
#             [5,6,7,8],
#             [9,0,0,0,]
#         ],
#         [
#             [9,0,0,0,],
#             [2,3,4,5],
#             [9,0,0,0,]
#         ]
#     ]
# )
# print(arr.shape)


#ARRAY RESHAPE

# arr = np.array(
#     [1,2,3,4,5,6,7,8,9,10,11,12]
# )
# # print(arr)
# new_arr = arr.reshape(2,6)
# new_arr1 = arr.reshape(2,3,2)
# print(new_arr1)



# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# newarr = arr.reshape(2,4)

# print(newarr)
# print(newarr.shape)
# print(arr.reshape(2,4))
# print(arr.reshape(2,4).base)




# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# newarr = arr.reshape(2, 2, -1)

# print(newarr)




#NumPy Joining Array
# arr1 = np.array([1,2,3,4])
# arr2 = np.array([1,2,3,4])
# arr = np.concatenate((arr1, arr2))
# print(arr)


# arr1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# new_arr1 = arr1.reshape(2,6)
# arr2 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# new_arr2 = arr2.reshape(2,6)


# # print(new_arr1)
# # print(new_arr2)
# arr = np.concatenate((new_arr1, new_arr2))
# print(f"new arry concatenate {arr}")




# arr1 = np.array([[1,2,3,4],[5,6,7,8]])
# arr2 = np.array([[1,2,3,4],[5,6,7,8]])
# arr = np.concatenate((arr1, arr2), axis=1)
# print(arr)




# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.stack((arr1, arr2),axis=1)
# Arr = np.concatenate((arr1, arr2))
# print(arr)
# print(Arr)



# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])

# arr = np.hstack((arr1, arr2))
# Arr = np.stack((arr1, arr2), axis=1)
# ARr = np.vstack((arr1, arr2))
# ARR = np.concatenate((arr1, arr2))

# print(f"Hstack one: {arr}")
# print(f"Stacke one: {Arr}  {Arr.shape}")
# print(f"vstacke one: {ARr} {ARr.shape}")
# print(f"Concatenate one: {ARR} {ARR.shape}")


# #Splitting NumPy Arrays
# arr = np.array([1,2,3,4,5,6,7])
# new_arr = np.array_split(arr, 3)
# print(new_arr)
# print(new_arr[0])
# print(new_arr[1])
# print(new_arr[2])



# #Splitting 2-D Arrays
# arr = np.array([
#         [1, 2], 
#         [3, 4], 
#         [5, 6], 
#         [7, 8], 
#         [9, 10], 
#         [11, 12]
#     ])
# print(arr.shape)
# new_arr = np.array_split(arr, 3)#split it to 2 block each
# print(new_arr)


# arr = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9], 
#     [10, 11, 12], 
#     [13, 14, 15], 
#     [16, 17, 18]])
# print(arr.shape)
# # print(np.array_split(arr, 3, axis=1))

# print(np.vsplit(arr,3))


# arr1 = np.array([1,5,3,4,2,6,7,8,9,10,11,12])
# new_Arr = np.sort(arr1)
# print(new_Arr)

# arr1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(np.where(arr1 ==1))
# print(np.where(arr1%2 ==1))
# print(np.where(arr1%2 ==0))




# arr1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# filter_arr = []

# for i in arr1:
#     if i >3:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)
# new_arr = arr1[filter_arr]
# print(filter_arr)
# print(new_arr)


# arr1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# filter_arr = []

# for i in arr1:
#     if i%2 == 0:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)
# new_arr = arr1[filter_arr]
# print(filter_arr)
# print(new_arr)