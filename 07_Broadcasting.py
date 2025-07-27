import numpy as np

#SCALAR BROADCASTING
arr1 = np.array([100,200,300,400,500,600])

print(arr1+5)

discount = 10
final_prices = arr1 - (arr1 * (discount)/100)
print(final_prices)

#1D and 2D
arr2D = np.array([[100,200,300,123] , 
                 [500,600,700]])

arr1D = np.array([7,8,9])

result = arr1D +arr2D      #"Broadcasting" smaller array onto higher one

#Adding another column using ".reshape()"
arr1D = np.array([7, 8, 9, 10, 11, 12]).reshape(1, 2, 3)

