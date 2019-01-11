# Lambda Operator
# The lambda operator or lambda function is a way to create small anonymous functions,
# i.e. functions without a name.
# lambda argument_list: expression


def dosum(x, y):
    return x + y


a = 10
b = 11

print("Sum of two number {0} and {1} is ".format(a, b), dosum(a, b))


# the above example is easy to understand but this can be done using lambda operator

result = lambda a, b: a+b

print(result(6, 7))

# ACCORDING TO PEP-8 DO NOT USE LAMBDA ISTEAD USE DEF. CHECK THE BELOW GIVEN LINK
# https://www.python.org/dev/peps/pep-0008/#programming-recommendations

# BUT LAMBDA CAN BE UTILISED WITH MAP FUNCTION

