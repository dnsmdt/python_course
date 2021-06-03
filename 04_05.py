from functools import reduce

first_list = [el for el in range(100, 1001)]
print(reduce(lambda x, y: x + y, first_list))
