#!/usr/bin/python3
"""
Creates a Rectangle


"""
from models.base import Base


class Rectangle(Base):
    """
    Creates a Rectangle that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initiates parameters of Rectangle

        Args:
            width: measurements of rectangle
            height: measurements of rectangle
            x: hoizontal position of rectangle
            y: vertical position of rectangle
            id: id of rectangle inherited from Base
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def integer_validator(self, name, value):
        """
        Checks if objects are of type int
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if (name == "width" or name == "height") and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if (name == "x" or name == "y") and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """
        Property getter/setter

        Used to get/set the width of rectangle

        Args:
            width(int): width of rectangle

        Returns:
            The value of width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """
        Property getter/setter

        Used to get/set the height of rectangle

        Args:
            height(int): height of rectangle

        Returns:
            The value of height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """
        Property getter/setter

        Used to get/set the horizontal position of rectangle

        Args:
            x(int): horizontal position of rectangle

        Returns:
            The horizontal position
        """
        return (self.__x)

    @x.setter
    def x(self, pos):
        self.integer_validator("x", pos)
        self.__x = pos

    @property
    def y(self):
        """
        Property getter/setter

        Used to get/set the vertical position of rectangle

        Args:
            y(int): vertical position of rectangle

        Returns:
            The vertical position
        """
        return (self.__y)

    @y.setter
    def y(self, pos):
        self.integer_validator("y", pos)
        self.__y = pos

    def area(self):
        """
        Returns:
            The area of a rectangle
        """
        return (self.__width * self.__height)

    def display(self):
        """
        Prints rectangle represented by #
        """
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Overrides default __str__

        Returns:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """
        Updates arguments passed in __str__

        Args:
            args: object to be updated

        Returns:
            Updated __str__
        """
        if len(args) == 0:
            for k, v in kwargs.items():
                setattr(self, k, v)

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """
        Creates a dictionary
        """
        seq = {"id": self.id, "width": self.width,
               "height": self.height, "x": self.x, "y": self.y}
        return (seq)
