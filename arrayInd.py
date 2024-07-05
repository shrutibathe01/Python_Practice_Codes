import numpy as np

arr = np.array([1, 2, 3, 4])
print("Original Array is: ",arr)
First_ele=arr[0]
print("First Element of Array: ",First_ele)
Add=arr[1]+arr[2]
print("Addition of 2nd and 3rd Elements of Array: ",Add)

arr2=np.array([[1,2,3,4,5], [6,7,8,9,10]])
print()
print("2D array: ",arr2)
ele=arr2[0, 1]
print("2nd element of 1st row: ",ele)
ele2=arr2[1, -1]
print("Last element from 2nd dim: ",ele2 )
