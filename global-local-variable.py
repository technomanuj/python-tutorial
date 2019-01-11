a = 10


def something():
    global a
    a = 15
    print("Local", a)
    print("Address of a", id(a))



something()

print("outside", a)
print("Address of a", id(a))

