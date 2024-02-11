#!/usr/bin/python3

#'''This is a command line interface to interact with the developer'''

import cmd
import re

class HBNBCommand(cmd.Cmd):
    prompt = "hbnb "
    my_class_name = ["BaseModel"]
    def do_emptyline(self):
        """ This does nothing when an empty-line is entered in the consol"""

    def do_create(self, line):
        ''' this creates a user with a unique identification'''
        if len(line.split()) != 2:
            print("** class name missing **")
        elif line[0] not in self.my_class_name:
            print("** class doesn't exist")
        else:
            new_created_instance = BaseModel()
            new_created_instance.save()
            print(new_created_instance.id)
    def do_show(self, line):
        """ shows whatever that has been created by the baseclass"""
        if len(line.split()) == 0:
            print("** class name missing **")
        elif line[0] not in self.my_class_name:
            print("** class doesn't exist **")
        elif len(line) < 2:
            print("** istance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(line[0], commands[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """ This method destroys whatever instance or attributes that is no longer needed"""
        if len(line.split()) == 0:
            print("** class name missing")
        elif line[0] not in self.my_class_name:
            print("** class doesn't exist **")
        elif len(line) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(line[0], line[0])
            if key in objects:
                del oblects[key]
            else:
                print("** no instance found **")

    def do_all(self, line):
        """this method peints all instances of all classes as a string"""
        objects = storage.all()
        if len(line.split()) == 0:
            for key, value in objects.items():
                print(str(value))
        elif (line[0]) not in self.my_class_name:
              print("** class doesn't exist **")
        else:
              for key, value in objects.items():
                  if key.split('.')[0] == line[0]:
                      print(str(value))

    def do_update(self, line):
        """ updates an instance of the class that was created, i.e <class name> <id> <attribute_name>"""
        if len(line.split()) == 0:
            print("** class name missing **")
        elif line[0] not in self.my_class_name:
            print("** class doesn't exist **")
        elif len(line) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(line[0], line[1])
            if key not in objects:
                print("** no istance found **")
            elif len(line) < 3:
                print("** attribute name missing **")
            elif len(line) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                attr_name = line[2]
                attr_value = line[3]
                try:
                    attr_value = eval(attr_value)
                except Exeption:
                    pass
                setattr(obj, attr_name, attr_value)
                obj.save()
    def do_EOF(self, line):
        """exit quits the shell"""
        print()
        return True
    def do_quit(self, line):
        """ this works similarly like the EOF used to exit the shell"""
        return True
    print()
if __name__ == '__main__':
    HBNBCommand().cmdloop()
