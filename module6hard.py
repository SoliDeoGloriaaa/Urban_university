class Figure:
    sides_count = 0

    def __init__(self, __sides, __color, filled) -> None:
        self.__sides = __sides
        self.__color = __color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        pass

    def set_color(self, r, g, b):
        pass

    def set_sides(self, *args):
        pass

    def __is_valid_sides(self, *args):
        pass

    def __len__(self):
        pass


class Circle(Figure):
    sides_count = 1

    def __init__(self, __sides, __color, filled, __radius) -> None:
        super().__init__(__sides, __color, filled)
        self.__radius = __radius

    def get_square(self):
        """Возвращает площать круга."""
        pass


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __sides, __color, filled, __height) -> None:
        super().__init__(__sides, __color, filled)
        self.__height = __height

    def get_square(self):
        """Возвращает площать треугольника."""
        pass


class Cube(Figure):
    sides_count = 12

    def __init__(self, __sides) -> None:
        super().__init__(__sides)

    def get_volume(self):
        """Возвращает объем куба."""
        pass


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15)  # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


