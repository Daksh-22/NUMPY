import numpy as np

# ORIGINAL ARRAY
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print("Original Array:\n", arr)
print("Shape:", arr.shape)

print("-" * 40)

# RESHAPING
reshaped = arr.reshape(3, 2)
print("Reshaped to (3,2):\n", reshaped)

reshaped_flat = arr.reshape(-1)
print("Flattened using reshape(-1):", reshaped_flat)

print("-" * 40)

# FLATTENING
flat = arr.flatten()
print("Flattened using flatten():", flat)

print("-" * 40)

# TRANSPOSE
transposed = arr.T
print("Transposed Array:\n", transposed)

print("-" * 40)

# RESIZE (in-place, changes original array shape)
arr_resize = np.array([1, 2, 3, 4, 5, 6])
arr_resize.resize((2, 3))
print("Resized Array:\n", arr_resize)

print("-" * 40)

# STACKING ARRAYS
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Stacking vertically (rows):\n", np.vstack((a, b)))
print("Stacking horizontally (columns):\n", np.hstack((a, b)))
print("Stacking along depth (new axis):\n", np.stack((a, b), axis=1))

print("-" * 40)

# SPLITTING ARRAYS
arr2 = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8]])

print("Original for Splitting:\n", arr2)

# Horizontal split (split columns)
print("Horizontal Split:", np.hsplit(arr2, 2))

# Vertical split (split rows)
print("Vertical Split:", np.vsplit(arr2, 2))

print("-" * 40)

# CHANGING DIMENSIONS
a = np.array([1, 2, 3])
print("Original 1D:", a)

print("As column vector:\n", a[:, np.newaxis])
print("As row vector:\n", a[np.newaxis, :])
 


############################################################################################################################################################################################