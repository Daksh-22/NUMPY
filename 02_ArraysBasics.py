import numpy as np

arr_1d = np.array([10, 20, 30])     # 1D array
print("1D array:", arr_1d)
print("Shape:", arr_1d.shape)

arr_2d = np.array([[10, 20, 30, 40],   #2D array
                   [50, 40, 60, 70.33]])  # Made both rows equal in length
print("\n2D Array:\n", arr_2d)
print("Shape:", arr_2d.shape)          #(rows,cols)
print("Size:",arr_2d.size)             #Number of elements
print("DataType;-",arr_2d.dtype)       #DataType

arr_3d = np.array([[[1, 2], [3, 4]],
                   [[5, 6], [7, 8]]])  # 3D array
print("\n3D Array:\n", arr_3d)
print("Shape:", arr_3d.shape)

custom_arr = np.full((2, 2), 7)     # 2x2 matrix filled with 7
print("\nCustom Full Array:\n", custom_arr)

range_arr = np.arange(1, 11, 2)     # (start, stop, step)
print("\nRange Array:", range_arr)

identity_arr = np.eye(4)            # Identity Matrix
print("\nIdentity Matrix:\n", identity_arr)


#Operations
arr1 = np.array([1,2,3,4,5,10])

print(arr1+5)
print(arr1*5)
print(arr1**5)


############################################################################################################################################################################################