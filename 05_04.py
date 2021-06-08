working_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open('05_04_text.txt', 'r', encoding='utf-8') as text_file:
    file_1 = open('05_04_text_2.txt', 'w', encoding='utf-8')
    for line in text_file:
        for el in working_dict:
            if line.count(el) != 0:
                result = line.replace(el, working_dict[el])
        file_1.write(result)
    file_1.close()
