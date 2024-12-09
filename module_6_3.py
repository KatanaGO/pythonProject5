import random

# Родительский класс Animal
class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0  # Уровень опасности

    def __init__(self, speed):
        self._cords = [0, 0, 0]  # Координаты в пространстве
        self.speed = speed  # Скорость передвижения

    def move(self, dx, dy, dz):
        """Изменение координат с учетом скорости."""
        if self._cords[2] + dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
            return
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        self._cords[2] += dz * self.speed

    def get_cords(self):
        """Вывод текущих координат."""
        print(f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}")

    def attack(self):
        """Атака в зависимости от степени опасности."""
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        """Издает звук."""
        if self.sound:
            print(self.sound)
        else:
            print("...")

# Класс Bird
class Bird(Animal):
    beak = True  # Наличие клюва

    def lay_eggs(self):
        """Откладывает яйца."""
        eggs = random.randint(1, 4)
        print(f"Here are(is) {eggs} eggs for you")

# Класс AquaticAnimal
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3  # Уровень опасности

    def dive_in(self, dz):
        """Ныряет, изменяя координату Z."""
        dz = abs(dz)  # Берем модуль dz
        if self._cords[2] - dz * (self.speed / 2) < 0:
            print("It's too deep, i can't dive :(")
            return
        self._cords[2] -= dz * (self.speed / 2)

# Класс PoisonousAnimal
class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8  # Уровень опасности

# Класс Duckbill (утконос)
class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"  # Звук утконоса

    def __init__(self, speed):
        super().__init__(speed)  # Инициализация через Animal

# Пример работы программы
db = Duckbill(10)

# Проверка свойств
print(db.live)  # Утконос жив
print(db.beak)  # Утконос имеет клюв

# Утконос издает звук
db.speak()

# Утконос атакует
db.attack()

# Утконос перемещается
db.move(1, 2, 3)
db.get_cords()

# Утконос ныряет
db.dive_in(6)
db.get_cords()

# Утконос откладывает яйца
db.lay_eggs()
