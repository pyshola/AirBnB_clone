#!/usr/bin/python3
""" class FileStorage
    serializes instances to a JSON file
    and deserializes JSON file to instances """
import json
import uuid
import os
import os.path as path
from datetime import datetime
from models.base_model import BaseModel


class FileStorage:
    """ construct """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return dictionary objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in dictionary the obj with key <obj class name>.id """
        FileStorage.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new_dictionary = {}
        with open(self.__file_path, mode="w", encoding='UTF-8') as fname:
            for k, v in self.__objects.items():
                new_dictionary[k] = v.to_dict()
            json.dump(new_dictionary, fname)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)"""
        if path.isfile(self.__file_path):
            with open(self.__file_path, mode="r", encoding='UTF-8') as f:
                for k, v in (json.load(f)).items():
                    v = eval(v["__class__"])(**v)
                    self.__objects[k] = v