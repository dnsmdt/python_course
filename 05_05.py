with open('05_05_text.txt', 'w') as text_file:
    text_file.write(input('Введите набор чисел, разделенных пробелом: '))


with open('05_05_text.txt', 'r') as text_file:
    result = [int(x) for x in text_file.read().split()]
    print(sum(result))
