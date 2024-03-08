#!/usr/bin/python3
""" a console that contains the entry point of the command interpreter"""
import cmd
import json
from models.base_model import BaseModel
from models.place import Place
from models.review import Review
from models.city import City
from models.user import User
from models.state import State

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

    def do_create(self, line):
        """Usage: create <classname>
        Starts a new instance of commandsecified class and saves it with a unique id.
                        Prints the newly created object's id"""
        if not line:
            print("** class name missing **")
            return
        if line in globals():
            cls = globals()[line]()
            cls.save()
            print(cls.id)
        else:
            print("** class doesn't exist **")
        
    def do_show(self, line):
        """Usage: show [<classname>.<instance-id> | <classname> ]
        displays information about an individual object\
or all objects of a particular class.
        """
        commands = line.split()
        if not line:
            print("** class name missing **")
        elif commands[0] not in globals():
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            key = f"{commands[0]}.{commands[1]}"
            obj = storage.all()
            if key in obj:
                print(obj[key])
            else:
                print("** no instance found **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
