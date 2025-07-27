import numpy as np

#1D ARRAY
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])      # First element → 10
print(arr[-1])     # Last element → 50

print(arr[1:4])    # Slicing → [20 30 40]
print(arr[:3])     # First 3 → [10 20 30]
print(arr[::2])    # Step of 2 → [10 30 50]

print('-'*40)

#2D ARRAY
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

print(arr2d[0])        # First row → [1 2 3]
print(arr2d[1][2])     # Element at 2nd row, 3rd column → 6
print(arr2d[1, 2])     # Same as above (preferred)

print(arr2d[0:2, 1:3]) # Slicing rows 0-1 and cols 1-2 → [[2 3], [5 6]]
print(arr2d[:, 1])     # All rows, 2nd column → [2 5 8]
print(arr2d[::2, ::2]) # Every other row and col → [[1 3], [7 9]]

print('-'* 40)

#3D ARRAY
arr3d = np.array([[[1, 2],
                   [3, 4]],
                  
                  [[5, 6],
                   [7, 8]]])

print(arr3d[0])        # First 2D matrix
print(arr3d[1, 0, 1])  # Element at (1st block, 1st row, 2nd col) → 6

print("-" * 40)

#BOOLEAN INDEXING
arr = np.array([10, 15, 20, 25, 30])
print(arr[arr > 20])   # → [25 30] i.e 20 se zyada vale values

print('-' * 40)

#START-STOP-STEP
arr = np.array([100, 200, 300, 400, 500])
print(arr[[0, 2, 4]])  # Select by index list → [100 300 500]



############################################################################################################################################################################################