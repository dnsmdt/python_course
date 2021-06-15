class Matrix:
    def __init__(self, number_list):
        self.number_list = number_list

    def __str__(self):
        matrix = ''
        for el in self.number_list:
            matrix += f'{el} \n'
        return matrix

    def __add__(self, other):
        result_list = []
        inter_list = []
        i = 0
        for el_1 in self.number_list:
            for number in el_1:
                inter_list.append(number + other.number_list[self.number_list.index(el_1)][i])
                if i < len(el_1) - 1:
                    i += 1
                else:
                    result_list.append(inter_list)
                    inter_list = []
                    i = 0
        return Matrix(result_list)


a = Matrix([[30, 22], [10, 20]])
b = Matrix([[10, 51], [12, 24]])
print(a)
print(b)
print(a + b)
