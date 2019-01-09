# Fibonacci series In Python:
# the sum of two elements defines the next element

print('write Fibonacci series using while loop ')
a, b = 0, 1
while a <= 20:
    print(' The value of a is ', a)
    a, b = b, a + b

print('write Fibonacci series using functions ')


def fib(n):    # write Fibonacci series up to n
    num1, num2 = 0, 1
    while num1 < n:
        print(num1, end=' ')
        num1, num2 = num2, num1 + num2
    print()


def fib2(num):
    result = []

    x, y = 0, 1
    while x < num:
        result.append(x)
        x, y = y, x+y
    return result


def concat(*args, sep="/"):
    return sep.join(args)


fib(50)


fibResult = fib2(50)


print(fibResult)

print(concat("earth", "moon", "mars"))
