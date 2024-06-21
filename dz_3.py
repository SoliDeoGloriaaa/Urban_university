class Vehicle:
    def __init__(self):
        self.vehicle_type = "none"


class Car:
    def __init__(self):
        self.price = 1000000

    def house_power(self):
        """
        Не понял, зачем этот метод создавать, да и еще переопределять, если он по заданию не вызывается нигде.
        Там нужно только через print распечатать 'vehicle_type, price'.
        Поэтому оставил заглушку =)). 
        """
        pass
    
    
class Nisan(Car, Vehicle):
    def __init__(self):
        super().__init__() 
        self.price = 2000000
        self.vehicle_type = 'Переопределил'

test =  Nisan()
print(test.price)
print(test.vehicle_type)
