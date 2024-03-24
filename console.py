#!/usr/bin/python3
""" A module contain the command interpretor for BaseModel class """
import cmd
from models.base_model import BaseModel
from models.user import User
import models


class HBNBCommand(cmd.Cmd):
    """ Command processor for Base Model class """

    prompt = "(hbnb) "
    __classes = {"BaseModel", "User", "State", "City",
                 "Amenity", "Place", "Review"}

    """ Handle end of file """
    def do_EOF(self, arg):
        """ Exit on ctrl+D """
        print("")
        return True

    """ Handle quitting the interpretor """
    def do_quit(self, arg):
        """ Quit command to quit the interpretor """
        return True

    """ Handle empty line + ENTER """
    def emptyline(self):
        """ This does not execute anything """
        pass

    """ Create a new instance """
    def do_create(self, arg):
        """ Create an instance of a given object
        and saves it to json file """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            class_name = args[0].strip()
            obj = eval(class_name)()
            obj.save()
            print(obj.id)

    """ Show string representation """
    def do_show(self, arg):
        """ Print string representation of a class
        based on the  class name """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            for obj in objects.values():
                if (obj.__class__.__name__ == args[0].strip()
                        and obj.id == args[1].strip()):
                    print(obj.__str__())
                    break
            else:
                print("** no instance found **")
    """ Destroy an instance """
    def do_destroy(self, arg):
        """ Destroy an instance based on class name and
        id and the save changes to file """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            for key, obj in objects.items():
                if (obj.__class__.__name__ == args[0].strip()
                        and obj.id == args[1].strip()):
                    del objects[key]
                    models.storage.save()
                    break
            else:
                print("** no instance found **")
    """ Print all string representation """
    def do_all(self, arg):
        """ Print string representation all instances
        based or not on class name """
        args = arg.split()
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            ans = []
            objects = models.storage.all()
            for o in objects.values():
                if len(args) > 0 and (o.__class__.__name__ == args[0].strip()):
                    ans.append(o.__str__())
                elif len(args) == 0:
                    ans.append(o.__str__())
            print(ans)

    """ Update an instance """
    def do_update(self, arg):
        """ Update an instance by class name and id """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            objects = models.storage.all()
            for key, obj in objects.items():
                if (obj.__class__.__name__ == args[0].strip() and
                        obj.id == args[1].strip()):
                    if args[2] not in obj.__dict__:
                        setattr(obj, args[2], args[3].strip('"'))
                    else:
                        t = type(getattr(obj, args[2]))
                        if t == "int":
                            setattr(obj, args[2], int(args[3]))
                        elif t == "float":
                            setattr(obj, args[2], float(args[3]))
                        elif t == "str":
                            setattr(obj, args[2], args[3].strip('"'))
                    break
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
