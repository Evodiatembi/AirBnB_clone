#!/usr/bin/python3

import cmd
import sys
from models.base_model import BaseModel
#from models.user import user
 models import storage
from models.user import user
#from models import storage
>>>>>>> parent of 446c694 (updated)


class HBNBCommand(cmd.Cmd):
    prompt = "hbnb "
    my_class_name = ["BaseModel"]

    def do_emptyline(self):
        """ This does nothing when an empty-line is entered in the console"""
        pass

    def do_create(self, line):
        ''' This creates a user with a unique identification'''
        if len(line.split()) != 2:
            print("** class name missing **")
        elif line.split()[0] not in self.my_class_name:
            print("** class doesn't exist **")
        else:
            new_created_instance = BaseModel()
            new_created_instance.save()
            print(new_created_instance.id)

    def do_show(self, line):
        """ Shows whatever that has been created by the base class"""
        if len(line.split()) == 0:
            print("** class name missing **")
        elif line.split()[0] not in self.my_class_name:
            print("** class doesn't exist **")
        elif len(line.split()) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(line.split()[0], line.split()[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        This method destroys whatever instance or
        attributes that is no longer needed
        """
        if len(line.split()) == 0:
            print("** class name missing **")
        elif line.split()[0] not in self.my_class_name:
            print("** class doesn't exist **")
        elif len(line.split()) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(line.split()[0], line.split()[1])
            if key in objects:
                del objects[key]
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        This method prints all instances of all classes as a string
        """
        objects = storage.all()
        if len(line.split()) == 0:
            for key, value in objects.items():
                print(str(value))
        elif line.split()[0] not in self.my_class_name:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == line.split()[0]:
                    print(str(value))

    def do_update(self, line):
        """
        Updates an instance of the class that was created,
        i.e <class name> <id> <attribute_name>
        """
        if len(line.split()) == 0:
            print("** class name missing **")
        elif line.split()[0] not in self.my_class_name:
            print("** class doesn't exist **")
        elif len(line.split()) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(line.split()[0], line.split()[1])
            if key not in objects:
                print("** no instance found **")
            elif len(line.split()) < 3:
                print("** attribute name missing **")
            elif len(line.split()) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                attr_name = line.split()[2]
                attr_value = line.split()[3]
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
    if sys.stdin.isatty():
       # hbnb_cmd.cmdloop()
    else:
        for line in sys.stdin:
            hbnb_cmd.onecmd(line.strip())
