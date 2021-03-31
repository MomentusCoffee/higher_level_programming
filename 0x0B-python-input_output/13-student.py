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
        if type(attrs) is list:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return (self.__dict__)

    def reload_from_json(self, json):
        """
        Replaces all attributes of Student

        Args:
            json: replaces all attribute to json
        """
        for key, value in json.items():
            self.__dict__[key] = value
