#!/usr/bin/python3
""" A module contain the command interpretor for BaseModel class """
import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """ Command processor for Base Model class """

    prompt = "(hbnb) "
    __classes = {"BaseModel"}

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
                o = obj.to_dict()
                if (o["__class__"] == args[0].strip()
                        and o["id"] == args[1].strip()):
                    print(eval(args[0].strip())())
                    break
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
