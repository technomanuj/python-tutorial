
x = 1

isNotPrime = 0

totalNumbers = int(input("Enter value to print prime numbers upto : "))

'''
Print prime numbers
'''

while x <= totalNumbers:
    iCounter = 1
    isNotPrime = 0
    while iCounter < x:
        if iCounter > 1 and x % 1 == 0 and x % iCounter == 0:
            isNotPrime = 1
            break
        iCounter = iCounter + 1

    if isNotPrime == 0:
        print(x)
    x = x + 1