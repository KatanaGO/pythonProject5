# Родительский класс для животных
class Animal:
    alive = True  # Атрибут класса: живой
    fed = False   # Атрибут класса: накормленный

    def __init__(self, name):
        self.name = name  # Имя животного

    def eat(self, food):
        if isinstance(food, Plant):  # Проверяем, что food является растением
            if food.edible:  # Если растение съедобное
                print(f"{self.name} съел {food.name}")
                self.__class__.fed = True  # Меняем класс-атрибут fed на True
            else:  # Если растение несъедобное
                print(f"{self.name} не стал есть {food.name}")
                self.__class__.alive = False  # Меняем класс-атрибут alive на False
        else:
            print("Это не растение!")

# Родительский класс для растений
class Plant:
    edible = False  # Атрибут класса: съедобность

    def __init__(self, name):
        self.name = name  # Имя растения

# Класс "Млекопитающие" (наследник Animal)
class Mammal(Animal):
    pass  # Поведение полностью унаследовано от Animal

# Класс "Хищник" (наследник Animal)
class Predator(Animal):
    pass  # Поведение полностью унаследовано от Animal

# Класс "Цветок" (наследник Plant)
class Flower(Plant):
    pass  # Цветы остаются несъедобными, ничего менять не нужно

# Класс "Фрукт" (наследник Plant)
class Fruit(Plant):
    edible = True  # Переопределяем атрибут класса: фрукты съедобны

# Тестирование
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)  # Вывод: Волк с Уолл-Стрит
print(p1.name)  # Вывод: Цветик семицветик

print(a1.alive)  # Вывод: True
print(a2.fed)    # Вывод: False
a1.eat(p1)       # Вывод: Волк с Уолл-Стрит не стал есть Цветик семицветик
a2.eat(p2)       # Вывод: Хатико съел Заводной апельсин
print(a1.alive)  # Вывод: False
print(a2.fed)    # Вывод: True
