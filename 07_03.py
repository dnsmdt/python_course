class Cell:
    def __init__(self, number_of_cells):
        self.number_of_cells = number_of_cells

    def __add__(self, other):
        return Cell(self.number_of_cells + other.number_of_cells)

    def __sub__(self, other):
        if self.number_of_cells - other.number_of_cells > 0:
            return Cell(self.number_of_cells - other.number_of_cells)
        else:
            print('Операция невозможна')

    def __mul__(self, other):
        return Cell(self.number_of_cells * other.number_of_cells)

    def __truediv__(self, other):
        return Cell(int(self.number_of_cells / other.number_of_cells))

    def make_order(self):
        i = 0
        work_str = ''
        for el in range(self.number_of_cells):
            if i == 4:
                work_str += '*\n'
                i = 0
            else:
                work_str += '*'
                i += 1
        return work_str


a = Cell(100)
b = Cell(21)
c = b.make_order()
print(c)

