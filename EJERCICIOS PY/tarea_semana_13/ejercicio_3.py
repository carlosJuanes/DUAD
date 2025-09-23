"""3. Cree una clase de `User` que:
    - Tenga un atributo de `date_of_birth`.
    - Tenga un property de `age`.
    
    Luego cree un decorador para funciones que acepten un `User` como parámetro
    que se encargue de revisar si el `User` es mayor de edad y arroje una excepción de no ser así."""

from datetime import date

class User:
    def __init__(self, name, date_of_birth):
        self.name=name
        self.date_of_birth=date_of_birth
        
    @property
    def age(self):
        today = date.today()
        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )
    
def check_age(func):
    def wrapper(user, *args, **kwarg):
        if user.age<18:
            raise ValueError("Sorry! You can't come in, you're underage.")
        result=func(user, *args, **kwarg)
        return result
    return wrapper

@check_age
def enter_club(user):
    print(f"welcome {user.name} you can enter the club")
    return True

adult_user=User("carlos Juanes", date(1992, 7, 1))
minor_user=User("Alfredo Medina", date(2010,12,8))

try:
    enter_club(adult_user)
except ValueError as e:
    print(e)

try:
    enter_club(minor_user)
except ValueError as e:
    print(e)