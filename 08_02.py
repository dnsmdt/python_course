class Operation(Exception):
    @classmethod
    def division_method(cls, number_1, number_2):
        try:
            result = int(number_1 / number_2)
        except ZeroDivisionError:
            print('Ошибка: невозможно делить на ноль')
        else:
            print(f'Результат - {result}')


Operation.division_method(3, 1)
