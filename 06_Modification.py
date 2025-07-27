import numpy as np

# ORIGINAL ARRAY
arr = np.array([10, 20, 30, 40, 50])
print("Original Array:", arr)

# MODIFYING SINGLE ELEMENT
arr[1] = 99
print("After modifying index 1:", arr)  # [10, 99, 30, 40, 50]

# MODIFYING MULTIPLE ELEMENTS (SLICING)
arr[2:4] = [77, 88]                  # element 2 and 3 ko 77 and 88 se replace krdia (4 isn't inclusive)
print("After slicing update:", arr)  # [10, 99, 77, 88, 50]

print("-" * 40)

# CONDITIONAL MODIFICATION
arr[arr > 50] = 100                        # Jo bhi value 50 se badi , replace maaro
print("Values > 50 changed to 100:", arr)  # [10, 99 → 100, 77 → 100, 88 → 100]

print("-" * 40)

# INSERTING VALUES
arr_new = np.insert(arr, 2, 555)            # (arr_name , index, value)
print("After insert at index 2:", arr_new)  # Insert 555 at index 2

print("-" * 40)

# DELETING VALUES
arr_deleted = np.delete(arr_new, 1)  
print("After deleting index 1:", arr_deleted)

print("-" * 40)

# APPENDING VALUES
arr_appended = np.append(arr, [60, 70])        # End me values insert krdega
print("After appending:", arr_appended)

print("-" * 40)

# CONCATENATION
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = np.concatenate((arr1, arr2))
print("Concatenated 1D:", result)
# Output: [1 2 3 4 5 6]

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

res = np.concatenate((a, b), axis=0)      # Vertial Stacking
print("Concat along rows:\n", res)

a1 = np.array([[1, 2], [3, 4]])
b1 = np.array([[5, 6], [7, 8]])

res = np.concatenate((a1, b1), axis=1)     # Horizontal Stacking
print("Concat along cols:\n", res)

# Stacking (basically adding a new dimension)
arr_one = np.arr([22,11,31,2])
arr_two = np.arr([44,22,62,4])

h_stack = np.hstack((arr_one,arr_two))      # Pehli array ke "AAGE" dusri array ko rakh dega
v_stack = np.vstack((arr_one,arr_two))      # Pehli array ke "NEECHE" dusri array ko rakh dega

############################################################################################################################################################################################

