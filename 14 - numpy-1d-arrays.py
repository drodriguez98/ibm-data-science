# import numpy library

import numpy as np 

# Create a numpy array

a = np.array([0, 1, 2, 3, 4])
a

# Get the size of numpy array

a.size

# Get the number of dimensions of numpy array

a.ndim

# Get the shape/size of numpy array

a.shape

# Print each element

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

# Check the type of the array

type(a)

# Check the type of the values stored in numpy array

a.dtype

# Assign the 5th element to 0

a[4] = 0

# Slicing the numpy array

b = a[1:4]

# Set the fourth element and fifth element to 300 and 400

a[3:5] = 300, 400

# Create the index list

select = [0, 2, 3, 4]

# Use List to select elements

b = a[select]

# Assign the specified elements to new value

a[select] = 100000

# Create a numpy array

a = np.array([1, -1, 1, -1])

# Get the mean of numpy array

mean = a.mean()

# Get the standard deviation of numpy array

standard_deviation=a.std()

# Create a numpy array

b = np.array([-1, 2, 3, 4, 5])

# Get the biggest value in the numpy array

max_b = b.max()

# Get the smallest value in the numpy array

min_b = b.min()

# Array addition

u = np.array([1, 0])
v = np.array([0, 1])
z = np.add(u, v)

# Array substraction

a = np.array([10, 20, 30])
b = np.array([5, 10, 15])

c = np.subtract(a, b)

print(c)

# Array multiplication

x = np.array([1, 2])
y = np.array([2, 1])

z = np.multiply(x, y)

# Array division

a = np.array([10, 20, 30])
b = np.array([2, 10, 5])

c = np.divide(a, b)

# Adding Constant to a Numpy Array

u = np.array([1, 2, 3, -1]) 
u + 1

# Mathematical Functions

# The value of pi

np.pi

# Create the numpy array in radians

x = np.array([0, np.pi/2 , np.pi])

# Calculate the sin of each elements

y = np.sin(x)

# Iterating 1-D Arrays

arr1 = np.array([1, 2, 3])
print(arr1)

# Quiz on 1D Numpy Array

u = np.array([1, 0])
v = np.array([0, 1])