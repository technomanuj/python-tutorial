
# Below given code is a very good approcach in python to generate prime number
# My other file PrimeNumber.py generates prime number in C# approach

for n in range(2, 50):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        print(n, ' is a prime number')