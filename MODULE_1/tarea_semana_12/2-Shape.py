from abc import ABC,abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
    
    def calculate_area(self):
        area=math.pi*self.radius**2
        return area
    
    def calculate_perimeter(self):
        perimeter=2*math.pi*self.radius
        return perimeter

class Square(Shape):
    def __init__(self, side):
        self.side=side

    def calculate_area(self):
        area=self.side*self.side
        return area
    
    def calculate_perimeter(self):
        perimeter=4*self.side
        return perimeter

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width=width
        self.height=height

    def calculate_area(self):
        area=self.width*self.height
        return area
    
    def calculate_perimeter(self):
        perimeter=2*(self.width+self.height)
        return perimeter
        
my_circle=Circle(5)
my_square=Square(10)
my_rectangle=Rectangle(5,10)
print("----------------------------")
print("CIRCLE")
print(f"The area of the circle is: {my_circle.calculate_area():.2f}")
print(f"The circumference of the circle is: {my_circle.calculate_perimeter():.2f}")
print("----------------------------")
print()
print("SQUARE")
print(f"The area of the square is: {my_square.calculate_area():.2f}")
print(f"The perimeter of the square is: {my_square.calculate_perimeter():.2f}")
print("----------------------------")
print()
print("RECTANGLE")
print(f"The area of the rectangle is: {my_rectangle.calculate_area():.2f}")
print(f"The perimeter of the rectangle is: {my_rectangle.calculate_perimeter():.2f}")
print("----------------------------")
print()