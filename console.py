#!/usr/bin/python3
""" a consol that contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    """Hearthstone Botnet Command Interface."""

    def do_EOF(self, line):
        """Exit from the program."""
        return True

    def do_quit(self, line):
        """Exit from the program."""
        return True

    def emptyline(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
