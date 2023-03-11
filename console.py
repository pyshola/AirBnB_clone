#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd
from models.base_model import BaseModel
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):

    """Class for the command interpreter."""

    prompt = "(hbnb) "

    def default(self, line):
        """Catch commands if nothing else matches then."""
        # print("DEF:::", line)
        # self._precmd(line)
        return line
    
    def do_EOF(self, line):
        """Handles End Of File character.
        """
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program.
        """
        return True

    def emptyline(self):
        """Doesn't do anything on ENTER.
        """
        pass

    
        


if __name__ == '__main__':
    HBNBCommand().cmdloop()
