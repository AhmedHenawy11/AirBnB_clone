import cmd 

class MyInterpreter(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        return True


MyInterpreter().cmdloop()
