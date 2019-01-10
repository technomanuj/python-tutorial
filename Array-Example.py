# Examples of Arrays
# When people talk about Python arrays, more often than not, they are talking about Python lists.
# you will have to use array module to create arrays in python

import array as arr

a = arr.array('i', [2, 4, 6, 8])
b = arr.array('i', [61, 62, 65])

print("First Element:", a[0])
print("Second Element:", a[1])
a[1] = 99
a.append(780)
a.extend([5, 6, 7])
print(a)

print(a+b)

'''
    y = 6
    print(type(y))
'''

