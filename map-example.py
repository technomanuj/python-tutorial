
# map() function
# r = map(func, seq)
# the first argument is a function and the second a sequence  eg. a list.
# func applies to all the elements of the sequence seq


def fahrenheit(temp):
    return (float(9)/5) * temp + 32


def celsisus(temp):
    return (float(5)/9) * (temp-32)


temperatures = (36.5, 37)
# the below given statement will gives map object
# F = map(fahrenheit, temperatures)
# C = map(celsisus, temperatures)
# print(F)
# print(C)


temp_in_Fahrenheit = list(map(fahrenheit, temperatures))
print("Temp in Fahrenheit using def:", temp_in_Fahrenheit)

temp_in_Celsius = list(map(celsisus, temperatures))
print("Temp in Celsius:", temp_in_Celsius)

# now we will use lambda operator instead of using def. But again as per PEP-8 coding style guide
# use def instead of lambda to calculate temperature in Fahrenheit
#  The general syntax of a lambda function is quite simple:
# lambda argument_list: expression

temp_in_Fahrenheit = list(map(lambda t: (float(9)/5) * t+32, temperatures))
print("Temp in Fahrenheit using lambda operator:", temp_in_Fahrenheit)





