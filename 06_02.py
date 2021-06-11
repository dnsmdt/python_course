class Road:

    def __init__(self, weight, length, mass_for_one, depth):
        self._weight = weight
        self._length = length
        self._mass_for_one = mass_for_one
        self._depth = depth

    def weight_of_road(self):
        result = (self._weight * self._length * self._mass_for_one * self._depth) / 1000
        print(f'Масса асфальта, необходимого для покрытия всей дороге равна {int(result)} Т')


first_road = Road(20, 5000, 25, 5)
first_road.weight_of_road()
