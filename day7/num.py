import numpy as np 

# creat arrays using numpy
# 1 d array
# arr1 = np.array([1,2,3,4,5])
# print(arr1)
# print(type(arr1))
# print(arr1.shape) # arrray shape (5,)-single d

# arr1 = np.array([1,2,3,4,5])

# lets reshape this array into 2 d array
# print(arr1.reshape(1,5)) # [[1 2 3 4 5]]
# 1,5 means 1 row and 5 col

# arr2 = np.array([
#     [1,2,3,4,5],
#     [6,7,8,9,10]
#     ]) # it is a 3d array

# print(arr2) 
# '''
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]]
# '''
# print(arr2.shape) # (2, 5) - 2 row 5 cola ray


# arr3 = np.arange(0,10,2) # 0,10 er modde number naw and 2 kre gap dw
# print(arr3)
# # reshape it in 2d
# print(arr3.reshape(5,1)) # 5 rows 1 col
'''
[[0]
 [2]
 [4]
 [6]
 [8]]
'''

# some inbuild function
# arr4 = np.ones((3,4)) # 3 row,4 col and sob element 1
# print(arr4)
'''
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]
'''

# indentity matrix 

arr5 = np.eye(3) # diagonal gula 1 hbe baki sob 0
print(arr5)
'''
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
'''





