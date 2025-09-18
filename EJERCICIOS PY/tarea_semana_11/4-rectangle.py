class Rectangle:
    def __init__(self, width, height):
        if width <0 or height <0:
            raise ValueError("There is a negative value, the values ​​must be positive")
        self.width=width
        self.height=height

    def get_area(self):
        area=self.width*self.height
        return area
        

    def get_perimeter(self):
        perimeter=2*(self.width+self.height)
        return perimeter
try:
    width=float(input("Please enter the width: "))
    height=float(input("Please enter the height: "))

    my_rectangle=Rectangle(width, height)
    my_area=my_rectangle.get_area()
    my_perimeter=my_rectangle.get_perimeter()
    print(f"The area is: {my_area}")
    print(f"The perimeter is: {my_perimeter}")
except ValueError as e:
     print (e)

