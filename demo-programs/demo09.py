import numpy as np
import time

# Generate a large random array
large_array = np.random.rand(10000000)


# Task 1: computing mean
start_time = time.time()
mean_value = np.mean(large_array)
numpy_mean_duration = time.time() - start_time
print(numpy_mean_duration)

large_array_list = large_array.tolist()

start_time = time.time()
mean_value_native = sum(large_array_list) / len(large_array_list)
native_mean_duration = time.time() - start_time
print(native_mean_duration)

# Task 1: computing squares

start_time = time.time()
squared_array = np.square(large_array)
numpy_square_duration = time.time() - start_time
print(numpy_square_duration)

start_time = time.time()
squared_list = [x**2 for x in large_array_list]
native_square_duration = time.time() - start_time
print(native_square_duration)
