def fibonaccisereis(num):
    result = []

    x, y = 0, 1
    while x < num:
        result.append(x)
        x, y = y, x+y
    return result

