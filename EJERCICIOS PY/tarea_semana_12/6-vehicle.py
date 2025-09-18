class Vehicle:
    def __init__(self, brand, year):
        self._brand=brand
        self._year=year

    def get_info(self):
        return (f"{self._brand}, ({self._year})")


class Car(Vehicle):
    def __init__(self, brand, year, door):
        super().__init__(brand, year)
        self.door=door

    def get_info(self):
        info_base=super().get_info()
        return(f"{info_base} - {self.door} doors")

class Motorcycle(Vehicle):
    def __init__(self, brand, year, type):
        super().__init__(brand, year)
        self.type=type
    def get_info(self):
        info_base=super().get_info()
        return (f"{info_base} - type: {self.type}")
    
vehicle_1=Car("Toyota", 2020, 4)
vehicle_2=Motorcycle("Yamaha", 2022, "sport")
print(vehicle_1.get_info())
print(vehicle_2.get_info())