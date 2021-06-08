i = 0
working_list = []

with open('05_02_text.txt') as text_file:
    for line in text_file:
        i += 1
        working_list.append('В {}-ой строке присутствует {} слов'.format(i, len(line.split())))


print('В фаиле всего {} строк'.format(i))
for el in working_list:
    print(el)
