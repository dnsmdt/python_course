class Warehouse:
    name = 'Склад'
    storage = {}
    i = 1

    def __init__(self, name):
        self.name = name

    def __setitem__(self, key, value):
        self.storage[key] = value

    def __getitem__(self, key):
        return self.storage[key]


class StrError(Exception):
    pass


class Unusual(Exception):
    pass


class OfficeEquipment:
    name = 'Оргтехника'
    quantity = None
    weight = None
    height = None

    def acceptance_warehouse(self, warehouse, unit):
        inter_str = [f'Подразделение: {unit}']
        return inter_str


class Printer(OfficeEquipment):
    name = 'Принтер'
    model = 'HP 4000'
    printer_type = ''

    def __init__(self, model, quantity, printer_type, weight, height):
        try:
            self.model = model
            self.quantity = quantity
            self.printer_type = printer_type
            self.weight = weight
            self.height = height
            if type(quantity) == str or type(weight) == str or type(height) == str:
                raise StrError('Ошибка: вы ввели строку, а не число')
            elif quantity > 1000 or weight > 10 or height > 2:
                raise Unusual('Некоторые показатели выглядят подозрительно (слишком завышенные данные)\n'
                              'Пожалуйста, перепроверьте и повторите процедуру')
        except StrError as err:
            print(err)
        except Unusual as err_2:
            print(err_2)
        else:
            print(f'|{self.name} {self.model}|\n'
                  'Данные введены верно \n', 'Проверка прошла удачно')

    def acceptance_warehouse(self, warehouse, unit):
        inter_str = OfficeEquipment.acceptance_warehouse(self, warehouse, unit)
        inter_str.extend([self.name, self.model, self.printer_type, f'{self.quantity} шт',
                          f'{self.weight} kg', f'{self.height} m'])
        warehouse.storage[f'{warehouse.i}'] = inter_str
        warehouse.i += 1


class Scanner(OfficeEquipment):
    name = 'Cканер'
    model = 'Kodak Alaris S2060'
    scanner_type = ''

    def __init__(self, model, quantity, scanner_type, weight, height):
        try:
            self.model = model
            self.quantity = quantity
            self.scanner_type = scanner_type
            self.weight = weight
            self.height = height
            if type(quantity) == str or type(weight) == str or type(height) == str:
                raise StrError('Ошибка: вы ввели строку, а не число')
            elif quantity > 1000 or weight > 10 or height > 2:
                raise Unusual('Некоторые показатели выглядят подозрительно (слишком завышенные данные)\n'
                              'Пожалуйста, перепроверьте и повторите процедуру')
        except StrError as err:
            print(err)
        except Unusual as err_2:
            print(err_2)
        else:
            print(f'|{self.name} {self.model}|\n'
                  'Данные введены верно \n', 'Проверка прошла удачно')

    def acceptance_warehouse(self, warehouse, unit):
        inter_str = OfficeEquipment.acceptance_warehouse(self, warehouse, unit)
        inter_str.extend([self.name, self.model, self.scanner_type, f'{self.quantity} шт',
                          f'{self.weight} kg', f'{self.height} m'])
        warehouse.storage[f'{warehouse.i}'] = inter_str
        warehouse.i += 1


class Xerox(OfficeEquipment):
    name = 'Ксерокс'
    model = 'CANON C3720I'
    xerox_type = ''

    def __init__(self, model, quantity, xerox_type, weight, height):
        try:
            self.model = model
            self.quantity = quantity
            self.xerox_type = xerox_type
            self.weight = weight
            self.height = height
            if type(quantity) == str or type(weight) == str or type(height) == str:
                raise StrError('Ошибка: вы ввели строку, а не число')
            elif quantity > 1000 or weight > 10 or height > 2:
                raise Unusual('Некоторые показатели выглядят подозрительно (слишком завышенные данные)\n'
                              'Пожалуйста, перепроверьте и повторите процедуру')
        except StrError as err:
            print(err)
        except Unusual as err_2:
            print(err_2)
        else:
            print(f'|{self.name} {self.model}|\n'
                  'Данные введены верно \n', 'Проверка прошла удачно')

    def acceptance_warehouse(self, warehouse, unit):
        inter_str = OfficeEquipment.acceptance_warehouse(self, warehouse, unit)
        inter_str.extend([self.name, self.model, self.xerox_type, f'{self.quantity} шт',
                          f'{self.weight} kg', f'{self.height} m'])
        warehouse.storage[f'{warehouse.i}'] = inter_str
        warehouse.i += 1


def pretty_show_of_storage(depot):
    print(f'|Перечень вещей на складе {depot.name}|')
    for el in depot.storage:
        print(f'{el}. {depot.storage[el]}')


warehouse_192 = Warehouse('Н192')
printer_1 = Printer('Kodak Alaris S2060', 3, 'Струйный', 1.5, 0.2)
printer_1.acceptance_warehouse(warehouse_192, 'Центральный')
scanner_2 = Scanner('HX 3910', 3, 'Барабанный', 5, 0.5)
scanner_2.acceptance_warehouse(warehouse_192, 'Офис на Бутырской')
xerox_3 = Xerox('WG9', 1, 'Многофункциональный', 2, 0.5)
xerox_3.acceptance_warehouse(warehouse_192, 'Офис в Мурино')

pretty_show_of_storage(warehouse_192)
