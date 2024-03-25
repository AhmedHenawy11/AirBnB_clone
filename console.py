#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ CMD Class """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
