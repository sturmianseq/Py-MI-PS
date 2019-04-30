from PyMIPS.lexer import *
from PyMIPS.Datastructure.commands import get_command
from PyMIPS.AST.class_utils import *


class I_Type:
    def __init__(self, command=None, target=None, source=None, immediate=None):
        self.command = command
        self.target_register = create_register(target)
        self.source_register = create_register(source)
        self.immediate = create_immediate(immediate)
        self.func = get_command(self)

    def __call__(self):
        return self.func()

    def __repr__(self):
        return f"I_Type({self.command} {self.target_register}, {self.source_register}, {self.immediate})"


class R_Type:
    def __init__(self, command=None, destination=None, r1=None, r2=None, shamt=None):
        self.command = command
        self.destination = create_register(destination)
        self.r1 = create_register(r1)
        self.r2 = create_register(r2)
        self.func = get_command(self)

    def __call__(self):
        return self.func()

    def __repr__(self):
        return f"R_Type({self.command} {self.destination}, {self.r1}, {self.r2})"


class J_Type:
    def __init__(self, command, address):
        self.command = command
        self.address = address

    def __repr__(self):
        return f"{self.command}({self.address})"


def unpack(contents) -> list:
    # Check to see if tuple
    if type(contents) != tuple:
        return [contents]
    result = []
    while type(contents) == tuple:
        value, contents = contents
        if type(value) == tuple:
            value, contents = contents, value

        result.append(value)
    result.append(contents)
    return result

