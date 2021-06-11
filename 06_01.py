import time


class TrafficLight:
    __color_time_dict = {'красный': 7, 'желтый': 3, 'зеленый': 5}
    __color_list = ['красный', 'желтый', 'зеленый', 'ключ']

    def __init__(self, color):
        self.__color = color

    def running(self):
        while self.__color != 'ключ':
            print(f'Горит {self.__color} цвет. Пауза - {self.__color_time_dict[self.__color]} секунд')
            time.sleep(self.__color_time_dict[self.__color])
            self.__color = self.__color_list[self.__color_list.index(self.__color) + 1]
        else:
            print('Цикл завершен')


light_first = TrafficLight('красный')
light_first.running()

light_second = TrafficLight('зеленый')
light_second.running()
