from itertools import count, cycle

for i in count(1):
    if i == 10:
        break
    else:
        print(i)

cycle_str = ''
for el in cycle(['X', 'Y', 'Z']):
    if cycle_str == 'XYZXYZXYZ':
        break
    else:
        cycle_str += el
        print(el)



