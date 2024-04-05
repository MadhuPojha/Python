"""
Create a Python program that explores polymorphism using a hierarchy of shapes. 
Start with a base class Shape, and then create two or more derived classes (e.g., Circle, Rectangle, Triangle) that inherit from the Shape class. 
Each shape class should have its own implementation of methods like area() and perimeter(). 
These methods will calculate the area and perimeter of the respective shape.
1.
Define the Shape base class with methods like area() and perimeter(). You can initialize any common attributes in the base class.
2.
Create derived classes for different shapes, e.g., Circle, Rectangle, and Triangle. 
 Each derived class should inherit from the Shape base class and implement its own version of the area() and perimeter() methods.
3.
Implement specific methods for each derived class. For example, the Circle class might have a method to calculate its area based on the radius, 
and the Rectangle class could have a method to calculate its area based on length and width.
Create instances of each shape type and demonstrate the use of polymorphism by calling the area() and perimeter() methods on them.
"""

class Shapes():

    pi = 3.14
    def __init__(self):
        pass


class Circle(Shapes):
    pi = 3.14
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def area(self):                 # method for calculate the area of circle
        return self.pi * self.radius**2
    
    def perimeter(self):
        return 2 * self.pi * self.radius

class Rectangle(Shapes):
    def __init__(self, width, length):
        super().__init__()
        self.width = width
        self.length = length

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shapes):
    def __init__(self, base, height, side1, side2, side3):
        super().__init__()
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

circle = Circle(7)
print("Area of circle is:", circle.area()) # Area of circle is: 153.86
print("Perimeter of circle is:", circle.perimeter()) # Perimeter of circle is: 43.96

rectangle = Rectangle(5, 7) 
print("Area of Rectangle is:", rectangle.area()) # Area of Rectangle is: 35
print("Perimeter of Rectangle is:", rectangle.perimeter()) # Perimeter of Rectangle is: 24

triangle = Triangle(5, 4, 4, 3, 5)
print("Area of Triangle is:", triangle.area()) # Area of Triangle is: 10.0
print("Perimeterof Triangle is:", triangle.perimeter())  # Perimeterof Triangle is: 12

