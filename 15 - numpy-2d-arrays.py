# Import the libraries

import numpy as np

# Create a list

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]

# Convert list to Numpy Array
# Every element is the same type

A = np.array(a)

# Show the numpy array dimensions

A.ndim

# Show the numpy array shape

A.shape

# Show the numpy array size

A.size

# Access the element on the second row and third column

A[1, 2]

# Access the element on the first row and first and second columns

A[0][0:2]

# Access the element on the first and second rows and third column

A[0:2, 2]

# Create a numpy arrays X and Y

X = np.array([[1, 0], [0, 1]]) 
Y = np.array([[2, 1], [1, 2]]) 

# Add X and Y

Z = X + Y

# Create a numpy array Y

Y = np.array([[2, 1], [1, 2]]) 

# Multiply Y with 2

Z = 2 * Y

# Create a matrix A and B

A = np.array([[0, 1, 1], [1, 0, 1]])
B = np.array([[1, 1], [1, 1], [-1, 1]])

