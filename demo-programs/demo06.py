import numpy as np
from sys import getsizeof

arr = np.array([1.1, 2.1, 3.1])
print(arr)
print(arr.dtype)
print(getsizeof(arr)-112) 


newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)
print(getsizeof(newarr)-112) 

newarr = arr.astype(np.float32)
print(newarr)
print(newarr.dtype)
print(getsizeof(newarr)-112) 