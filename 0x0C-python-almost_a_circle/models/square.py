#!/usr/bin/python3
"""
Create a Square


"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Creates a Square that inherits attributes of a Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initiates attributes of a square

        Args:
            size: size of a square
            x: horizontal position of square
            y: vertical position of square
            id: id of square

        Note**
            The attribute size is assigned the value of width and height
            from Rectangle.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Property for size of Square

        Args:
            size(int): size of square

        Returns:
            The value of size

        Note**
            Using inherited width attribute to represent square
        """
        return (self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """
        Overrides Rectangle method of __str__

        Returns:
            size instead of width or height
        """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.size))

    def update(self, *args, **kwargs):
        """
        Updates the __str__ attributes values
        """
        if len(args) == 0:
            for k, v in kwargs.items():
                setattr(self, k, v)

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):
        """
        Creates a dictionary
        """
        seq = {"id": self.id, "size": self.size,
               "x": self.x, "y": self.y}
        return (seq)
