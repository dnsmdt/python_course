input_v = ''

with open('05_01_text.txt', 'w') as text_file:
    while input_v != '\n':
        input_v = input('Введите строку для записи: (пробел прерывает цикл): ') + '\n'
        text_file.write(input_v)

print('Запись завершена')
