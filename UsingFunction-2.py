# function that return list of name whose length is greater than 5
def morethanfive(*username):
    result = []
    for name in username:
        if len(name) > 4:
            result.append(name)
    return result


# function that return count of names whose length is greater than 5
def name_gt_five_char(*username):
    # ls = ["true", "true", "false"]
    # print(ls.count("true"))
    return [len(name) > 4 for name in username].count(True)


# find factorial of a number using loop
def factorial(num):
    x = 1
    while num >= 1:
        x = x * num
        num = num - 1
    return x


# find factorial of a number using recursion
def fact(num):
    if num == 0:
        return 1

    return num * fact(num - 1)


neon = 5

print('Factorial of {0} is'.format(neon), fact(neon))

print("Name with maximum five characters", morethanfive("manoj", "anuj", "tanuj", "kaka", "rajkishore"))

print("Total name have more than five characters", name_gt_five_char("manoj", "anuj", "tanuj", "kaka", "rajkishore"))
