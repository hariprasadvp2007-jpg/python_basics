import numpy as np

# 1. Creating a NumPy array
arr = np.array([10, 20, 30, 40])
print("Initial array:", arr)

# 2. Appending elements to the array
arr = np.append(arr, 50) # Append a single value
arr = np.append(arr, [60, 70]) # Append multiple value
print("After appending elements:", arr)

# 3. Removing elements from the array
arr = np.delete(arr, 1) # Removes element at index 1
arr = np.delete(arr, [2, 3]) # Removes elements at index 2 and 3
print("After deleting elements:", arr)


