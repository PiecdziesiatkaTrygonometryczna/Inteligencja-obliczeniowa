import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr)
print('shape of array :', arr.shape)

newarr = arr.reshape(2, 2)

print(newarr)
print('shape of a new array :', newarr.shape)