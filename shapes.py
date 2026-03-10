from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape"""
        pass
    @abstractmethod
    def name(self) -> str:
        """Return the name of the shape"""
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number")
        if radius <= 0:
            raise ValueError("Radius must be more than 0")
        
        self.__radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def name(self):
        return "Circle"
    
# Rectangle:
# Constructor takes: width, height


# Area formula: width × height

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, width):
        if not isinstance(width, (int, float)):
            raise TypeError("Width must be a number")
        if width <= 0:
            raise ValueError("Width must be more than 0")
        
        self.__width = width

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        if not isinstance(height, (int, float)):
            raise TypeError("Height must be a number")
        if height <= 0:
            raise ValueError("Height must be more than 0")
        
        self.__height = height

    def area(self):
        return self.width * self.height

    def name(self):
        return "Rectangle"
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @property
    def base(self):
        return self.__base
    
    @base.setter
    def base(self, base):
        if not isinstance(base, (int, float)):
            raise TypeError("Base must be a number")
        if base <= 0:
            raise ValueError("Base must be more than 0")
        
        self.__base = base

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        if not isinstance(height, (int, float)):
            raise TypeError("Height must be a number")
        if height <= 0:
            raise ValueError("Height must be more than 0")
        
        self.__height = height

    def area(self):
        return (self.base * self.height) / 2

    def name(self):
        return "Triangle"
    
def print_area(shape: Shape):
    print(f"{shape.name()} area: {shape.area():.2f}")

