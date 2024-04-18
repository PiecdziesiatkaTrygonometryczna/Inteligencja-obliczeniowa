import numpy as np
import time

def matrix_multiply(A, B):
    result = [[sum(a*b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
    return result

# Generate two large random matrices
A = np.random.rand(500, 500)
B = np.random.rand(500, 500)

start_time = time.time()
C = np.dot(A, B)
numpy_duration = time.time() - start_time
print(numpy_duration)

# Convert numpy matrices to lists for native multiplication
A_list = A.tolist()
B_list = B.tolist()

start_time = time.time()
C_native = matrix_multiply(A_list, B_list)
native_duration = time.time() - start_time
print(native_duration)