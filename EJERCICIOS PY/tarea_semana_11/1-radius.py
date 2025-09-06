import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = math.pi * self.radius**2
        return area

my_circle = Circle(5)
area = my_circle.get_area()
print(f"The area of the circle is {area:.2f}")