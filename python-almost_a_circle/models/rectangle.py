#!/usr/bin/python3
"""class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """
    A class representing a rectangle, which inherits from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle object with the given width, height,
        x-coordinate, y-coordinate, and id.

        Parameters:
        - width (int): the width of the rectangle
        - height (int): the height of the rectangle
        - x (int, optional): the x-coordinate of the rectangle (default is 0)
        - y (int, optional): the y-coordinate of the rectangle (default is 0)
        - id (int, optional): the id of the rectangle (default is None)
        """
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Get the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Set the width of the rectangle to the given value.

        Parameters:
        - width (int): the new width of the rectangle
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
        Get the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Set the height of the rectangle to the given value.

        Parameters:
        - height (int): the new height of the rectangle
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
        Get the x-coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        Set the x-coordinate of the rectangle to the given value.

        Parameters:
        - x (int): the new x-coordinate of the rectangle
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
        Get the y-coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        Set the y-coordinate of the rectangle to the given value.

        Parameters:
        - y (int): the new y-coordinate of the rectangle
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """method that calculate area"""
        return self.width*self.height

    def display(self):
        """method that print "#" by form area """
        x = 0
        n = 0
        while n < self.y:
            print()            
            n = n + 1
        while x < self.height:
            y = 0
            m = 0
            while y < self.width:
                while m < self.x:
                    print(" ",end="")
                    m = m + 1
                print("#", end="")
                y = y + 1
            print()
            x = x + 1

    def __str__(self):
        """method __str__ print rectangle atributes"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
        self.width, self.height)

    def update(self, *args, **kwargs):
        """ method print args """
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "height":
                    self.height = value
                if key == "width":
                    self.width = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
        else:
            if args:
                self.id = args[0]
            if len(args) >= 2 and args[1] is not None:
                self.width = args[1]
            if len(args) >= 3 and args[2] is not None:
                self.height = args[2]
            if len(args) >= 4 and args[3] is not None:
                self.x = args[3]
            if len(args) >= 5 and args[4] is not None:
                self.y = args[4]

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
        self.width, self.height)
