import numpy as np

# Create an array of 10 zeros
zeros_array = np.zeros(10)

# Create an array of 10 ones
ones_array = np.ones(10)

# Create an array of 10 fives
fives_array = np.full(10, 5)

print("Array of zeros:", zeros_array)
print("Array of ones:", ones_array)
print("Array of fives:", fives_array)





import numpy as np

# Create a 3x3 matrix with values from 2 to 10
matrix = np.arange(2, 11).reshape(3, 3)

print("3x3 matrix:")
print(matrix)
