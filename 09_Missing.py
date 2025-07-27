import numpy as np

#Creating array with missing values
missing = np.array([10,20,30,np.nan,40,np.nan,60])
print("Array with missing values",missing)

#Checking for missing values
print("Is NAN:-",np.isnan(missing))

#Counting number of missing values
print("Number of missing values are:", np.isnan(missing).sum())

#Replacing NAN's with values
filler_arr = np.nan_to_num(missing , nan = 0)
print("Filled Array:",filler_arr)

#Removing NAN values
full_arr = missing[~np.isnan(missing)]

# Compute mean ignoring NaNs
mean_without_nan = np.nanmean(missing)
print("Mean (ignoring NaNs):", mean_without_nan)