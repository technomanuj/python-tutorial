# Python Matrix

A = [
    [1, 4, 5],
    [5, 6, 7]]

'''
print(A)
print(A[0])
print(A[0][1])

'''

B = [
    [2, 5, 7],
    [8, 10, 11]
]

# Add both A and B metrix


result = [
    [0, 0, 0],
    [0, 0, 0]
]

print('Matrix addition using nested loop')

for i in range(len(A)):
    for j in range(len(B[i])):
        result[i][j] = A[i][j] + B[i][j]

print(result)

# Matrix addition using nested list comprehension

print('Matrix addition using nested list comprehension')

newResult = [[A[i][j] + B[i][j] for j in range(len(B[i]))] for i in range(len(A))]

print(newResult)
