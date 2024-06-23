class Vehicle:
    def __init__(self):
        self.vehicle_type = "none"


class Car:
    def __init__(self):
        self.price = 1000000
        self.house_powers = 78

    def house_power(self):
        return self.house_powers
    
    
class Nisan(Car, Vehicle):
    def __init__(self):
        super().__init__() 
        self.price = 2000000
        self.vehicle_type = 'Переопределил'
        self.house_powers = 150

test =  Nisan()
print(test.price)
print(test.vehicle_type)
print(test.house_powers) 