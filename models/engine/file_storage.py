#!/usr/bin/python3

import os

import json

from models.base_model import BaseModel

from models.user import user

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        class_name = obj.__class__.__name__
        key = "{}.{}".format(class_name, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        return FileStorage.__objects

    def save(self):
        """
        this method saves and serializes __objects
        to the JSON file (path: __file_path)
        """
        all_new_obj = FileStorage.__onjects
        obj_dict = {}
        for ob in all_new_obj.keys:
            obj_dict[ob] = all_new_obj[ob].to_dict()

        with open(FileStorag.__self.__file_path, "w", encoding="utf-8") as file:
            json.dump(new_dict, file, indent=4)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists otherwise
        do nothing. If the file doesn’t exist, no exception
        should be raised)
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)
                    for key, value in obj_dict.items():
                        class_name, obj_id key.split('.')
                        clas = eval(class_name)
                        old_inst = clas(**value)
                        FilStorage.__objects[key] = created_inst
        except FileNotFoundError:
            pass 
