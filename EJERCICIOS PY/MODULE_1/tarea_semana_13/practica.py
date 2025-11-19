from datetime import datetime


class Person:
	def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name


class User:
    def __init__(self, email, password, person):
        self.email = email
        self.password = password
        self.person = person

my_person = Person("Sarah", "Connor")
my_user = User("sconor@gmail.com", "321", my_person)

print("User: ", vars(my_user))
print("Person: ", vars(my_user.person))

"----------------------------------------------------------------"

from datetime import datetime

class Person:
	def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name


class User:
    def __init__(self, email, password, person):
        self.email = email
        self.password = password
        self.person = person

    @classmethod
    def create_user(cls, first_name, last_name, email, password):
        person = Person(first_name, last_name)
        return User(email, password, person)


my_user = User.create_user("Sarah", "Connor", "sconor@gmail.com", "321")
print("User: ", vars(my_user))
print("Person: ", vars(my_user.person))




print()
print("----------------------------------")
print("Abstract Method @abstractmethod")
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Guau!")

class Cat(Animal):
    def make_sound(self):
        print("Miau!")

# Esto funciona porque Dog implementa make_sound()
mi_perro = Dog()
mi_perro.make_sound()

# Esto daría un error (TypeError) porque la clase Animal es abstracta
# mi_animal = Animal() 

# Esto también daría un error si una subclase no implementa make_sound()
# class Fish(Animal):
#     pass
# mi_pez = Fish() # ¡Error! TypeError: Can't instantiate abstract class Fish with abstract method make_sound

print()
print("----------------------------------")
print("@property")


class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible.")
        self._celsius = value

# Creamos una instancia de la clase
temp = Temperature(25)

# Accedemos a la temperatura en Fahrenheit como si fuera un atributo
print(f"Temperatura en Fahrenheit: {temp.fahrenheit}°F") # Output: 77.0°F

# Intentamos cambiar la temperatura en Celsius (lo cual valida el setter)
try:
    temp.celsius = -300
except ValueError as e:
    print(f"Error: {e}") # Output: Error: Temperature below absolute zero is not possible.

# El getter (@property) para obtener el valor.

# El setter (@property_name.setter) para modificar el valor de forma controlada.

# El uso de _ (guion bajo) en _celsius para indicar que es un atributo "privado" o para uso interno.
    
print()
print("----------------------------------")
print("@classmethod")
from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def from_birth_year(cls, name, year):
        age = date.today().year - year
        return cls(name, age)

# Usamos el constructor normal (__init__)
person1 = Person("Alice", 30)
print(f"{person1.name} tiene {person1.age} años.")

# Usamos el constructor alternativo (@classmethod)
person2 = Person.from_birth_year("Bob", 1995)
print(f"{person2.name} tiene {person2.age} años.")