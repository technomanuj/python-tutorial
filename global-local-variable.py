a = 10


def something():
    global a
    a = 15
    print("Local", a)
    print("Address of a", id(a))

def morethanfive(*username):
    result = []
    for name in username:
        if len(name) > 4:
            result.append(name)

    return result


def countnamelenghtgreaterfive(*username):
    result = []
    for name in username:
        if len(name) > 4:
            result.append(name)
    '''
        ls = ["true", "true", "false"]
        print(ls.count("true"))
    '''

    return [len(name) > 4 for name in username].count(True)


print(morethanfive("manuj", "anuj", "tanuj", "kaka", "rajkishore"))

print(countnamelenghtgreaterfive("manuj", "anuj", "tanuj", "kaka", "rajkishore"))

something()

print("outside", a)
print("Address of a", id(a))

