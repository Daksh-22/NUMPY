import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([10, 20, 30, 40])

# Add scalar
print("Add 5:", arr1 + 5)

# Element-wise operations
print("arr1 * arr2:", arr1 * arr2)

# Dot product
print("Dot product:", np.dot(arr1, arr2))

# Normalizing
norm = np.linalg.norm(arr1)
print("Normalized arr1:", arr1 / norm)

# Boolean indexing (vectorized filtering)
print("Values > 2:", arr1[arr1 > 2])
