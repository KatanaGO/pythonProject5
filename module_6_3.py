import random

# Класс Animal — базовый для всех животных
class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]  # Координаты
        self.speed = speed       # Скорость

    def move(self, dx, dy, dz):
        # Перемещаем животное, умножая на скорость
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        new_z = self._cords[2] + dz * self.speed
        if new_z < 0:
            print("I'm moving underwater!")
        self._cords[2] = new_z

    def get_cords(self):
        print(f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        if self.sound:
            print(self.sound)
        else:
            print("I have nothing to say...")

# Класс Bird — описывает птиц
class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print(f"Here are(is) {random.randint(1, 4)} eggs for you")

# Класс AquaticAnimal — описывает плавающих животных
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)  # Берем модуль глубины
        self._cords[2] -= dz * (self.speed / 2)  # Уменьшаем координату z
        print("I'm diving deeper!")

# Класс PoisonousAnimal — описывает ядовитых животных
class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

# Класс Duckbill — утконос, наследуется от PoisonousAnimal, Bird и AquaticAnimal
class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)  # Инициализируем через самый первый класс в MRO

# Тестирование
db = Duckbill(10)

print(db.live)  # True
print(db.beak)  # True

db.speak()      # Click-click-click
db.attack()     # Be careful, i'm attacking you 0_0

db.move(1, 2, 3)  # Перемещение утконоса
db.get_cords()    # X: 10 Y: 20 Z: 30
db.dive_in(6)     # Ныряние утконоса
db.get_cords()    # X: 10 Y: 20 Z: 15 (или меньше, в зависимости от глубины)

db.lay_eggs()     # Here are(is) <случайное число от 1 до 4> eggs for you
