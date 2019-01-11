# Here we will create Numpy Array from different methods

# import numpy package
import numpy as np

my_list = [1, 2, 3, 4, 5, 6]

# Create numpy array from python list
np_arr = np.array(my_list)

# print the current version of numpy
print(np.__version__)

# print numpy array
print(np_arr)

# see the difference if 2 is multiplied by numpy array and python list
print(np_arr * 2)
print(my_list * 2)

# Create numpy array using range
np_arr_2 = np.array(range(5))
print(np_arr_2.size)


# Create numpy array using arange function
print(np.arange(5))
print(np.arange(10, 36, 5))
print(np.arange(36, step=5))


# linespace function
print(np.linspace(2.0, 3.0, 5))

# zeros() function
print(np.zeros(5))

print("Two dimensional array ")
print(np.zeros((5, 4)))

print("Three dimensional array ")
# 5 two dimensional array
# 4 tells group of matrices
# 3 tells that each one of these arrays contain three columns
print(np.zeros((5, 4, 3)))

# we can specify the data type of numbers by default this is float
print(np.zeros(11, dtype='int64'))


# ones function
print(np.ones(7))


