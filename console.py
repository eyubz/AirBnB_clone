#!/usr/bin/python3
import cmd
""" A module contain the command interpretor for BaseModel class """


class HBNBCommand(cmd.Cmd):
    """ Command processor for Base Model class """

    prompt = "(hbnb) "

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
