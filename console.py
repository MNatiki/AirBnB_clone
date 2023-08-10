#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
import models
from models.user import User
"""importing everything for `HBNBCommand` class"""


class HBNBCommand(cmd.Cmd):
    """
    The `HBNBCommand` class is a command-line interface that
    allows users to interact with a process and execute commands
    such as quitting or handling the end of file signal.
    """
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
    }

    def do_quit(self, *args):
        """`quit` command quits the process at hand"""
        return True

    def do_EOF(self, *args):
        """`EOF` is used to handle the end of file (EOF) signal."""
        print("")
        return True

    def emptyline(self):
        """
        The function "emptyline" does nothing and serves as a placeholder.
        """
        pass

    def do_create(self, args):
        """`create` creates a new instance of a class and saves it,
         printing the ID of the new instance."""
        args = args.split(" ")
        if args == ['']:
            print("** class name missing **")
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        new_instance = eval(args[0])()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """`show` Usage: show <class> <id>
        Display the string representation of a class instance."""
        args = args.split(" ")
        if len(args) == 1 and args == ['']:
            print("** class name missing **")
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] + "." + args[1] not in models.storage.all().keys():
            print("** no instance found **")
            return
        print(models.storage.all()[args[0] + "." + args[1]])

    def do_destroy(self, args):
        """`do_destroy` Usage: destroy <class> <id>
        Delete a class instance of a given id."""
        args = args.split(" ")
        if len(args) == 1 and args == ['']:
            print("** class name missing **")
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] + "." + args[1] not in models.storage.all().keys():
            print("** no instance found **")
            return
        del models.storage.all()[args[0] + "." + args[1]]
        models.storage.save()

    def do_all(self, args):
        """`all`Usage: all or all <class>
        Display string representations of all instances of a given class."""

        args = args.split(" ")
        if args == ['']:
            for i in models.storage.all().values():
                print(i)
            return
        if args[0] not in self.__classes and args != ['']:
            print("** class doesn't exist **")
            return
        for i in models.storage.all().keys():
            if args[0] in i:
                print(models.storage.all()[i])

    def do_update(self, args):
        """`update`
        update <class name> <id> <attribute name> "<attribute value>"
        Updates current instance of a class."""

        args = args.split(" ")
        if len(args) == 1 and args == ['']:
            print("** class name missing **")
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] + "." + args[1] not in models.storage.all().keys():
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        obj = models.storage.all()[args[0] + "." + args[1]]
        try:
            if str(int(args[3])) == args[3]:
                setattr(obj, args[2], int(args[3]))
                obj.save()
                return
        except ValueError:
            try:
                if str(float(args[3])) == args[3]:
                    setattr(obj, args[2], float(args[3]))
                    obj.save()
                    return
            except ValueError:
                setattr(obj, args[2], (args[3]).replace("\"", ""))
                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
