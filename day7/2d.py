import numpy as np 

# numpy aray
arr = np.array([1,2,3,4,5])
print(arr) # [1 2 3 4 5]
print(type(arr)) # <class 'numpy.ndarray'>

# 2d array (martix)
matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(matrix) 
print(matrix.shape) # (3, 3)

print(np.zeros((3, 3)) )     # সব 0 দিয়ে 3x3 matrix

# np.ones((2, 4))       # সব 1 দিয়ে 2x4 matrix
# np.arange(0, 10, 2)   # [0, 2, 4, 6, 8] (start, stop, step)
# np.linspace(0, 1, 5)  # [0, 0.25, 0.5, 0.75, 1.0] (5টা equally spaced)
# np.random.rand(3, 3)  # random 3x3 matrix (0-1 এর মধ্যে)

a = np.array([[1, 2, 3], [4, 5, 6]])

a.shape    # (2, 3) → 2 rows, 3 columns
a.ndim     # 2 → dimensions সংখ্যা
a.dtype    # int64 → data type
a.size     # 6 → মোট elements সংখ্যা


a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

# Element-wise operations (loop ছাড়া!)
print(a + b)    # [11, 22, 33, 44, 55]
print(a * b)    # [10, 40, 90, 160, 250]
print(a ** 2)   # [1, 4, 9, 16, 25]
print(b / a)    # [10, 10, 10, 10, 10]

# Scalar operation
print(a + 10)   # [11, 12, 13, 14, 15]
print(a * 2)    # [2, 4, 6, 8, 10]

a = np.array([10, 20, 30, 40, 50])

a[0]      # 10 (first element)
a[-1]     # 50 (last element)
a[1:4]    # [20, 30, 40] (index 1 থেকে 3)
a[:3]     # [10, 20, 30] (শুরু থেকে index 2)

# 2D array indexing
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix[0]       # [1, 2, 3] (first row)
matrix[1][2]    # 6 (row 1, column 2)
matrix[1, 2]    # 6 (same, cleaner syntax)
matrix[:, 1]    # [2, 5, 8] (সব row এর column 1)

a = np.array([1, 2, 3, 4, 5])

np.sum(a)      # 15
np.mean(a)     # 3.0
np.max(a)      # 5
np.min(a)      # 1
np.std(a)      # standard deviation
np.sort(a)     # sorted array

