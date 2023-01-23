#!/usr/bin/python3
""" Base module contains class """


class Base():
    """ base clase for checking id for other classes """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initialization base class with id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

def to_json_string(list_dictionaries):
        """ 15 return json str of list of dicts """
        if type(list_dictionaries) != list and list_dictionaries is not None:
            raise TypeError
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        for dic in list_dictionaries:
            if type(dic) != dict:
                raise TypeError
        return json.dumps(list_dictionaries)
