#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """this class defines all common attributes or methos for other class. i.e class where other classes will inherit from
    """

    def __init__(self, *args, **kwargs):
        """instantiation construct of attribute                           """
        if kwargs:
            for key, value in kwargs.item():
                if key = "__class__":
                    continue
                if key in("updated_at", ."created_at"):
                    setattr(self, key, value)
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """
        prints the class name, self.id and self.dict in dictionary representation
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}]".format(class_name, self.id, self.__dict__)
    def save(self):
        """
        udates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        This returns the a dictionary containing keys and valuesof the dict of the instance
        """
        only_instance_to_dict = self.__dict__.copy()
        #class_name = self.__class__.__name__
        only_instance_to_dict["__class__"] = self.__class__.__name__
        only_instance_to_dict["created_at"] = self.created_at.isoformat()
        only_instance_to_dict["updated_at"] = self.updated_at.isoformat()
        return only_instance_to_dict

if __name__ == "__main__":
    my_class_model = BaseModel()
    my_class_model.name = "Buchi and Tembi"
    my_class_model.my_number = 89
    print(my_class_model)
    my_class_model.save()
    print(my_class_model)
    my_class_model_json = my_class_model.to_dict()
    print(my_class_model_json)
    print("Jason of my_class_model:")
    for key in my_class_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_class_model_json[key]), my_class_model_json[key]))
