class Stationery:
    title = 'Канцелярская принадлежность'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    title = 'Ручка'

    def draw(self):
        print('Начало рисования ручкой')


class Pencil(Stationery):
    title = 'Карандаш'

    def draw(self):
        print('Начало рисования карандашом')


class Handle(Stationery):
    title = 'Маркер'

    def draw(self):
        print('Начало рисования маркером')


pen_1 = Pen()
pencil_1 = Pencil()
handle_1 = Handle()

pen_1.draw()
pencil_1.draw()
handle_1.draw()
