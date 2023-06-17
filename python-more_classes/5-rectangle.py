#!/usr/bin/python3
"""
Rectangle class example
"""


class Rectangle:
    """
    Rectangle class with width and height
    """

    def __init__(self, width=0, height=0):
        """
        initstantiation of rectangle

        arguments:
        width
        height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """get height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return int(self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return_string = ""
        for i in range(self.__height):
            if i == self.__height - 1:
                return_string = return_string + '#' * self.__width
            else:
                return_string = return_string + '#' * self.__width + '\n'
        return return_string

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
