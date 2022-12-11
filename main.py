class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self._a * self._b


main_rect = Rectangle(5, 4)
