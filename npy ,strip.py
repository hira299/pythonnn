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



# Store a person's name with whitespace characters
name = "\t\n  John Doe  \n\t"

# Print the name with the whitespace displayed
print("Name with whitespace:")
print(repr(name))  # Using repr() to show the whitespace characters clearly

# Print the name using lstrip() to remove leading whitespace
print("\nName with leading whitespace removed (lstrip()):")
print(repr(name.lstrip()))

# Print the name using rstrip() to remove trailing whitespace
print("\nName with trailing whitespace removed (rstrip()):")
print(repr(name.rstrip()))

# Print the name using strip() to remove both leading and trailing whitespace
print("\nName with leading and trailing whitespace removed (strip()):")
print(repr(name.strip()))
