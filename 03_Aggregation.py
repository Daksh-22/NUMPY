import numpy as np

# Sample 2D array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
 
print("Original Array:\n", arr)
print("-" * 40)

# SUM
print("Total Sum:", np.sum(arr))
print("Sum along rows (axis=1):", np.sum(arr, axis=1))
print("Sum along columns (axis=0):", np.sum(arr, axis=0))
print("-" * 40)

# MEAN
print("Overall Mean:", np.mean(arr))
print("Mean per row:", np.mean(arr, axis=1))
print("-" * 40)

# MIN and MAX
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))
print("Min per column:", np.min(arr, axis=0))
print("Max per row:", np.max(arr, axis=1))
print("-" * 40)

# STANDARD DEVIATION and VARIANCE
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("-" * 40)

# PRODUCT of all elements
print("Product of all elements:", np.prod(arr))
print("-" * 40)

# MEDIAN
print("Median:", np.median(arr))
print("-" * 40)

# ARGMAX and ARGMIN (index positions in flattened array)
print("Index of Max (argmax):", np.argmax(arr))
print("Index of Min (argmin):", np.argmin(arr))
print("-" * 40)

# Flattened array
print("Flattened array:", arr.flatten())


############################################################################################################################################################################################