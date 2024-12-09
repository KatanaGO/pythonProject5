import math

# Базовый класс Figure
class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color) if self.__is_valid_color(*color) else [0, 0, 0]
        self.filled = True
        if len(sides) == self.sides_count and self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count

    def get_color(self):
        """Возвращает текущий цвет (RGB)."""
        return self.__color

    def set_color(self, r, g, b):
        """Устанавливает новый цвет, если он корректен."""
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print("Некорректные значения цвета.")

    def __is_valid_color(self, r, g, b):
        """Проверяет корректность цвета (RGB)."""
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def __is_valid_sides(self, *sides):
        """Проверяет корректность сторон."""
        return all(isinstance(s, (int, float)) and s > 0 for s in sides)

    def get_sides(self):
        """Возвращает текущие стороны фигуры."""
        return self.__sides

    def set_sides(self, *new_sides):
        """Изменяет стороны, если количество сторон совпадает с `sides_count`."""
        if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            print("Некорректные значения сторон.")

    def __len__(self):
        """Возвращает периметр фигуры."""
        return sum(self.__sides)


# Класс Circle (круг)
class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        """Возвращает площадь круга."""
        return math.pi * (self.__radius ** 2)


# Класс Triangle (треугольник)
class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        """Возвращает площадь треугольника (по формуле Герона)."""
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


# Класс Cube (куб)
class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == 1 and self._Figure__is_valid_sides(*sides):
            self.set_sides(*([sides[0]] * 12))

    def get_volume(self):
        """Возвращает объем куба."""
        edge = self.get_sides()[0]
        return edge ** 3


circle1 = Circle((200, 200, 100), 10)  # Круг с цветом (RGB) и длиной окружности
cube1 = Cube((222, 35, 130), 6)  # Куб с цветом (RGB) и длиной ребра

# Проверка изменения цветов:
circle1.set_color(55, 66, 77)  # Цвет изменится
print(circle1.get_color())  # Ожидаемый вывод: [55, 66, 77]

cube1.set_color(300, 70, 15)  # Некорректное значение, цвет не изменится
print(cube1.get_color())  # Ожидаемый вывод: [222, 35, 130]

# Проверка изменения сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Некорректное количество сторон, не изменится
print(cube1.get_sides())  # Ожидаемый вывод: [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]

circle1.set_sides(15)  # Количество сторон корректно, изменится
print(circle1.get_sides())  # Ожидаемый вывод: [15]

# Проверка длины окружности (периметра круга):
print(len(circle1))  # Ожидаемый вывод: 15

# Проверка объёма куба:
print(cube1.get_volume())  # Ожидаемый вывод: 216
