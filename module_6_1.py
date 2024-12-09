# Родительский класс Animal
class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True  # Живой
        self.fed = False   # Накормленный

# Родительский класс Plant
class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False  # Съедобность

# Класс Mammal, наследник Animal
class Mammal(Animal):
    def eat(self, food):
        if isinstance(food, Plant):  # Проверяем, является ли объект растением
            if food.edible:  # Если растение съедобное
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:  # Если растение несъедобное
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False

# Класс Predator, наследник Animal
class Predator(Animal):
    def eat(self, food):
        if isinstance(food, Plant):  # Проверяем, является ли объект растением
            if food.edible:  # Если растение съедобное
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:  # Если растение несъедобное
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False

# Класс Flower, наследник Plant
class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)  # Наследуем атрибуты от Plant

# Класс Fruit, наследник Plant
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Переопределяем атрибут edible на True

# Создание объектов
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Вывод названий объектов
print(a1.name)  # Волк с Уолл-Стрит
print(p1.name)  # Цветик семицветик

# Проверка начальных значений атрибутов
print(a1.alive)  # True
print(a2.fed)    # False

# Хищник пытается съесть цветок
a1.eat(p1)  # Волк с Уолл-Стрит не стал есть Цветик семицветик
# Млекопитающее ест фрукт
a2.eat(p2)  # Хатико съел Заводной апельсин

# Проверка конечных значений атрибутов
print(a1.alive)  # False
print(a2.fed)    # True
