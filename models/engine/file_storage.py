#!/usr/bin/python3
"""This is a file storag module for the hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class FileStorage:
    """Manage a class for the class format of the file storage"""
    __file_path = 'file.json'
    __objects = {}

    def delete(self,obj=None):
        """Delet an exsisting object"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def all(self, cls=None):
        """Return a dictionary of models currently in storage to the object"""
        dic = {}
        if cls:
            dictionary = self.__objects
            for m in dictionary:
                partition = m.replace('.', ' ')
                partition = shlex.split(partition)
                if (partition[0] == cls.__name__):
                    dic[m] = self.__objects[m]
            return (dic)
        else:
            return self.__objects

    def new(self, obj):
        """This will add a new object to a given obj"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj


    def save(self):
        """Saves storage dictionary to jison file path"""
        my_dict = {}
        for m, n in self.__objects.items():
            my_dict[m] = n.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """Loads storage dictionary from file to the jison path"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for m, n in (json.load(f)).items():
                    n = eval(n["__class__"])(**n)
                    self.__objects[m] = n
        except FileNotFoundError:
            pass

    def close(self):
        """This will call for  the reload command"""
        self.reload()
