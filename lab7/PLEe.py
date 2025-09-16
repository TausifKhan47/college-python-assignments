import numpy as np

arr = np.array([10, 20, 30, 40, 50])

memory_size = arr.size * arr.itemsize

print("Array:", arr)
print("Memory size of array in bytes:", memory_size)
