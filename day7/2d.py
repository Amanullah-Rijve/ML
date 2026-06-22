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

 (np.ones((2, 4)))       # সব 1 দিয়ে 2x4 matrix
# np.arange(0, 10, 2)   # [0, 2, 4, 6, 8] (start, stop, step)
# np.linspace(0, 1, 5)  # [0, 0.25, 0.5, 0.75, 1.0] (5টা equally spaced)
# np.random.rand(3, 3)  # random 3x3 matrix (0-1 এর মধ্যে)