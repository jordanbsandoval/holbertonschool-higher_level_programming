#!/usr/bin/python3
""" 1-rectangle.py: Defines rectangle based on 0-rectangle.py
"""


class Rectangle:
    """ Define Class with validated private instance
        attributes width and height
    """

    def __init__(self, width=0, height=0):
        """Initializes rectangle size"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Defines width of the rectangle and returns its value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Defines the value of width of rectangle and checks if >= 0"""

        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Defines height of the rectangle and returns its value"""

        return self.__height

    @height.setter
    def height(self, value):
        """Defines the value of height of rectangle and checks if >= 0"""

        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value