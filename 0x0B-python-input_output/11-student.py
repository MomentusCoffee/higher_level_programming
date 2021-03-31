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

    def to_json(self):
        """
        Dictionary Description with simple data structure
        """
        return (self.__dict__)
