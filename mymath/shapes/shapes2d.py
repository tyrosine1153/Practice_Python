from mymath.shapes import PI


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return PI * self.radius * self.radius


class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length