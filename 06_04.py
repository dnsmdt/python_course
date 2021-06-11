class Car:
    speed = 30
    color = 'white'
    name = 'Lada'
    is_police = False

    def go(self):
        print('Автомобиль поехал!')

    def stop(self):
        print('Автомобиль остановился')

    def turn(self, direction):
        if direction == 'Left':
            print('Машина повернулась налево')
        else:
            print('Машина повернулась направо')

    def show_speed(self):
        print(f'Скорость - {self.speed}')


class TownCar(Car):
    speed = 60

    def show_speed(self):
        print(f'Скорость - {self.speed}')
        print('Внимание: вы превысили лимит скорости!')


class WorkCar(Car):
    speed = 40

    def show_speed(self):
        print(f'Скорость - {self.speed}')
        print('Внимание: вы превысили лимит скорости!')


class SportCar(Car):
    speed = 100


class PoliceCar(Car):
    is_police = True


car_1 = WorkCar()
car_1.show_speed()
car_2 = TownCar()
car_2.show_speed()
