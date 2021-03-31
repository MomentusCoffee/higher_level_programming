#!/usr/bin/python3
"""
Base class for managing id attributes for
project 0x0C-python-almost_a_circle


"""
import json


class Base:
    """
    Base class

    Args:
        __nb_objects: counts number of id attributes created
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initiates id attribute

        Args:
            id: creates an id for specified object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Updates dictionaries to json format
        """
        if list_dictionaries is None or list_dictionaries is "":
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes a JSON string representation of list_objs
        """
        filename = cls.__name__ + ".json"
        lst = []
        if list_objs is None:
            lst = []
        else:
            for i in list_objs:
                lst.append(cls.to_dictionary(i))
        with open(filename, mode="w") as f:
            f.write(cls.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """
        Representation of dictionaries in JSON format
        """
        if json_string is None or json_string is "":
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        Creates instance with all attribute already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """
        Returns:
            List of instances
        """
        lst = []
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r") as f:
                j = f.readline()
                j = cls.from_json_string(j)
                for elem in j:
                    lst.append(cls.create(**elem))
                return (lst)
        except Exception:
            return (lst)
