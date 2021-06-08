final_dict = {}

with open('05_06_text.txt', 'r', encoding='utf-8') as text_file:
    for line in text_file:
        val = line[line.index(':')+2:]  # [+ 2] для того, чтобы он не включал в себя двоеточие и последующий пробел
        val = val.split()
        working_list = [int(x[:x.index('(')]) for x in val]
        final_dict[line[:line.index(':')]] = sum(working_list)

print(final_dict)
