class Animal:
    def __init__(self, name):
        self.name=name

    def speak(self):
        print(f"{self.name} makes sound")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        return "Guau"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "Miau"

my_dog=Dog("fidel")
print(my_dog.speak())

my_cat=Cat("fu")
print(my_cat.speak())

