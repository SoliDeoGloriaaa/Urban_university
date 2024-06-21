class Vehicle:
    _COLOR_VARIANTS = ['Зеленый', 'Красный', 'Черный', 'Белый', 'Black']
    
    def __init__(self, owner, __modelv, __color, __engine_power) -> None:
        self.owner = owner
        self.__modelv = __modelv
        self. __engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return f'Модель: {self.__modelv}\n'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}\n'

    def get_color(self):
        return f'Цвет: {self.__color}\n'

    def print_info(self):
        print(self.get_model(), self.get_horsepower(), self.get_color(), 'Владелец:',  self.owner)

    def set_color(self, new_color):
        if new_color.lower().capitalize() in self._COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Невозможно покрасить в {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5



# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

# Модель: Toyota Mark II
# Мощность двигателя: 500
# Цвет: blue
# Владелец: Fedos
# Невозможно покрасить в Pink
# Модель: Toyota Mark II
# Мощность двигателя: 500
# Цвет: BLACK
# Владелец: Vasyok