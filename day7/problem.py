import numpy as np

# ১। একটা 1D array বানাও: [10, 20, 30, 40, 50]
#    - সব element এর সাথে 5 যোগ করো
#    - সব element কে 2 দিয়ে গুণ করো
#    - sum, mean, max, min বের করো
arr = np.array([10,20,30,40,50])

print("Sum: ",np.sum(arr))
print("Mean: ",np.mean(arr))
print("Max: ",np.max(arr))
print("Min: ",np.min(arr))
print(arr * 2)
print(arr + 5)

# ২। একটা 3x3 matrix বানাও (যেকোনো numbers দিয়ে)
#    - shape, ndim, size print করো
#    - দ্বিতীয় row টা print করো
#    - তৃতীয় column টা print করো
a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print("shape: ",np.shape(a))
print("ndim: ",np.ndim(a))
print("Size: ",np.size(a))
print("second row: ",a[1])
print("third col: ",a[:,2])

# ৩। দুটো array বানাও:
#    a = [1, 2, 3, 4, 5]
#    b = [5, 4, 3, 2, 1]
#    - element-wise যোগ, বিয়োগ, গুণ করো
#    - a এর square বের করো (a**2)

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])

print("Sqrt of arr1: ",np.sqrt(arr1))
print("arr1 + arr2: ", (arr1+arr2))
print("arr1 - arr2: ", (arr1-arr2))
print("arr1 * arr2: ", (arr1*arr2))
print("arr1 / arr2: ", (arr1/arr2))


# ৪। Real-world:
#    - 5 জন student এর marks: [78, 92, 85, 60, 95]
#    - average, highest, lowest বের করো
#    - normalize করো (0-1 এর মধ্যে আনো)

marks = np.array([78,92,85,60,95])
mean = np.mean(marks)
print("Average: ",mean)

normalized = (marks - np.min(marks)) / (np.max(marks) - np.min(marks))
print("Normalized: ", normalized)
