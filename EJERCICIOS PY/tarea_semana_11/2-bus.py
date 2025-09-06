class Person:
    def __init__(self, name):
        self.name = name


class Bus:
    
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        if len(self.passengers) >= self.max_passengers:
            print("The maximum passenger limit has been reached")
            return
        else:
            self.passengers.append(person)

    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f"The passenger {person.name} has gotten off the bus")
        else:
            print(f"The passenger {person.name} was not found on the bus")

    def print_passengers(self):
        print("--------PASSENGERS ON BOARD--------")
        if not self.passengers:
            print("There are no passengers on board yet")
        else:
            for i, passenger in enumerate(self.passengers):
                print(f"{i+1}-{passenger.name}")
        print("---------------------------------")


school_bus = Bus(5)
passenger_1 = Person("Carlos")
passenger_2 = Person("Alfredo")
passenger_3 = Person("Juanes")
passenger_4 = Person("Medina")
passenger_5 = Person("Juan")
passenger_6 = Person("Pedro")
passenger_7 = Person("Lucas")

school_bus.add_passenger(passenger_1)
school_bus.add_passenger(passenger_2)
school_bus.add_passenger(passenger_3)
school_bus.add_passenger(passenger_4)
school_bus.add_passenger(passenger_5)
school_bus.print_passengers()
school_bus.add_passenger(passenger_6)
school_bus.remove_passenger(passenger_5)
school_bus.remove_passenger(passenger_2)
school_bus.print_passengers()
school_bus.add_passenger(passenger_5)
school_bus.print_passengers()
school_bus.remove_passenger(passenger_7)