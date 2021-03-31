#!/usr/bin/python3
"""
Defines Students


"""


class Student:
    """
    Class students
    """
    def __init__(self, first_name, last_name, age):
        """
        Initiates student attributes

        Args:
            first_name: students first name
            last_name: students last name
            age: students age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Dictionary Description with simple data structure

        Args:
            attrs: list of strings

        Returns:
            Dictionary Description with simple data structure
        """
        if attrs is None:
            return (self.__dict__)
        new_dict = {}
        for k, v in self.__dict__.items():
            if k in attrs:
                new_dict[k] = v
        return (new_dict)
