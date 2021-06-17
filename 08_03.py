class IsInt(Exception):
    @staticmethod
    def check():
        check_list = []
        while True:
            check_input = input('Введите число: ')
            try:
                check_input = int(check_input)
            except ValueError:
                print('Ошибка: вы ввели не число')
            else:
                check_list.append(check_input)
            question = input('Хотите продолжить добавление чисел? (Напишите "stop", если хотите прекратить)')
            if question == 'stop':
                print(check_list)
                break
            else:
                continue


IsInt.check()
