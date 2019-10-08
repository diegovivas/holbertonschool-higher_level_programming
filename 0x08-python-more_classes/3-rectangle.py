#!/usr/bin/python3
class Rectangle:
    def __str__(self):
        if self.__width != 0 and self.__height != 0:
            strin = "#" * self.__width + "\n"
            strin = strin * self.__height
            return strin[:-1]
        else:
            return ("")

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height != 0 and self.__width != 0:
            return ((self.__height * 2) + (self.__width * 2))
        else:
            return 0
