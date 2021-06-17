class ComplexNumber:
    def __init__(self, number, imag):
        self.number = number
        self.imag = imag

    def __add__(self, other):
        return complex(self.number + other.number, self.imag + other.imag)

    def __mul__(self, other):
        return complex((self.number * other.number) + (self.imag * other.imag),
                       (self.imag * other.number) + (self.number * other.imag))


number_1 = ComplexNumber(5, 3)
number_2 = ComplexNumber(4, 4)
number_3 = number_1 + number_2
number_4 = number_1 * number_2
print(number_3)
print(number_4)
