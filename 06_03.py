class Worker:
    _income = {}

    def __init__(self, name='Jake', surname='Smith', position='Manager', wage_val=20000, bonus_val=500):
        self.name = name
        self.surname = surname
        self.position = position
        self._income['wage'] = wage_val
        self._income['bonus'] = bonus_val


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(f'Доход сотрудника полностью - {self._income["wage"] + self._income["bonus"]} ')


worker_1 = Position('John', 'Small', 'Fisherman', 10000, 20)
print(worker_1.position)
worker_1.get_full_name()
worker_1.get_total_income()
