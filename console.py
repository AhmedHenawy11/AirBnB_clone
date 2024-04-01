#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ CMD Class """

    prompt = "(hbnb) "

    def do_quit(self, command):
        """ Method to exit the HBNB console"""
        exit()

    def help_quit(self):
        """ Prints the help documentation for quit  """
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
        exit()

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
