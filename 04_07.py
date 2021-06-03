def fact(x):
    y = 1
    for i in range(1, x):
        y += y * i
        yield y


for el in fact(4):
    print(el)
