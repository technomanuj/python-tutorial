# create function to do sum of two numbers
def sum_numbers(num1, *allothernum):
    y = num1
    for i in allothernum:
        y = y + i
    return y


def greet_user(username):
    return " Hello " + username


def change_value(x):
    print(id(x))
    x[0] = 55
    x[1] = 66

    print(id(x))
    return x


a = [1, 2, 3]
print(id(a))

print(change_value(a))
print("Sum of numbers are :", sum_numbers(1, 2, 3, 77, 88, 75))
