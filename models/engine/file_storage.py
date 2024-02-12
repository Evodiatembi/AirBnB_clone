#!/usr/bin/python3

import os

import json

from models.base_model import BaseModel

from models.user import user

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    __our_classes = {
        "BaseModel": BaseModel,
    }

    def all(self):
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        class_name = obj.__class__.__name__
        instance_id = obj.id

        key = f"{class_name}.{instance_id}"

        self.__objects[key] = obj

    def save(self):
        """
        this method saves and serializes __objects
        to the JSON file (path: __file_path)
        """
        new_dict = {}

        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(new_dict, file, indent=4)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists otherwise
        do nothing. If the file doesn’t exist, no exception
        should be raised)
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                my_objects = json.load(file)

            for key, value in my_objects.items():
                class_name = value["__class__"]

                self.__objects[key] = self.__our_classes[class_name](**value)
        except FileNotFoundError:
            pass
