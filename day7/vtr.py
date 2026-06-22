import numpy as np 

# numpy vectorised operation

# arr1 = np.array([1,2,3,4,5])
# arr2 = np.array([10,20,30,40,50])

# ### elemint waise addition
# print("Addition: ",arr1+arr2)
# ## element waise substraction
# print("Substraction: ",arr1-arr2)
# ## element waise multiplication
# print("Multiplication: ",arr1*arr2)
# ## element waise division
# print("division: ",arr1/arr2)
## ! element waise means index waise

'''
Addition:  [11 22 33 44 55]
Substraction:  [ -9 -18 -27 -36 -45]
Multiplication:  [ 10  40  90 160 250]
division:  [0.1 0.1 0.1 0.1 0.1]
'''

## universel funtions - mane je function gula numpy er sob arry jurei kaj krbe
# arr1 = np.array([2,3,4,5,6])
# ## suarq root
# print("suare: ",np.sqrt(arr1))
# # Exponential
# print("Exponential: ",np.exp(arr1))
# ## sine
# print("Sine: ",np.sin(arr1))
# # natural log
# print("log: ",np.log(arr1))

#! all calculates element waise
'''
suare:  [1.41421356 1.73205081 2.         2.23606798 2.44948974]
Exponential:  [  7.3890561   20.08553692  54.59815003 148.4131591  403.42879349]
Sine:  [ 0.90929743  0.14112001 -0.7568025  -0.95892427 -0.2794155 ]
log:  [0.69314718 1.09861229 1.38629436 1.60943791 1.79175947]
'''

## array slicing and indexing
# arr = np.array([
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]) # 3,4 - 3 row 4 col
# print(arr)
'''
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
'''
# ? how can i pickup single element from this arr?
# print('first Element: ', arr[0][0])
# first Element:  1
# ? how can i pickup single element from this arr?
# print('Element: ',arr[1][2])
# 2 nmbr colum er 3 nmbr element
# ans: Element:  7

# ? pickup multiple elements
# print('Multiple element: \n',arr[1:,2:])
'''
Multiple element: 
 [[ 7  8]
 [11 12]]
'''
## modify array element
# change 0 no index into 100
# arr2 = arr[0,0]=100
# print(arr2)
# output-100

## some practicle practice
## statistical concepts-normalization
#? normalization: mean of 0 and standard deviation of 1
# data = np.array([1,2,3,4,5])

# calculate mean and standrad derivation
# mean = np.mean(data)
# std_dev = np.std(data)
# print(mean)
# mean: 3.0
# print(std_dev)
# std: 1.4142135623730951

## normalization
# normalized_data = (data - mean)/std_dev
# print("Normalized data: ",normalized_data)
'''
Normalized data:  
[-1.41421356 -0.70710678  0.       
0.70710678  1.41421356]
'''

# data = np.array([1,2,3,4,5,6,7,8,9,10])

# # mean
# mean = np.mean(data)
# print("Mean: ",mean)
# ## median
# median = np.median(data)
# print("Medidan: ",median)
# ## standard deviation
# std_Dev = np.std(data)
# print(" Standard deviation: ",std_Dev)
# ## variacne
# variacne = np.var(data)
# print("Variacne: ",variacne)

'''
output:
Mean:  5.5
Medidan:  5.5
 Standard deviation:  2.8722813232690143
Variacne:  8.25 
'''

## logical operation 
data = np.array([1,2,3,4,5,6,7,8,9,10])

# true if ligis matches false if not
print(data>5)
# [False False False False False  True  True  True  True  True]
print(data[data>5]) # 5 theke boro nmbr gula dibe
# [ 6  7  8  9 10]
Data = data[(data>5)& (data<8)]  # 5 theke boro 8 theke coto
print(Data)
#[6 7]





