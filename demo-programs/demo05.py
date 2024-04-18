import numpy as np
from sys import getsizeof
arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(arr.dtype)
print(getsizeof(arr)-112)  #112 bytes is additional info for multidimensional arrays







# getsizeof - bytes
# Int32 -- (-2,147,483,648 to +2,147,483,647) 4 bytes
# Int64 -- (-9,223,372,036,854,775,808 to +9,223,372,036,854,775,807) 8 bytes
# what happens if we add 3 million?
# what happens if I change the line to: arr = np.array([1, 2, 3, 4], dtype='int64')