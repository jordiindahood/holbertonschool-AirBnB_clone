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
from models import storage


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
                print(f'["{obj[key]}"]')
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Destroy an object by its ID."""
        command = line.split()
        if not line:
            print("** class name missing **")
        elif command[0] not in globals():
            print("** class doesn't exist **")
        elif len(command) < 2:
            print("** instance id missing **")
        else:
            key = f"{command[0]}.{command[1]}"
            obj = storage.all()
            if key in obj:
                del obj[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        List all instances of a given class.
        """
        class_name = line.split(".")[0]
        if class_name not in globals().keys() and len(line) != 0:
            print("** class doesn't exist **")
        else:
            obj = storage.all()
            print(list(str(obj[key]) for key in obj if class_name in key))

    def do_update(self, line):
        """
        update
        """
        command = line.split()
        if not line:
            print("** class name missing **")
        elif command[0] not in globals():
            print("** class doesn't exist **")
        elif len(command) < 2:
            print("** instance id missing **")
        elif len(command) < 3:
            print("** attribute name missing **")
        elif len(command) < 4:
            print("** value missing **")
        else:
            key = f"{command[0]}.{command[1]}"
            obj = storage.all()
            if key in obj:
                obj[key].__dict__[command[2]] = command[3]
                storage.save()
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
