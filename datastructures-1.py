import UserDefined as udf

# Example of List

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))

fruits.sort()
print(fruits)

fruits.remove('apple')
print(fruits)

del fruits[0]
print(fruits)


# List of squares
squares = [x**2 for x in range(10)]
print(squares)


# Example of tuples
# Tuples are immutable

testTuple = (1, 2, 3, 4, 5, 2)
print(testTuple, ' List of tuple')

# Example of sets
# A set is an unordered collection with NO DUPLICATE ELEMENTS

fruitBasket = {'apple', 'mango', 'apple', 'guava', 'orange'}
print('List of fruits :', fruitBasket)

# Import module userdefined.py and then call function defined in user module
print(udf.fibonaccisereis(50))




