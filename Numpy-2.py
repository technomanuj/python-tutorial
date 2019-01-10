# NumPy Array
# https://docs.scipy.org/doc/numpy-1.15.1/user/quickstart.html
# NumPy is a package for scientific computing which has support for a powerful N-dimensional
# array object.

import numpy as np

A = [
    [1, 4, 5],
    [6, 6, 7]]

B = [
    [2, 5, 7],
    [8, 10, 11]
]

mat1 = np.array(A)
mat2 = np.array(B)

# Addition of two matrices using numpy
print(mat1 + mat2)

# transpose of a matrix using numpy
print("Matrix :")
print(mat1)

print("Transpose Matrix :")
print(mat1.transpose())

# multiplication of two matrices using numpy
# print(mat1 * mat2) This is for multiplication of array corresponding elements

print("Multiplication of Matrix :")
A1 = np.array([[3, 6, 7], [5, -3, 0]])
B1 = np.array([[1, 1], [2, 1], [3, -3]])
C1 = A1.dot(B1)
print(C1)

print("Access rows and columns of a Matrix :")
A2 = [
    [1, 4, 5],
    [5, 6, 7]]

C2 = np.array(A2)
print("First Row:", C2[0])
print("Last Column:", C2[-1][-1])

C3 = np.array([1, 3, 5, 6, 7, 8, 9, 10])

print("Slicing of a matrix :", C3[2:6])

# 1st to last elements
print("1st to last elements:", C3[:])

# Reversing an array or list
print("Reversing a list:", C3[::-1])

