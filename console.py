#!/usr/bin/python3

import cmd
import shlex
import sys
from models.base_model import BaseModel
from models.engine import storage
#from models.user import user
#from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "hbnb "
    my_class_name = ["BaseModel"]

    def emptyline(self):
        """ This does nothing when an empty-line is entered in the console"""
        pass

    def do_create(self, line):
        ''' This creates a user with a unique identification'''
        command_line = shlex.split(line)
        if len(command_line) == 0:
            print("** class name missing **")
        elif command_line[0] not in self.my_class_name:
            print("** class doesn't exist **")
        else:
            new_created_instance = BaseModel()
            new_created_instance.save()
            print(new_created_instance.id)

    def do_show(self, line):
        """ Shows whatever that has been created by the base class"""
        command_line = shlex.split(line)
        if len(command_line) == 0:
            print("** class name missing **")
        elif command_line[0] not in self.my_class_name:
            print("** class doesn't exist **")
        elif len(command_line) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(command_line[0], command_line()[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        This method destroys whatever instance or
        attributes that is no longer needed
        """
        command_line = shlex.split(line)
        if len(command_line) == 0:
            print("** class name missing **")
        elif command_line[0] not in self.my_class_name:
            print("** class doesn't exist **")
        elif len(command_line) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(command_line[0], command_line()[1])
            if key in objects:
                del objects[key]
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        This method prints all instances of all classes as a string
        """
        command_line = shlex.split(line)
        objects = storage.all()
        if len(command_line) == 0:
            for key, value in objects.items():
                print(str(value))
        elif command_line[0] not in self.my_class_name:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == command_line[0]:
                    print(str(value))

    def do_update(self, line):
        """
        Updates an instance of the class that was created,
        i.e <class name> <id> <attribute_name>
        """
        command_line = shlex.split(line)
        if len(command_line) == 0:
            print("** class name missing **")
        elif command_line[0] not in self.my_class_name:
            print("** class doesn't exist **")
        elif len(command_line) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(command_line[0], command_line[1])
            if key not in objects:
                print("** no instance found **")
            elif len(command_line) < 3:
                print("** attribute name missing **")
            elif len(command_line) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                attr_name = comman_line[2]
                attr_value = comman_line[3]
                try:
                    attr_value = eval(attr_value)
                except Exception:
                    pass
                setattr(obj, attr_name, attr_value)
                obj.save()

    def do_EOF(self, line):
        """Exit quits the shell"""
        print()
        return True

    def do_quit(self, line):
        """
        This works similarly like the EOF
        used to exit the shell
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
