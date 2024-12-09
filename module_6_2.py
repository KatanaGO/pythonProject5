# Родительский класс Vehicle
class Vehicle:
    # Атрибут класса - список допустимых цветов
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner  # Владелец транспорта
        self.__model = model  # Модель транспорта
        self.__color = color  # Цвет транспорта
        self.__engine_power = engine_power  # Мощность двигателя

    # Метод для получения модели
    def get_model(self):
        return f"Модель: {self.__model}"

    # Метод для получения мощности двигателя
    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    # Метод для получения цвета
    def get_color(self):
        return f"Цвет: {self.__color}"

    # Метод для вывода информации об объекте
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    # Метод для изменения цвета
    def set_color(self, new_color):
        # Проверяем, есть ли новый цвет в списке допустимых цветов
        if new_color.lower() in [color.lower() for color in self.__COLOR_VARIANTS]:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


# Класс Sedan, наследник Vehicle
class Sedan(Vehicle):
    # Константа - лимит пассажиров
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, color, engine_power):
        # Вызываем конструктор родительского класса
        super().__init__(owner, model, color, engine_power)


# Создание объекта класса Sedan
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Попытка смены цвета
vehicle1.set_color('Pink')  # Нельзя сменить цвет на Pink
vehicle1.set_color('BLACK')  # Сменим цвет на BLACK
vehicle1.owner = 'Vasyok'  # Меняем владельца

# Проверка изменений
vehicle1.print_info()
