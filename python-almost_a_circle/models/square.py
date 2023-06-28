#!/usr/bin/python3
"""Here is the module description"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Description of the the class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor function"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns formatted string"""
        coordinates = f"{self.__x}/{self.__y}"
        return f"[Square] ({self.id}) {coordinates} - {self.width}"

    @property
    def size(self):
        """Get the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """"Sets the size value with validation"""
        self.width = type(self).dimension_validator(self, "width", value)
        self.height = type(self).dimension_validator(self, "height", value)

    @property
    def x(self):
        """Get the x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """Validates the x value"""
        self.__x = type(self).coordinate_validator(self, "x", value)

    @property
    def y(self):
        """Get the y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """Validates the y value"""
        self.__y = type(self).coordinate_validator(self, "y", value)

    def dimension_validator(self, name, value):
        """"Validates the width and height values as positive integers"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(name))
        else:
            return value

    def coordinate_validator(self, name, value):
        """"Validates the x and y values as positive integers"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(name))
        else:
            return value

    def area(self):
        """Returns the area of a circle"""
        return self.__width * self.__height

    def display(self):
        """ prints in stdout the Rectangle instance with the character #"""
        print("\n" * self.__y, end="")
        for row in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """Updates attributes of instance"""
        if args:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
        else:
            try:
                self.id = kwargs['id']
            except KeyError:
                pass
            try:
                self.__width = kwargs['width']
            except KeyError:
                pass
            try:
                self.__height = kwargs['height']
            except KeyError:
                pass
            try:
                self.__x = kwargs['x']
            except KeyError:
                pass
            try:
                self.__y = kwargs['y']
            except KeyError:
                pass
